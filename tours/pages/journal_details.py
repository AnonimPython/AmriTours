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

def journal() -> rx.Component:
    return rx.box(
        rx.mobile_only(
                rx.box(
                    rx.vstack(
                        # back button
                        rx.box(
                            rx.link(
                                rx.icon(
                                    tag="arrow-left",
                                    color="white",
                                    
                                ),
                                href="/tours",
                            ),
                            
                            z_index="2",
                            position="absolute",
                            top="4%",
                            left="30px",
                        ),
                        
                        # main text
                        rx.text(
                            "Cheops pyramids",
                            color="white",
                            font_size="3em",
                            font_weight="bold",
                            text_align="start",
                            width="50%",
                            height="10%",
                            word_spacing="12px",
                            z_index="2",
                            position="absolute",
                            top="238px",
                            left="23px",
                        ),
                        # stars
                        rx.box(
                            rx.hstack(
                                rx.icon(tag="star",color="yellow"),
                                rx.text(
                                    "4.8",
                                    color="#fff",
                                    weight="bold",
                                    size="4",
                                ),
                                
                            ),
                            z_index="2",
                            position="absolute",
                            top="400px",
                            left="23px",
                            margin_bottom="400px"
                        ),
                        # description
                        rx.text(
                            "The Great Pyramid of Giza, also known as the Pyramid of Khufu or Cheops, is one of the most famous and largest pyramids in the world. It was built during the Fourth Dynasty of the Old Kingdom of Ancient Egypt, around 2580–2560 BC, as a tomb for Pharaoh Khufu. The pyramid originally stood at about 146.6 meters (481 feet) tall, making it the tallest man-made structure for over 3,800 years.",
                            color="rgba(255, 255, 255, 0.7)",
                            font_size="1.2em",
                            # text_align="center",
                            z_index="2",
                            position="absolute",
                            top="500px",
                            left="23px",
                        ),
                        rx.box(
                            rx.link(
                                
                            ),
                            z_index="2",
                            position="absolute",
                            top="700px",
                            left="23px",
                            
                        ),
                        align="center",
                        justify="center",
                        height="100vh",
                        spacing="4", 
                    ),
                    # Стили для контейнера с фоном
                    background_image="url(https://cdn.tripster.ru/photos/12d866a3-fdd5-4b7b-9c50-0ce3481d01ef.jpg)",
                    background_size="cover",
                    background_position="center",
                    background_repeat="no-repeat",
                    position="relative",
                    height="100vh",
                    width="100%",
                    _after={
                        "content": '""',
                        "position": "absolute",
                        "top": 0,
                        "left": 0,
                        "width": "100%",
                        "height": "100%",
                        "background": "rgba(0,0,0,0.5)",
                        "z_index": 1
                    }
                ),
            ),
        )
        