 # *navbar
import reflex as rx


 
# color pallete states
GRAY = "#daecf2"
RED = "#ff414d"
LAZURE = "#19a6b6"
DARK_LAZURE = "#012d40"


def navbar_link(icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.icon(icon),
        href=url, 
        color=DARK_LAZURE,
        style={"background-color":"white", "border-radius":"50%","padding":"10px"}
    )


def navbar():
    return rx.box(
        rx.hstack(
            navbar_link("layout-grid", "/tours"),
            navbar_link("tram-front", "/tours"),
            # ! make real profile use DB. For test I make 1 user
            navbar_link("user", "/profile"),
            # navbar_link("About", "/#"),
            # navbar_link("Pricing", "/#"),
            # navbar_link("Contact", "/#"),
            spacing="9",
            width="100%",

            style={
                "align-items":"center",
                "align-items":"center",
                "justify-content":"center",
                "align-self":"center",
                "padding":"13px",
                
            },
        ),
        position="fixed",
        top="90%",
        left="5%",
        style={
            "width":"90%",
            "height":"70px",
            "align-items":"center",
            "justify-content":"center",
            "align-self":"center",
            "border-radius":"30px",
        },
        
        background_color=GRAY,
    ),