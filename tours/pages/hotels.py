import reflex as rx
from rxconfig import config

from ..state import UserData

from ..ui.topbar import topbar

from .tours_list import tour_card          

from sqlmodel import select,or_
from ..database import Tours


#* BACKEND
from ..backend.components.terminal_notofication import terminal_info,terminal_warning  






# color pallete states
GRAY = "#daecf2"
RED = "#ff414d"
LAZURE = "#19a6b6"
DARK_LAZURE = "#012d40"


class ToursDBState(rx.State):
    # Определяем переменную состояния для хранения списка туров
    tours: list[Tours] = []
    is_loading: bool = False


    @rx.event
    def get_regular_tours(self) -> list[Tours]:
        try:
            with rx.session() as session:
                query = select(Tours)
                self.tours = session.exec(query).all()
        except Exception as e:
            terminal_warning(f"[WARNING] Error getting tours from BD (get_regular_tours): {e}")
        # test
        terminal_info(f"INFO] SQL Query: {query}")  # Выводим SQL запрос
        terminal_info(f"[INFO] All Data: {self.tours}")  # Выводим полученные данные



class SelectCountry(rx.State):
    values: list[str] = [
        "United States",
        "Canada",
        "Mexico",
        "Brazil",
        "Argentina",
        "United Kingdom",
        "Germany",
        "France",
        "Italy",
        "Spain",
        "Russia",
        "China",
        "India",
        "Japan",
        "Australia",
        "South Africa"
    ]
    value: str = ""

    @rx.event
    def change_value(self, value: str):
        """Change the select value var."""
        self.value = value
        print("Change value", self.value)



class RangeSliderState(rx.State):
    value_start: int = 25
    value_end: int = 75

    @rx.event
    def set_end(self, value: list[int]):
        self.value_start = value[0]
        self.value_end = value[1]
    
    @rx.event
    def set_start_value(self, value: str):
        # Convert string to int and validate
        if value.isdigit():
            new_value = min(max(int(value), 0), 10000)
            self.value_start = new_value
    
    @rx.event
    def set_end_value(self, value: str):
        # Convert string to int and validate
        if value.isdigit():
            new_value = min(max(int(value), 0), 10000)
            self.value_end = new_value

class TypeOfHotel(rx.State):
    # Используем словарь для хранения состояния каждого чекбокса
    choices: dict[str, bool] = {
        k: False
        for k in [
            "Hotel",
            "Kotage",
            "Villa",
            "Motel",
            "Kamping",
            "Apartments"
        ] 
    }

    def check_choice(self, value, index):
        self.choices[index] = value
        print("Choice:", value, "at index", index,)
              
class Stars(rx.State):
    # Используем словарь для хранения состояния каждого чекбокса
    choices: dict[str, bool] = {
        k: False
        for k in [
            "5*",
            "4*",
            "3*",
            "2*",
            "1*",
        ] 
    }

    def check_choice(self, value, index):
        self.choices[index] = value
        print("Choice:", value, "at index", index,)

class MealPlan(rx.State):
    # Используем словарь для хранения состояния каждого чекбокса
    choices: dict[str, bool] = {
        k: False
        for k in [
            "All Inclusive",
            "Breakfast",
            "Breakfast and Dinner",
            "Breakfast and Lunch",
            "Nothing",
        ] 
    }

    def check_choice(self, value, index):
        self.choices[index] = value
        print("Choice:", value, "at index", index,)
        
        
def hotels() -> rx.Component:
    return rx.box(
        rx.mobile_only(
            rx.container(
                
                topbar("Tours"),
                
                # filter
                rx.box(
                    rx.alert_dialog.root(
                    rx.alert_dialog.trigger(
                        rx.button("Filter",background=LAZURE),
                    ),
                    rx.alert_dialog.content(
                        rx.alert_dialog.title("All Filter"),
                        rx.alert_dialog.description(
                            rx.vstack(
                                # Dropdown menu
                                #* country   
                                rx.box(
                                    rx.box(
                                        rx.hstack(
                                        rx.heading(f"Country:"),
                                        rx.select(
                                            SelectCountry.values,
                                            value=SelectCountry.value,
                                            on_change=SelectCountry.change_value,
                                        ),
                                        

                                        ),
                                    ),
                                    margin="10px",
                                ),                       
                                #* price
                                rx.box(
                                    rx.heading("Price"),
                                    rx.hstack(
                                        rx.vstack(
                                        rx.hstack(
                                            rx.heading("From:", size="5"),
                                            rx.heading(RangeSliderState.value_start, "$", size="5"),
                                        ),
                                        rx.input(
                                            value=RangeSliderState.value_start,
                                            on_change=RangeSliderState.set_start_value,
                                            type_="number",
                                            min_=0,
                                            max=10000,
                                            margin_bottom="5px",
                                            width="70px",
                                        ),
                                    ),
                                    rx.vstack(
                                        rx.hstack(
                                            rx.heading("By:", size="5"),
                                            rx.heading(RangeSliderState.value_end, "$", size="5"),
                                        ),
                                        rx.input(
                                            value=RangeSliderState.value_end,
                                            on_change=RangeSliderState.set_end_value,
                                            type_="number",
                                            min_=0,
                                            max=1000,
                                            width="70px",
                                        ),
                                        margin_bottom="15px",
                                    ),
                                        justify="between",
                                    ),
                                    
                                    rx.slider(
                                        default_value=[RangeSliderState.value_start, RangeSliderState.value_end],
                                        min_=0,
                                        max=4000,
                                        on_value_commit=RangeSliderState.set_end,
                                        style={
                                                "& .rt-SliderRange": {
                                                    "background": LAZURE
                                                }
                                            }
                                        ),
                                    width="100%",
                                    margin="10px",
                                    
                                ),
                                #* type hotel
                                rx.box(
                                    rx.heading("Type",margin_bottom="10px"),
                                    
                                    rx.flex(
                                        rx.foreach(
                                        TypeOfHotel.choices,
                                        lambda choice: rx.checkbox(
                                            choice[0],
                                            checked=choice[1],
                                            on_change=lambda val: TypeOfHotel.check_choice(val, choice[0])
                                        ),
                                    ),
                                        width="100%",
                                        flex_wrap="wrap",
                                        spacing="2",
                                    ),
                                    margin="10px",
                                ),
                                #* stars
                                rx.box(
                                    rx.heading("Stars",margin_bottom="10px"),
                                    rx.flex(
                                        rx.foreach(
                                        Stars.choices,
                                        lambda choice: rx.checkbox(
                                            choice[0],
                                            checked=choice[1],
                                            on_change=lambda val: Stars.check_choice(val, choice[0])
                                        ),
                                    ),
                                        width="100%",
                                        flex_wrap="wrap",
                                        spacing="2",
                                    ),
                                    
                                    
                                    margin="10px",
                                ),
                                #* meal plan
                                rx.box(
                                    rx.heading("Meal Plan",margin_bottom="10px"),
                                    rx.flex(
                                        rx.foreach(
                                        MealPlan.choices,
                                        lambda choice: rx.checkbox(
                                            choice[0],
                                            checked=choice[1],
                                            on_change=lambda val: MealPlan.check_choice(val, choice[0])
                                        ),
                                    ),
                                        width="100%",
                                        flex_wrap="wrap",
                                        spacing="2",
                                    ),
                                    
                                    
                                    margin="10px",
                                ),
                            )
                        ),
                        # ! make position fixed
                        rx.flex(
                            rx.alert_dialog.cancel(
                                rx.button("Cancel",background=RED,radius="full",variant="soft",color="white"),
                            ),
                            rx.alert_dialog.action(
                                rx.button("Access",variant="soft",color_scheme="green",radius="full"),
                            ),
                            spacing="3",
                            justify="end",  # Right align the buttons
                            margin_top="16px",
                        ),
                    ),
                )
                )
                   
                   
                   
                   
                   
                ),
                # list of  tours
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
                
                
                # navbar(),
            
                margin="10px"
            ),
            
            
        )
        
