import reflex as rx


# color pallete states
GRAY = "#daecf2"
RED = "#ff414d"
LAZURE = "#19a6b6"
DARK_LAZURE = "#012d40"

def index() -> rx.Component:
    return rx.container(
        # mobile devices 478px
            rx.mobile_only(
            rx.flex(
                rx.box(
                    rx.text(
                        "Welcome",
                        align="center",
                        as_="div",
                        size="7",
                        color=GRAY,
                    ),
                ),
                rx.box(
                    rx.text(
                        "AmricaTours",
                        align="center",
                        as_="div",
                        size="9",
                        weight="bold",
                        color=GRAY,
                        
                    ),
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
        background_color=LAZURE,
        height="100vh",
    )# index