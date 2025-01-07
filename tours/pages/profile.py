import reflex as rx

from rxconfig import config


from ..ui.topbar import topbar


from ..state import UserData

from reflex.style import set_color_mode, color_mode
from sqlmodel import select,or_
from ..database import Tickets


#* BACKEND
from ..backend.components.terminal_notofication import terminal_info,terminal_warning



class State(rx.State):
    pass
            
# class UserName(UserData):
#     def login(self):
#         print(f"User info - Name: {UserData.username}, Age: {UserData.mail}")

#pragma mark - 123

class SendSupport(rx.State):
    form_data: dict
    
    
    
    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data["support_message"]
        
        if not self.form_data == "":
            terminal_info(f"[INFO] Support message: {self.form_data}")
            # connect DB
            try:
                with rx.session() as session:
                    new_ticket = Tickets(
                        # user_id=UserData.id,
                        text=self.form_data,
                    )
                    session.add(new_ticket)
                    session.commit()
                    session.refresh(new_ticket)
                    terminal_info(f"[INFO] Ticket added to DB")
            except Exception as e:
                terminal_warning(f"[WARNING] Error getting tickets from BD (SendSupport): {e}")
                
            return rx.toast.success(f"Your support message has been submitted")
            
        else:
            terminal_warning(f"[WARNING] Error adding ticket to DB (SendSupport): {e}")
            return rx.toast.warning(f"Support massage is empty or invalid")


class ChangeTheme(rx.State):
    is_dark: bool = False

    def toggle_theme(self):
        self.is_dark = not self.is_dark


class FormState(rx.State):
    form_data: dict = {}
    current_field: str = ""  #? To track which field is being edited
    
    @rx.event
    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        field_value = form_data.get("new_value", "")
        
        if self.current_field == "mail_field":
            terminal_info(text=f"[INFO] Email changed to: {field_value}")
            return rx.toast(f"Email changed to: {field_value}")
        elif self.current_field == "name_field":
            print(f"[INFO] Name changed to: {field_value}")
            return rx.toast(f"Name changed to: {field_value}")
    
    #* taking from field this name and set variable current_field = name of field
    @rx.event
    def set_current_field(self, field: str):
        self.current_field = field

def edit_field_dialog(title: str, description: str, field_value: str, field_type: str) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button(
                f"Change {title}",
                weight="bold", 
                font_size="20px",
                width="100%",
                background=LAZURE,
                #* in class FormState we have a function set_current_field
                #* this function take name of field and set in class current_field = name of field
                #? if field name are "name" -> FormState.set_current_field("name")
                #? def set_current_field(self, field: str): self.current_field = "name"
                on_click=FormState.set_current_field(field_type)  # Set field type when button clicked
            ),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(f"Change {title}"),
            rx.alert_dialog.description(
                f"Enter your new {description}:",
            ),
            # ! in realise change to rx.form
            rx.form.root(
                rx.flex(
                    rx.input(
                        placeholder=field_value,
                        size="3",
                        name="new_value"
                    ),
                    rx.alert_dialog.cancel(
                        rx.button(
                            "Cancel",
                            variant="soft",
                            background=RED,
                            radius="full", 
                            color="white"
                        ),
                    ),
                    rx.alert_dialog.action(
                        rx.button(
                            "Save",
                            color_scheme="green",
                            radius="full",
                            type="submit"
                        ),
                    ),
                    direction="column",
                    spacing="3",
                ),
                on_submit=FormState.handle_submit,
            ),
        ),
    )

# color pallete states
GRAY = "#daecf2"
RED = "#ff414d"
LAZURE = "#19a6b6"
DARK_LAZURE = "#012d40"

def segment(text: str) -> rx.Component:
    return rx.box(
        rx.text(text, weight="bold", font_size="20px"),
        rx.separator(margin="5px"),
        
        margin_top="15px",
        margin_bottom="15px",
    )
    

def profile() -> rx.Component:
    
    return rx.box(
        rx.mobile_only(
            rx.container(
                topbar("Profile"),
                # header
                rx.box(
                    rx.text(f"{UserData.username}", weight="bold", font_size="20px"),
                    rx.text(f"{UserData.mail}"),
                    align="center",
                    text_align="center",
                    margin_bottom="20px",
                ),
                # settings
                rx.box(
                    segment("Settings"),
                    rx.box(
                        rx.flex(
                            rx.text("Theme", weight="bold", font_size="20px"),
                            rx.box(
                                rx.segmented_control.root(
                            rx.segmented_control.item(
                                rx.icon(tag="monitor", size=20),
                                value="system",
                            ),
                            rx.segmented_control.item(
                                rx.icon(tag="sun", size=20),
                                value="light",
                            ),
                            rx.segmented_control.item(
                                rx.icon(tag="moon", size=20),
                                value="dark",
                            ),
                            on_change=set_color_mode,
                            variant="classic",
                            radius="large",
                            value=color_mode,
                        )
                                
                            ),
                            # rx.color_mode.button(style={"width": "70px"}),
                            
                            justify="between",
                        ),
                        margin_bottom="20px",
                        
                    ),
                    rx.flex(
                        rx.box(
                            edit_field_dialog(
                                title="Name",
                                description="name", 
                                field_value=UserData.username,
                                field_type="name_field"
                                
                            ),
                            width="50%",
                        ),
                        rx.box(
                            edit_field_dialog(
                                title="Mail",
                                description="email",
                                field_value=UserData.mail,
                                field_type="mail_field",
                            ),
                            margin_left="20px",
                            width="50%",
                        ),
                        justify="center",
                        # flex| change name and mail
                    ),
                   
                # box| settings
                ),
                
                # support
                rx.box(
                    segment("Support"),
                    rx.box(
                        rx.alert_dialog.root(
                    rx.alert_dialog.trigger(
                        rx.button(
                            f"Send message", 
                            weight="bold",
                            font_size="20px",
                            width="100%",
                            background=LAZURE
                        ),
                    ),
                    rx.alert_dialog.content(
                        rx.alert_dialog.title(f"Whats Wrong?"),
                        rx.alert_dialog.description(
                            f"Enter your new massage:",
                        ),
                        rx.form.root(
                            rx.flex(
                                rx.form.field(
                                    rx.text_area(
                                        placeholder="Type here...",
                                        name="support_message"
                                    ),
                                ),
                                rx.alert_dialog.cancel(
                                    rx.button(
                                        "Cancel",
                                        variant="soft", 
                                        background=RED,
                                        radius="full",
                                        color="white"
                                    ),
                                ),
                                rx.alert_dialog.action(
                                    rx.form.submit(
                                        rx.button(
                                            "Send",
                                            color_scheme="green",
                                            radius="full",
                                            width="100%",
                                        ),
                                    ),
                                ),
                                direction="column",
                                spacing="3",
                            ),
                            on_submit=SendSupport.handle_submit,
                        ),
                    ),
                    # box| alert_dialog
                    ),
                
                ),
                # box| support
                ),
                

            # container
            ),
             
            
            
        ),
        
    )
        