import reflex as rx

from rxconfig import config
from ..state import UserData

class State(rx.State):
    pass
        
class UserName(UserData):
    def login(self):
        username, mail= self.get_user_info()
        print(f"User info - Name: {username}, Age: {mail}")
            

# color pallete states
GRAY = "#daecf2"
RED = "#ff414d"
LAZURE = "#19a6b6"
DARK_LAZURE = "#012d40"

from sqlmodel import select,or_
from ..database import Tours

import asyncio

class ToursDBState(rx.State):
    # Определяем переменную состояния для хранения списка туров
    tours: list[Tours] = []
    is_loading: bool = False


    @rx.event
    def get_regular_tours(self) -> list[Tours]:
        try:
            with rx.session() as session:
                query = select(Tours).where(Tours.stars <= 4)
                self.tours = session.exec(query).all()
        except Exception as e:
            print(f"[WARNING] Error getting tours from BD (get_regular_tours): {e}")
        # test
        print(f"\033[34m[INFO] SQL запрос: {query}")  # Выводим SQL запрос
        print(f"[INFO] All Data: {self.tours}")  # Выводим полученные данные
            
            
    @rx.event
    async def get_beach_tours(self):
        try:
            with rx.session() as session:
                query = select(Tours).where(Tours.price == 123)
                self.tours = session.exec(query).all()
        except Exception as e:
            print(f"[WARNING] Error getting tours from BD (get_beach_tours): {e}")
           
            
            
"""
FOR DB SESSION
            with rx.session() as session:
            query = select(Tours)
            tours = session.exec(query).all()
            # Convert to list of dictionaries
            self.tours = [
                {
                    "src_img": tour.src_img,
                    "text": tour.text,
                    "url_tour": tour.url_tour, 
                    "price": tour.price,
                    "stars": tour.stars
                }
                for tour in tours
            ]
            print(f'''
                  \n{self.tours}\n
            ''')
            """


'''
rx.text(f"Hello {UserName.username}"),
rx.text(f"Hello {UserName.mail}"),
'''
# ! Make moduls in UI folder
def filter_card(
        icon: str,
        text: str,
        bgcolor: str,
        icon_color: str,
        id_box: str,
        url: str
    ) -> rx.Component:
    return rx.link(
        rx.box(
            rx.vstack(
                rx.icon(tag=icon,color=icon_color),
                rx.text(text, size="3",color="black"),
                align="center",
                justify="center",
                height="100%",
                width="100%",
                spacing="2",
            ),
            id=id_box,
            style={
                "align_self": "center",
                "display": "flex",
                "align_items": "center",
                "justify_content": "center",
                "background-color": bgcolor,
                # "border": f"2px {border_color} solid",
                "border-radius":"10px",
                "height":"90px",
                "width":"90px",
            },
        ),
        href=url,
        style={"text_decoration": "none"},
    )


def ad_card(
    icon: str,
    text: str,
    gradient_color1: str,
    gradient_color2: str,
    degreee: str,
    description: str,
    id_ad_card:str,
    
    ) -> rx.Component:
    return rx.box(
        # up text|icon
        rx.box(
            rx.hstack(
                rx.icon(icon,transform="rotate(90deg)",size=60),
                rx.text.strong(text,style={"font-size":"20px","text-align":"center"}),
            ),
            margin_bottom="5px",
            justify="center",
            padding="10px 10px"
            
        ),
        rx.divider(height="3px",border_radius="10px"),
        # description
        rx.box(
            rx.text(description,margin_top="10px",),
        ),
        
        width="50%",
        height="150px",
        
        background=f"linear-gradient({degreee}deg, rgba({gradient_color1}) 0%, rgba({gradient_color2}) 100%);",
        border_radius="10px",
        padding="10px",
        text_align="center",
        margin_right="10px",
        
        id=id_ad_card
    ),

def tour_card(
    src_img: str,
    text: str,
    url_tour: str,
    price: str,
    stars: str,
    ) -> rx.Component:
    return rx.link(
        rx.box(
            rx.box(
                position="absolute",
                top="134px",
                left="0px",
                background_color=DARK_LAZURE,
                width="100%",
                height="62px",
                style={
                    "-webkit-border-bottom-right-radius": "10px",
                    "-webkit-border-bottom-left-radius": "10px",
                    "-moz-border-radius-bottomright": "10px",
                    "-moz-border-radius-bottomleft": "10px",
                    "border-bottom-right-radius": "10px",
                    "border-bottom-left-radius": "10px",
                        
                },
                
            ),
            rx.image(
                src=src_img,
                height="21vh",
                width="100%",
                border_radius="10px",
                margin_top="30px",  
                
            ),
            rx.text(
                text,
                color="#fff",
                position="absolute",
                top="140px",
                left="10px",
                style={
                    "font-size": "30px",
                    "font-weight": "bold",
                    # "background-color":"white",
                    # "border-radius":"10px",
                    
                },
            ),
            rx.hstack(
                rx.text(
                    f"{price}",
                    color="#000",
                    position="absolute",
                    top="147px",
                    left="300px",
                    background_color="#fff",
                    padding="5px",
                    border_radius="30px",
                ),
                rx.box(
                    rx.hstack(
                        rx.icon(tag="star",color="yellow"),
                        rx.text(
                            stars,
                            color="#fff",
                            weight="bold",
                            size="4",
                        ),
                    
                    ),
                    position="absolute",
                    top="152px",
                    left="110px",
                ),
                
            ),
            
            position="relative",
            
            
        ),
        url=url_tour
    )

def tours_list() -> rx.Component:
    return rx.box(
        rx.mobile_only(
            #page
            rx.container(
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.hstack(
                                rx.icon(tag="slack",margin="5px",color=RED),
                                rx.text(f"Hello, {UserName.username}",size="7"),
                            ),
                            
                        ),
                        # profile
                        rx.link(
                            rx.icon(tag="user", margin="5px",color=RED),
                            href="/profile",
                            style={"background-color":"#f4f3f7", "border-radius":"50%","padding":"2px"},
                           
                        ),
                        justify="between",
                        align="center",
                    ),
                    style={"align-items": "center","align-self": "center","padding":"10px 0px"},
                ),
                #header
                rx.box(
                    rx.text("Discover your next trip and desination",size="8",weight="bold"),
                    
                    margin_top="40px",    
                ),
                # input
                rx.box(
                    rx.flex(
                        # ! make dinamic changes 
                        rx.input(
                            rx.input.slot(rx.icon("search",margin_left="10px"),),
                            id="search-tour-input",
                            placeholder="Search tour...",
                            size="3",
                            style={
                                "border-radius":"30px",
                                "width":"90%",
                                "height":"50px",
                                "--text-field-focus-color":LAZURE,
                            },
                        ),
                        rx.button(
                            rx.icon(tag="settings-2"),
                            style={
                                "margin-left":"10px",
                                "border-radius":"50%",
                                "padding":"17px 6px",
                                "align-self":"center",
                                "background-color":RED,
                            },
                        ),
                    ),
                    margin_top="20px",    
                    width="100%",
                ),
                # filter list
                rx.box(
                    rx.scroll_area(
                        rx.flex(
                            # hotel
                            filter_card(
                                icon="bed-double",
                                text="Tours",
                                bgcolor="#fff7ee",
                                icon_color="#fb8f1d",
                                id_box="hotel-id",
                                url="/hotels",
                            ),
                            # flight
                            filter_card(
                                icon="plane",
                                text="Planes",
                                bgcolor="#ecf5f8",
                                icon_color="#3d9ae9",
                                id_box="flight-id",
                                url="#",
                            ),
                            # journal
                            filter_card(
                                icon="book-heart",
                                text="Journal",
                                bgcolor="#fef2ed",
                                icon_color="#fd714c",
                                id_box="journal-id",
                                url="#",
                            ),
                            # attractions
                            filter_card(
                                icon="award",
                                text="Attractions",
                                bgcolor="#fcf5e8",
                                icon_color="#df932d",
                                id_box="attractions-id",
                                url="#",
                            ),
                            # sales
                            filter_card(
                                icon="percent",
                                text="Sales",
                                bgcolor="#dffbf2",
                                icon_color="#32edaf",
                                id_box="sales-id",
                                url="#",
                            ),
                            
                            
                            gap="10px"
                        ),
                        align="center",
                        scrollbars="horizontal",

                    ),
                    
                    
                    margin_top="25px"
                ),
                # AD
                # wrapper for DB
                rx.box(
                # ! make AD form in admin pannel to add or delete card
                    rx.scroll_area(
                        rx.flex(
                            ad_card(
                                icon="ticket-percent",
                                text="20% Discount",
                                gradient_color1="224,2,37,1",
                                gradient_color2="218,61,101,1",
                                degreee="225",
                                description="Buy first tour!",
                                id_ad_card="1",
                            ),
                            ad_card(
                                icon="ticket-percent",
                                text="20% Discount",
                                gradient_color1="224,2,37,1",
                                gradient_color2="218,61,101,1",
                                degreee="225",
                                description="Buy first tour!",
                                id_ad_card="2",
                            )
                        ),
                        margin_top="40px",
                        color="white",
                        
                    ),
                    # ! give id to make display:none and show that user are selected in filter
                    id="list_of_ad_cards"
                ),
                # filter of tours type
                rx.box(
                    rx.text("Explorer by category",style={"font-size":"20px"},weight="bold"),
                    # filter
                    rx.box(
                        rx.scroll_area(
                            rx.flex(
                                # ! when your click on button, BG color will change
                                rx.button(
                                    rx.icon(tag="tram-front"),
                                    rx.text("Tours"),
                                    background=LAZURE,
                                    border_radius="30px",
                                    # * tour
                                    on_click=ToursDBState.get_regular_tours
                                ),
                                rx.button(
                                    rx.icon(tag="tree-palm"),
                                    rx.text("Beach"),
                                    background="#f0f1f5",
                                    color=DARK_LAZURE,
                                    border_radius="30px",
                                    # * beach
                                    on_click=ToursDBState.get_beach_tours
                                    
                                ),
                                rx.button(
                                    rx.icon(tag="arrow-down-narrow-wide"),
                                    rx.text("Price down"),
                                    background="#f0f1f5",
                                    color=DARK_LAZURE,
                                    border_radius="30px",
                                    # * price down
                                    
                                ),
                                rx.button(
                                    rx.icon(tag="arrow-up-narrow-wide"),
                                    rx.text("Price up"),
                                    background="#f0f1f5",
                                    color=DARK_LAZURE,
                                    border_radius="30px",
                                    # * price up
                                    
                                ),
                                rx.button(
                                    rx.icon(tag="crown"),
                                    rx.text("Popular"),
                                    background="#f0f1f5",
                                    color=DARK_LAZURE,
                                    border_radius="30px",
                                    # * popular
                                    
                                ),
                                gap="10px",
                            ),
                        ),
                    ),
                    
                    margin_top="20px",
                    # ! give id to make display:none and show that user are selected in filter
                    id="list_of_tours_cards"
                ),
                # tours
                rx.box(
                    rx.cond(
                        ToursDBState.is_loading,
                        rx.center(rx.spinner()),
                        rx.foreach(
                            ToursDBState.tours,
                            lambda tour: tour_card(
                                src_img=tour.src_img,
                                text=tour.text,
                                url_tour=tour.url_tour,
                                price=tour.price,
                                stars=tour.stars
                            )
                        )
                    ),
                    margin_top="30px",
                    on_mount=ToursDBState.get_regular_tours  #* call function when page is loaded
                ),
            ), 
            # navbar()
            
            ),
        
    # hello.py
    )
        