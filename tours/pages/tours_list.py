import reflex as rx

from ..state import UserData
from sqlmodel import select,or_
from ..database import Tours

from ..ui.colored_card import colored_card

#* BACKEND
from ..backend.components.terminal_notofication import terminal_info,terminal_warning

class State(rx.State):
    pass
        
            

# color pallete states
GRAY = "#daecf2"
RED = "#ff414d"
LAZURE = "#19a6b6"
DARK_LAZURE = "#012d40"




class ToursDBState(rx.State):
    # Определяем переменную состояния для хранения списка туров
    tours: list[Tours] = []
    is_loading: bool = False
    
    # active button, needs to change background color XD
    active_button: str = "tours"

    #* All tours in DB
    @rx.event
    async def get_regular_tours(self) -> list[Tours]:
        self.active_button = "tours"
        try:
            with rx.session() as session:
                query = select(Tours).order_by(Tours.id.desc())
                self.tours = session.exec(query).all()
        except Exception as e:
            terminal_warning(f"[WARNING] Error getting tours from BD (get_regular_tours): {e}")
        # test
        # terminal_info(f"INFO] SQL query: {query}")  # send SQL query on terminal
        # terminal_info(f"[INFO] All Data: {self.tours}")  # Show all data in DB to terminal
            
    @rx.event
    async def get_beach_tours(self):
        self.active_button = "beach"
        try:
            with rx.session() as session:
                query = select(Tours).where(Tours.beach == True)
                self.tours = session.exec(query).all()
        except Exception as e:
            terminal_warning(f"[WARNING] Error getting tours from BD (get_beach_tours): {e}")
            
    @rx.event
    async def get_low_price_tours(self):
        self.active_button = "price_down"
        try:
            with rx.session() as session:
                query = select(Tours).order_by(Tours.price.asc())
                self.tours = session.exec(query).all()
        except Exception as e:
            terminal_warning(f"[WARNING] Error getting tours from BD (get_low_price_tours): {e}")
    
    @rx.event
    async def get_hight_price_tours(self):
        self.active_button = "price_up"
        try:
            with rx.session() as session:
                query = select(Tours).order_by(Tours.price.desc())
                self.tours = session.exec(query).all()
        except Exception as e:
            terminal_warning(f"[WARNING] Error getting tours from BD (get_hight_price_tours): {e}")
            
    @rx.event
    async def get_popular_tours(self):
        self.active_button = "popular"
        try:
            with rx.session() as session:
                query = select(Tours).where(Tours.popular == True).order_by(Tours.popular.desc())
                self.tours = session.exec(query).all()
        except Exception as e:
            terminal_warning(f"[WARNING] Error getting tours from BD (get_popular_tours): {e}")
           
            

# ! Make moduls in UI folder



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
# ! REFACTORE STYLE!
def tour_card(
    tour: Tours,
    src_img: str,
    text: str,
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
                    f"${price}",
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
        href=f"/tours/{tour.id}",
        is_external=False
    )


def filter_buttons(
        icon: str,
        text: str,
        id_button: str,
        function_query: str,
    ):
    return rx.button(
        rx.icon(tag=icon),
        rx.text(text),
        background=rx.cond(
            ToursDBState.active_button == id_button,
            # not selected
            LAZURE,
            # selected
            "#f0f1f5"
        ),
        color=rx.cond(
            ToursDBState.active_button == id_button,
            # not selected
            "white",
            # selected
            DARK_LAZURE
        ),
        border_radius="30px",
        # * tour
        on_click=function_query
    ),

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
                                rx.text(f"Hello, {UserData.username}",size="7"),
                            ),
                            
                        ),
                        # profile
                        rx.link(
                            rx.icon(tag="user", margin="5px",color=RED),
                            href="/profile",
                            style=rx.color_mode_cond(
                            light={"background":"#f4f3f7", "padding":"2px", "border-radius":"50%"},
                            dark={"background":"#2d3748", "padding":"2px", "border-radius":"50%"}
                        ),
                           
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
                                "width":"100%",
                                "height":"50px",
                                "--text-field-focus-color":LAZURE,
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
                            colored_card(
                                icon="bed-double",
                                text="Tours",
                                bgcolor="#fff7ee",
                                icon_color="#fb8f1d",
                                id_box="hotel-id",
                                url="/hotels",
                            ),
                            # flight
                            colored_card(
                                icon="plane",
                                text="Planes",
                                bgcolor="#ecf5f8",
                                icon_color="#3d9ae9",
                                id_box="flight-id",
                                url="/planes",
                            ),
                            # journal
                            colored_card(
                                icon="book-heart",
                                text="Journal",
                                bgcolor="#fef2ed",
                                icon_color="#fd714c",
                                id_box="journal-id",
                                url="#",
                            ),
                            # attractions
                            colored_card(
                                icon="award",
                                text="Attractions",
                                bgcolor="#fcf5e8",
                                icon_color="#df932d",
                                id_box="attractions-id",
                                url="#",
                            ),
                            # sales
                            colored_card(
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
                                #* tours
                                filter_buttons(
                                    icon="tram-front",
                                    text="Tours",
                                    id_button="tours",
                                    function_query=ToursDBState.get_regular_tours
                                ),
                                #* beach
                                filter_buttons(
                                    icon="tree-palm",
                                    text="Beach",
                                    id_button="beach",
                                    function_query=ToursDBState.get_beach_tours
                                ),
                                #* Price down
                                filter_buttons(
                                    icon="arrow-down-narrow-wide",
                                    text="Price down",
                                    id_button="price_down",
                                    function_query=ToursDBState.get_low_price_tours
                                ),
                                #* Price up
                                filter_buttons(
                                    icon="arrow-up-narrow-wide",
                                    text="Price up",
                                    id_button="price_up",
                                    function_query=ToursDBState.get_hight_price_tours
                                ),
                                #* Popular
                                filter_buttons(
                                    icon="crown",
                                    text="Popular",
                                    id_button="popular",
                                    function_query=ToursDBState.get_popular_tours
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
                            #! remake tour cards and add more info
                            lambda tour: tour_card(
                                tour=tour,
                                src_img=tour.src_img,
                                text=tour.text,
                                price=tour.price,
                                stars=tour.stars
                            )
                        )
                    ),
                    margin_top="30px",
                    on_mount=ToursDBState.get_regular_tours  #* call function when page is loaded
                ),
            ), 

            ),
        
    # hello.py
    )
        