import reflex as rx

from ..database import Tours

class AddTourState(rx.State):
    src_img: str
    text: str
    url_tour: str
    price: str
    stars: str
    
    @rx.event
    def handle_submit(self, form_data: dict):
        with rx.session() as session:
            new_tour = Tours(
                src_img=form_data["src_img"],
                text=form_data["text"],
                price=form_data["price"],
                stars=form_data["stars"],
            )
            session.add(new_tour)
            session.commit()
            return [
                rx.toast.success("Success"),
                # clear inputs using id in inputs
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
                rx.input(placeholder="src_img", name="src_img",id="src_img",),
                rx.input(placeholder="text", name="text",id="text",),
                rx.input(placeholder="price", name="price",id="price",),
                rx.input(placeholder="stars", name="stars",id="stars",),
                rx.button("Add Tour", type="submit"),
                spacing="4",
            ),
            on_submit=AddTourState.handle_submit,
        )
    )