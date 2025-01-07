import reflex as rx

from ..state import UserData
from sqlmodel import select,or_
from ..database import Tours
from typing import Optional

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
            terminal_info("(get_tour_details)==================")
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
    return rx.container(
            rx.vstack(
            rx.cond(
                TourDetailState.tour,
                rx.vstack(
                    rx.image(src=TourDetailState.tour.src_img),
                    rx.heading(TourDetailState.tour.text),
                    rx.text(f"Price: ${TourDetailState.tour.price}"),
                    rx.text(f"Rating: {TourDetailState.tour.stars}")
                ),
                rx.text("Tour not found")
            ),
            on_mount=TourDetailState.get_tour_details
        )
    ),