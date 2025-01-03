import reflex as rx
from ..database import RegisterUser



# color pallete states
GRAY = "#daecf2"
RED = "#ff414d"
LAZURE = "#19a6b6"
DARK_LAZURE = "#012d40"


class Register(rx.State):
    username: str = ""
    mail: str = ""
    password: str = ""
    confirm_password: str = ""

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        try:
            # Basic validation
            if form_data["password"] != form_data["confirm_password"]:
                return [
                    rx.set_value("password", ""),  # Clear password field
                    rx.set_value("confirm_password", ""),  # Clear confirm field
                    rx.toast.error("Passwords do not match")
                ]
            
            # Create new user
            with rx.session() as session:
                new_user = RegisterUser(
                    username=form_data["username"],
                    mail=form_data["mail"],
                    password=form_data["password"],  # In production, hash this!
                    confirm_password=form_data["confirm_password"]
                )
                session.add(new_user)
                session.commit()
                
            # Clear form and redirect
            return rx.redirect("/login")
            
        except Exception as e:
            return rx.toast.error(str(e))
        
        
        
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
                                id="password",
                                placeholder="Password",
                                radius="large",
                                style={"width":"300px","height":"50px","--text-field-focus-color":DARK_LAZURE},
                            ),
                            rx.input(
                                rx.input.slot(
                                    rx.icon(tag="shield-check"),
                                ),
                                name="confirm_password",
                                id="confirm_password",
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
    
