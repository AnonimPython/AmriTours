import reflex as rx
# from ..database import RegisterUser

from ..state import UserData


# color pallete states
GRAY = "#daecf2"
RED = "#ff414d"
LAZURE = "#19a6b6"
DARK_LAZURE = "#012d40"


      
class Login(UserData):
    form_data: dict = {}
    
    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle form submission and save to localStorage"""
        self.form_data = form_data
        
        # Get values from form
        mail = form_data["mail"]
        username = form_data["username"]
        
        # Save to localStorage through parent class method
        self.set_user_data(username=username, mail=mail)
        




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
                            # ! TEST
                            rx.input(
                                rx.input.slot(
                                    rx.icon(tag="lock"),
                                ),
                                name="username",
                                placeholder="usernameTEST",
                                radius="large",
                                style={"width":"300px","height":"50px","--text-field-focus-color":DARK_LAZURE},
                            ),
                            # !!!!
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