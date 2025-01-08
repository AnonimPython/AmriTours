import reflex as rx


from typing import List
from ..database import Tours

#* BACKEND
from ..backend.components.terminal_notofication import terminal_info,terminal_warning




class AddTourState(rx.State):
    # type of living
    select_values: list[str] = [
        "Hotel",
        "Kotage",
        "Villa",
        "Motel",
        "Kamping",
        "Apartments"
    ]
    
    src_img: str
    text: str
    url_tour: str
    price: str
    stars: str
    
    # type of meal
    meal_options: List[str] = [
        "All Inclusive",
        "Breakfast", 
        "Breakfast and Dinner",
        "Breakfast and Lunch",
        "Nothing",
    ]
    selected_meals: List[str] = []

    @rx.event
    def toggle_meal(self, meal: str):
        """Checkbox toggle handler. Need to append or remove List selected_meals"""
        if meal in self.selected_meals:
            self.selected_meals.remove(meal)
            terminal_info(f"[INFO] - Remove meals: {self.selected_meals}")
            
        else:
            self.selected_meals.append(meal)
            terminal_info(f"[INFO] + Selected meals: {self.selected_meals}")
            
    
    @rx.event
    def handle_submit(self, form_data: dict):
        with rx.session() as session:
            new_tour = Tours(
                src_img=form_data["src_img"],
                text=form_data["text"],
                price=form_data["price"],
                stars=form_data["stars"],
                beach=form_data["beach"],
                type_living=form_data["select"],
                meal_plan=self.selected_meals
            )
            session.add(new_tour)
            session.commit()
            # clear list
            self.selected_meals = []
            return [
                rx.toast.success("Success"),
                rx.set_value("src_img", ""),
                rx.set_value("text", ""),
                rx.set_value("price", ""),
                rx.set_value("stars", ""),
            ]

def add_tour():
    return rx.container(
        rx.heading("Add Tour"),
        rx.form(
            rx.vstack(
                rx.input(placeholder="src_img", name="src_img",id="src_img"),
                rx.input(placeholder="text", name="text",id="text"),
                rx.input(placeholder="price", name="price",id="price"),
                rx.input(placeholder="stars", name="stars",id="stars"),
                # beach
                rx.box(
                    rx.checkbox(
                        name="beach",
                        text="Beach near? (3km)",
                    ),
                ),
                # select type of tour
                rx.heading("Select type of tour:"),
                rx.box(
                    rx.select(
                        AddTourState.select_values,
                        name="select",
                        required=True,
                    ),
                ),
                rx.heading("Meal Plans:", size="3"),
                rx.vstack(
                    rx.foreach(
                        AddTourState.meal_options,
                        lambda meal: rx.checkbox(
                            meal,
                            # Use checked instead of value
                            checked=AddTourState.selected_meals.contains(meal),
                            on_change=lambda: AddTourState.toggle_meal(meal)
                        )
                    ),
                    align_items="start",
                    spacing="2",
                    padding="2"
                ),
                rx.button("Add Tour", type="submit"),
                spacing="4",
            ),
            on_submit=AddTourState.handle_submit,
        )
    )