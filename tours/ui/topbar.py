 # *topbar 
import reflex as rx


# color pallete states
GRAY = "#daecf2"
RED = "#ff414d"
LAZURE = "#19a6b6"
DARK_LAZURE = "#012d40"



def topbar(text: str, link: str = "/tours") -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                rx.hstack(
                    rx.link(
                        rx.icon(
                            tag="undo-2",
                            style=rx.color_mode_cond(
                                light={"color":DARK_LAZURE,},
                                dark={"color":GRAY}
                            )
                        ),
                        href=link,
                        style=rx.color_mode_cond(
                            light={"background":GRAY, "padding":"10px", "border-radius":"50%"},
                            dark={"background":"#2d3748", "padding":"10px", "border-radius":"50%"}
                        ),
                    ),
                )
            ),
            rx.color_mode_cond(
                light=rx.text(text, color=DARK_LAZURE, font_size="35px", weight="bold"),
                dark=rx.text(text, color=GRAY, font_size="35px", weight="bold"),
            ),
            margin_bottom="25px",
            justify="between",
            align="center",
        ),
    )
    
def topbar_details(text: str, link: str = "/tours") -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                rx.hstack(
                    rx.link(
                        rx.icon(
                            tag="undo-2",
                            style=rx.color_mode_cond(
                                light={"color":DARK_LAZURE,},
                                dark={"color":GRAY,}
                            )
                        ),
                        href=link,
                        style=rx.color_mode_cond(
                            light={"background":GRAY, "padding":"10px", "border-radius":"50%"},
                            dark={"background":"#2d3748", "padding":"10px", "border-radius":"50%"}
                        ),
                    ),
                    rx.link(
                        rx.icon(
                            tag="hotel",
                            style=rx.color_mode_cond(
                                light={"color":DARK_LAZURE,},
                                dark={"color":GRAY,}
                            )
                        ),
                        href="/hotels",
                        style=rx.color_mode_cond(
                            light={"background":GRAY, "padding":"10px", "border-radius":"50%"},
                            dark={"background":"#2d3748", "padding":"10px", "border-radius":"50%"}
                        ),
                    ),
                ),
                spacing="2",
            ),
            rx.color_mode_cond(
                light=rx.text(text, color=DARK_LAZURE, font_size="35px", weight="bold"),
                dark=rx.text(text, color=GRAY, font_size="35px", weight="bold"),
            ),
            margin_bottom="25px",
            justify="between", 
            align="center",
            padding="10px"
        ),
    )