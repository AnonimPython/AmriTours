 # *topbar 
import reflex as rx


 
# color pallete states
GRAY = "#daecf2"
RED = "#ff414d"
LAZURE = "#19a6b6"
DARK_LAZURE = "#012d40"



def topbar(text: str):
    return rx.box(
        rx.hstack(
            rx.link(
                rx.icon(tag="undo-2",color=DARK_LAZURE),
                href="/tours",
                style={"background":"#f4f3f7","padding":"10px","border-radius":"50%"},
            ),
            rx.text(text,color=DARK_LAZURE,font_size="35px",weight="bold",),
            # rx.link(
            #     rx.icon(tag="user",color=DARK_LAZURE),
            #     href="/tours",
            #     style={"background":"#f4f3f7","padding":"10px","border-radius":"50%"},
            # ),
            
            margin_bottom="25px",
            justify="between",
            align="center",
        ),
    )