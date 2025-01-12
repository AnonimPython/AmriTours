import reflex as rx

from ..state import UserData
from sqlmodel import select,or_
from ..database import Tours
from typing import Optional

from ..pages.error import error_404

from ..ui.topbar import topbar

#* BACKEND
from ..backend.components.terminal_notofication import terminal_info,terminal_warning



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
            topbar("Let's go!"),
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
                                        width="100%",
                                        style={"align-self": "center","align-items": "center"}
                                        ),
                                    ),
                                    # stars
                                    rx.box(
                                        rx.hstack(
                                            rx.icon(
                                                tag="star",
                                                color="gold",
                                                size=25,
                                                style={"align-self": "center","align-items": "center"}),
                                            rx.text(f'{TourDetailState.tour.stars}',size="7")
                                        ),
                                        
                                    ),   
                                    justify="between",
                                ),
                                    margin_top="10px",
                                ),
                            margin_top="20px",
                        ),
                        # rx.text(f"Popular: {TourDetailState.tour.popular}"),
                        # rx.text(f"Beach: {TourDetailState.tour.beach}"),
                        rx.text(f"Type living: {TourDetailState.tour.type_living}"),
                        rx.text(f"Meal plan: {TourDetailState.tour.meal_plan}"),
                        rx.text(f"Description: {TourDetailState.tour.description}"),

                    ),
                    error_404()
                ),
                on_mount=TourDetailState.get_tour_details
            )
        # container
        ),
    )