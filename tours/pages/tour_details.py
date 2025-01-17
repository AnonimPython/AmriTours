import reflex as rx

#* DATABASE
from ..state import UserData
from sqlmodel import select,or_
from ..database import Tours
from typing import Optional

#* PAGES
from ..pages.error import error_404

#* UI
from ..ui.topbar import topbar,topbar_details
from ..ui.colored_card import colored_card

#* BACKEND
from ..backend.components.terminal_notofication import terminal_info,terminal_warning

# color pallete states
GRAY = "#daecf2"
RED = "#ff414d"
LAZURE = "#19a6b6"
DARK_LAZURE = "#012d40"

class TourDetailState(rx.State):
    #* Определяем переменную состояния tour типа Tours или None
    #* Optional[Tours] означает что переменная может быть либо объектом Tours, либо None
    #* None используется как начальное значение до загрузки данных
    tour: Optional[Tours] = None
    
    @rx.event
    async def get_tour_details(self):
        with rx.session() as session:
            
            #* Получаем id тура из параметров URL
            #* self.router.page.params - словарь с параметрами URL
            #* .get("pid", 0) - получаем значение параметра pid, если его нет - возвращаем 0
            #* int() - преобразуем строку в число потоскольку id тура в БД str 
                                                                    #! fix
            tour_id = int(self.router.page.params.get("id", 0))
            # terminal_info("(get_tour_details)==================")
            terminal_info(f"[INFO] tour_id: {tour_id}")
            
            #* Получаем объект тура из базы данных по его id
            #* session.get() - метод для получения одной записи по первичному ключу
            #* Tours - модель данных тура
            #* tour_id - идентификатор нужного тура
            #* Результат сохраняется в переменную состояния self.tour
            self.tour = session.get(Tours, tour_id)
            terminal_info(f"[INFO]  self.tour: {self.tour}")
            terminal_info("(get_tour_details)==================")
            
            
            
def tour_detail():
    return rx.box(
            rx.container(
            topbar_details("Let's go!"),
                rx.vstack(
                rx.cond(
                    TourDetailState.tour,
                    rx.box(
                        #* img
                        rx.box(
                            rx.image(
                                src=TourDetailState.tour.src_img,
                                height=300,
                                width="100%",
                                border_radius="20px",
                            ),  
                        ),
                        #* title | price
                        rx.box(
                            rx.flex(
                                rx.text(TourDetailState.tour.text, size="8", weight="bold"),
                                rx.text(f"${TourDetailState.tour.price}", size="8", weight="bold"),
                                justify="between",
                            ),
                            margin_top="30px",
                        ),
                        #* country | per person
                        rx.box(
                            rx.flex(
                                # county + icon
                                rx.box(
                                    rx.hstack(
                                        rx.icon(tag="earth",color="#919191",
                                                style={"align-self": "center","align-items": "center"}),
                                        rx.text(
                                            f"{TourDetailState.tour.country}",
                                            color="#919191",
                                            weight="light",
                                        ),
                                    ),
                                    
                                ),
                                # person
                                rx.box(
                                    rx.hstack(
                                        rx.icon(tag="user",color="#919191",
                                                style={"align-self": "center","align-items": "center"}),
                                        rx.text(
                                            f"Per person",
                                            color="#919191",
                                            weight="light",
                                        )
                                    ),
                                    
                                ),
                                justify="between",
                            ),
                            
                            margin_top="20px",
                        ),
                        rx.separator(
                            margin_top="20px",
                            background_color="rgb(145,145,145,0.5)",
                            height="1px"
                        ),
                        #* address | time | day | stars
                        rx.box(
                            # addres
                            rx.box(
                                rx.hstack(
                                    rx.icon(
                                        tag="map-pin",
                                        color="#919191",
                                        size=25,
                                        padding="5px",
                                        background_color="#d4d4d4",
                                        border_radius="50%",
                                    ),
                                    rx.text(
                                        f"{TourDetailState.tour.address}",
                                        weight="regular",
                                        size="5"
                                    ),
                                    width="100%",
                                    style={"align-self": "center","align-items": "center"}
                                ),
                                    margin_top="10px",
                                ),
                            #* time | day | stars
                            rx.box(
                                rx.flex(
                                    # time | day
                                    rx.box(
                                        rx.hstack(
                                        rx.icon(
                                            tag="clock-9",
                                            color="#919191",
                                            size=25,
                                            padding="5px",
                                            background_color="#d4d4d4",
                                            border_radius="50%",
                                        ),
                                        rx.text(
                                            f"{TourDetailState.tour.days} Days | {TourDetailState.tour.time} PM",
                                            weight="regular",
                                            size="5"
                                            
                                        ),
                                        style={"align-self": "center","align-items": "center"},
                                        width="100%"
                                        ),
                                        width="60%",
                                    ),
                                    # stars
                                    rx.box(
                                        rx.hstack(
                                            rx.icon(
                                                tag="star",
                                                color="gold",
                                                style={"align-self": "center","align-items": "center"},
                                                
                                            ),
                                            rx.text(f"{TourDetailState.tour.stars}",size="5"),
                                        ),
                                        
                                    # box stars   
                                    ),   
                                    justify="between",
                                ),
                                    margin_top="10px",
                                ),
                            margin_top="20px",
                        ),
                        rx.separator(
                            margin_top="20px",
                            background_color="rgb(145,145,145,0.5)",
                            height="1px"
                        ),
                        #* type_living | meal_plan | description
                        rx.box(
                        rx.tabs.root(
                            rx.tabs.list(
                                rx.tabs.trigger(
                                    rx.text("More",size="6",weight="bold"), 
                                    value="tab1",
                                    color_scheme="yellow",
                                    margin_left="10px",
                                ),
                                rx.tabs.trigger(
                                    rx.text("Decription",size="6",weight="bold"), 
                                    value="tab2",
                                    color_scheme="yellow",
                                ),

                            ),
                            rx.tabs.content(
                                rx.box(
                                rx.flex(
                                
                                #type_living
                                rx.box(
                                    colored_card(
                                        icon="bed",
                                        text=f"\n{TourDetailState.tour.type_living}\n",
                                        bgcolor="#dffbf2",
                                        icon_color="#32edaf",
                                        id_box="sales-id",
                                        url="#",
                                        width="100%",

                                        # height= "140px",
                                         
                                    ),
                                    width="40%",
                                    
                                ),
                                # meal_plan
                                rx.box(
                                    colored_card(
                                        icon="cooking-pot",
                                        text=rx.box(
                                            rx.foreach(
                                                TourDetailState.tour.meal_plan,
                                                lambda meal: rx.text(meal, margin_bottom="0.5em")
                                            ),
                                        ),
                                        bgcolor="#fef2ed",
                                        icon_color="#fd714c",
                                        id_box="sales-id",
                                        url="#",
                                        width="100%",
                                        height= "140px",
                                        
                                    ),
                                    # background_color="#fef2ed",
                                    width="100%",
                                    
                                ),

                            gap="10px",
                            justify="between",
                            margin_top="20px",
                            width="100%",
                            # flex tab1
                            ),
                                ),
                                value="tab1",
                            
                            # tab content tab1
                            ),
                            
                            rx.tabs.content(
                                # description
                                rx.box(
                                    rx.scroll_area(
                                        rx.text(f"{TourDetailState.tour.description}"),
                                        type="always",
                                        scrollbars="vertical",
                                    ),
                                    margin_top="20px",
                                    height="167px",
                                ),
                                
                                value="tab2",
                            # tab content tab1
                            ),
                        
                            margin_top="10px",
                            default_value="tab1",
                            style={
                                ".rt-BaseTabList": {
                                    "justify_content": "center",
                                    "box-shadow": "none",
                                }
                            }
                        # tab root 
                        ),
                        # box tab.root
                        ),
                        # book tour button
                        rx.button(
                            rx.text("Book tour",size="5",weight="bold"),
                            style={
                                "position": "fixed",
                                "bottom": "20px",
                                "left": "50%",
                                "width": "80%", 
                                "max-width": "500px",
                                "transform": "translateX(-50%)",
                                "margin": "0 auto",
                                "padding": "1.5em",
                                "border-radius": "30px",
                                "background-color": LAZURE,
                            }
                        )
                    ),
                    
                    error_404()
                ),
                on_mount=TourDetailState.get_tour_details
            )
        # container
        ),
    )