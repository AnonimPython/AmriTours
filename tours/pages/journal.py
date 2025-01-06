import reflex as rx

from rxconfig import config
from ..ui.navbar import navbar

from ..state import UserData


class State(rx.State):
    pass
            
# class UserName(UserData):
#     def login(self):
#         print(f"User info - Name: {UserData.username}, Age: {UserData.mail}")




# color pallete states
GRAY = "#daecf2"
RED = "#ff414d"
LAZURE = "#19a6b6"
DARK_LAZURE = "#012d40"

def profile() -> rx.Component:
    
    return rx.box(
        rx.mobile_only(
            rx.box(
                rx.text(f"Hello Journal{UserData.username}"),
                rx.text(f"Hello {UserData.mail}"),
                
                
            ),
            # navbar(),
            
        ),
        
    )
        