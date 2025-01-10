import reflex as rx


# color pallete states
GRAY = "#daecf2"
RED = "#ff414d"
LAZURE = "#19a6b6"
DARK_LAZURE = "#012d40"

def index() -> rx.Component:
    return rx.mobile_only(
        # mobile devices 478px
            rx.box(
            rx.flex(
                rx.box(
                    rx.text(
                        "AmriTours",
                        color="#000",
                        position="absolute",
                        top="40px",
                        left="0px",
                        background_color="#ffcb48",
                        style={
                            "font-size": "70px",
                            "font-weight": "bold",
                            "width": "100%",
                            "letter-spacing": "10px",
                            "transform":" rotate(10deg)"
                        },
                    ),
                    width="100%",
                    height="100vh",
                    position="relative",
                    overflow="hidden",
                    
                ),
                # Login and Singin btn
                rx.box(
                    rx.center(
                        rx.vstack(
                            rx.link(
                                rx.button(
                                    "Login",
                                    size="4",
                                    background_color=DARK_LAZURE,
                                    radius="full",
                                    style={
                                        "margin-bottom":"50%",
                                        "padding":"10px 80px",
                                    }
                                ),
                            href="/login",color=GRAY),
                            
                            rx.link(
                                rx.button(
                                    "Register",
                                    size="4",
                                    background_color=DARK_LAZURE,
                                    radius="full",
                                    style={
                                        "margin-bottom":"50%",
                                        "padding":"10px 80px",
                                    }
                                ),
                                href="/register",color=GRAY
                            ),
                            
                            align="center",
                        ),
                    ),
                    style={
                        "margin-top": "40%",
                    },
                ),
                
                spacing="4",
                padding="1em",
                height="100%",
                direction="column",
                justify="between",
                width="100%",
                
                
                
            ),
            
        ),
        style={
            "background-image": "url(https://cs13.pikabu.ru/post_img/big/2019/10/29/10/157236514218472865.jpg)",
            "background-position": "center",
            "background-size": "cover",
            "background-repeat": "no-repeat" 
        },
        position="relative",
        height="100vh",
        width="100%",
    )# index