import reflex as rx

from rxconfig import config


#? https://ip-api.com/ for location
# pages
from .pages.tours_list import tours_list
from .pages.profile import profile
from .pages.hotels import hotels
from .pages.register import register
from .pages.login import login
from .pages.index import index

#backend pages
from .backend.add_tour import add_tour

# state data|variables
from .state import UserData


  
# color pallete states
GRAY = "#daecf2"
RED = "#ff414d"
LAZURE = "#19a6b6"
DARK_LAZURE = "#012d40"

@rx.page(route="/", title="Index")
def index_page() -> rx.Component:
    return index()
    
@rx.page(route="/register", title="Register")
def register_page() -> rx.Component:
    return register()


@rx.page(route="/login", title="Login")
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

@rx.page(route="/add_tour", title="testing_db")
def add_tour_page() -> rx.Component:
    return add_tour()


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
