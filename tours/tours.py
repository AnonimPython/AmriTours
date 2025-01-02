import reflex as rx

import sqlalchemy

from rxconfig import config


#? https://ip-api.com/ for location
# pages
from .pages.tours_list import hello
from .pages.profile import profile
from .pages.hotels import hotels

# state data|variables
from .state import UserData

class Register(UserData):
    form_data: dict = {}
    
    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        
        username = self.form_data["username"]
        mail = self.form_data["mail"]

        

        # in class UserData have 2 variables: username and mail.
        self.username = username
        self.mail = mail

        
        # ?test
        print(form_data)
        print("username", username)

        
class Login(UserData):
    form_data: dict = {}
    
    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        
        mail = self.form_data["mail"]
        # username = self.form_data["username"]
        

        # self.set_user_data(mail)
        
        print(form_data)
        print("mail" , mail)


# color pallete states
GRAY = "#daecf2"
RED = "#ff414d"
LAZURE = "#19a6b6"
DARK_LAZURE = "#012d40"

@rx.page(route="/", title="Index")
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
    
@rx.page(route="/register", title="Register")
def register() -> rx.Component:
    return rx.box(
        rx.mobile_only(
        # register test and image
        rx.box(
            rx.image(
                src="https://img.freepik.com/free-vector/line-luxury-gradient-color-minimalist-style-wave_483537-3948.jpg?t=st=1734395085~exp=1734398685~hmac=6352ea8c1ab42362bf7fbefed7a423141ff35f4a2f3224acb7556ee401add6c4&w=2000",
                height="21vh",
                width="100%",
            ),
            rx.text(
                "Register",
                color="#fff",
                position="absolute",
                top="40px",
                left="34px",
                style={"font-size": "40px","font-weight": "bold"},
            ),
            rx.text(
                "Create your account",
                color=GRAY,
                position="absolute",
                top="113px",
                left="34px"
            ),
            position="relative"
        ),
        # inputs
        rx.box(
            # ! in release change to rx.form()
            rx.form.root(
                   rx.center(
                        rx.vstack(
                            
                            rx.input(
                                rx.input.slot(
                                    rx.icon(tag="user"),
                                ),
                                name="username",
                                placeholder="Username",
                                radius="large",
                                style={"width":"300px","height":"50px","--text-field-focus-color":DARK_LAZURE},
                            ),
                            rx.input(
                                rx.input.slot(
                                    rx.icon(tag="mail"),
                                ),
                                name="mail",
                                placeholder="Mail",
                                radius="large",
                                style={"width":"300px","height":"50px","--text-field-focus-color":DARK_LAZURE},
                            ),
                            rx.input(
                                rx.input.slot(
                                    rx.icon(tag="lock"),
                                ),
                                name="password",
                                placeholder="Password",
                                radius="large",
                                style={"width":"300px","height":"50px","--text-field-focus-color":DARK_LAZURE},
                            ),
                            rx.input(
                                rx.input.slot(
                                    rx.icon(tag="shield-check"),
                                ),
                                name="confirm_password",
                                placeholder="Confirm Password",
                                radius="large",
                                style={"width":"300px","height":"50px","--text-field-focus-color":DARK_LAZURE},
                                border=RED,
                            ),
                            # ! make BD. For test I dont  use it
                            rx.button(
                                rx.text("Register"),
                                type="submit",
                                align_self="center",
                                align_items="center",
                                style={"width":"300px","height":"50px","font-size":"20px"},
                                background_color=LAZURE,
                            ),
                            gap="50px"
                        ),    
                    ),
                    style={"margin-top":"10%"},
                    on_submit=Register.handle_submit,
                ), 
                            
            ),
            
        ),
        rx.center(rx.hstack(rx.text("Have account?",),rx.link("Login", href="/login")),style={"margin-top":"10%"}),
        
    )
    

@rx.page(route="/login", title="Login")
def login() -> rx.Component:
    return rx.box(
        rx.mobile_only(
        # register test and image
        rx.box(
            rx.image(
                src="https://img.freepik.com/free-vector/line-luxury-gradient-color-minimalist-style-wave_483537-3948.jpg?t=st=1734395085~exp=1734398685~hmac=6352ea8c1ab42362bf7fbefed7a423141ff35f4a2f3224acb7556ee401add6c4&w=2000",
                height="21vh",
                width="100%",
            ),
            rx.text(
                "Login",
                color="#fff",
                position="absolute",
                top="40px",
                left="34px",
                style={"font-size": "40px","font-weight": "bold"},
            ),
            rx.text(
                "Sing in to your account",
                color=GRAY,
                position="absolute",
                top="113px",
                left="34px"
            ),
            position="relative"
        ),
        # inputs
        rx.box(
            # ! in release change to rx.form()
            rx.form.root(
                   rx.center(
                        rx.vstack(
                            # mail
                            rx.input(
                                rx.input.slot(
                                    rx.icon(tag="mail"),
                                ),
                                name="mail",
                                placeholder="Mail",
                                radius="large",
                                style={"width":"300px","height":"50px","--text-field-focus-color":DARK_LAZURE},
                            ),
                            rx.input(
                                rx.input.slot(
                                    rx.icon(tag="lock"),
                                ),
                                name="password",
                                placeholder="Password",
                                radius="large",
                                style={"width":"300px","height":"50px","--text-field-focus-color":DARK_LAZURE},
                            ),
                            # ! make BD. For test I dont  use it
                            rx.button(
                                rx.text("Login"),
                                type="submit",
                                align_self="center",
                                align_items="center",
                                style={"width":"300px","height":"50px","font-size":"20px"},
                                background_color=LAZURE,
                            ),
                            gap="50px"
                        ),    
                    ),
                    style={"margin-top":"20%"},
                    on_submit=Login.handle_submit,
                ), 
                            
            ),
            
        ),
        rx.center(rx.hstack(rx.text("Dont have account?",),rx.link("Register", href="/register")),style={"margin-top":"10%"}),
        
    )

@rx.page(route="/tours", title="Tours")
def tours_list() -> rx.Component:
    return hello()

@rx.page(route="/profile", title="Profile")
def profile_page() -> rx.Component:
    return profile()

@rx.page(route="/hotels", title="Hotels")
def hotels_page() -> rx.Component:
    return hotels()


app = rx.App(
    # stylesheets=[ "/style.css", ],
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        # accent_color="teal",
    )
)
# app.add_page(index)
