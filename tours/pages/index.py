import reflex as rx


# color pallete states
GRAY = "#daecf2"
RED = "#ff414d"
LAZURE = "#19a6b6"
DARK_LAZURE = "#012d40"

def index() -> rx.Component:
    return rx.mobile_only(
        rx.box(
            rx.flex(
                rx.box(
                    # rx.icon(tag="plane",color="white"),
                    rx.text(
                        "AmriTours",
                        color="#fff",
                        position="absolute", 
                        top="20px",
                        left="0px",
                        style={
                            "font-size": "50px",
                            "font-weight": "bold",
                            "width": "100%",
                            "text-align": "center",
                        },
                    ),
                    # height="100vh",
                    position="relative",
                    width="100%",
                ),
                # Login and Register buttons 
                rx.box(
                    rx.center(
                        rx.vstack(
                            rx.box(
                                rx.text(
                                    "Travel your dream place",
                                    color="#fff",
                                    weight="bold",
                                    size="5",
                                    text_align="center",
                                    margin_bottom="10px",
                                ),
                                rx.text(
                                    "We are the best raited travel agency of 2025 in the world!",
                                    color="rgb(255,255,255,0.6)",
                                    weight="bold",
                                    size="2",
                                    text_align="center",
                                    padding="20px 60px",
                                ),
                            ),
                            rx.link(
                                rx.button(
                                    rx.text("Get started",weight="bold",),
                                    size="4", 
                                    color="#5f3500",
                                    background_color="#fdc509",
                                    radius="full",
                                    width="290px",
                                ),
                                href="/login",
                                color=GRAY
                            ),
                            rx.hstack(
                                rx.text("Dont have an account?",color="#fff"),
                                rx.link(
                                    "Sing up",
                                    href="/register",
                                    color="#fdc509",
                                    style={"text-decoration": "underline"},
                                ),
                            ),
                            
                            spacing="4",
                            align="center",
                        ),
                    ),
                    position="absolute",
                    top="80%",
                    left="50%",
                    transform="translate(-50%, -50%)",
                    padding="15px",
                    width="400px",
                    margin_left="0px",
                    margin_top="0px",
                    background_color="rgb(45,40,38,0.9)",
                    border_radius="15px",
                ),
                spacing="4",
                padding="1em", 
                # height="100vh", 
                direction="column",
                justify="between",
                width="100%",
            ),
            style={
                "background-image": "url(https://i.pinimg.com/originals/0a/db/29/0adb29a661d427e9a1146a8eff872f1f.jpg)",
                "background-position": "center",
                "background-size": "cover", 
                "background-repeat": "no-repeat",
                "min-height": "100vh",
                "margin": "0",         
                "padding": "0"         
            },
            position="relative",
            height="100vh",
            width="100%",
            margin="0px",
            padding="0px" 
        ),
        width="100%",    
        height="100vh", 
        margin="0px",   
        padding="0px"    
    )