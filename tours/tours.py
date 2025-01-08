import reflex as rx

from rxconfig import config


#? https://ip-api.com/ for location
# frontend pages
from .pages.tours_list import tours_list
from .pages.tour_details import tour_detail
from .pages.profile import profile
from .pages.hotels import hotels
from .pages.register import register
from .pages.login import login
from .pages.index import index

#backend pages
from .backend.add_tour import add_tour

# state data|DB data
from .state import UserData
            
  
# color pallete states
GRAY = "#daecf2"
RED = "#ff414d"
LAZURE = "#19a6b6"
DARK_LAZURE = "#012d40"
#*                               in state.py fuction check LocalStorage, if is null -> redirect to register page
@rx.page(route="/", title="Index", on_load=UserData.check_auth)
def index_page() -> rx.Component:
    return index()
    
@rx.page(route="/register", title="Register", on_load=UserData.check_auth)
def register_page() -> rx.Component:
    return register()

# ! for test LocalStorage filling username and mail
@rx.page(route="/login", title="Login", on_load=UserData.check_auth)
def login_page() -> rx.Component:
    return login()

@rx.page(route="/tours", title="Tours")
def tours_page() -> rx.Component:
    return tours_list()

@rx.page(route="/profile", title="Profile")
def profile_page() -> rx.Component:
    return profile()

@rx.page(route="/hotels", title="Hotels")
def hotels_page() -> rx.Component:
    return hotels()

@rx.page(route="/add_tour", title="add_tour")
def add_tour_page() -> rx.Component:
    return add_tour()


@rx.page(route="/tours/[id]")
def tour_detail_page():
    return tour_detail()


# def api_test(item_id: int):
#     return {"my_result": item_id}
# app.api.add_api_route("/items/{item_id}", api_test)


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
# app.add_page(tour_detail)
