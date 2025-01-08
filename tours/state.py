import reflex as rx

class UserData(rx.State):
    username: str = rx.LocalStorage(name="username")
    mail: str = rx.LocalStorage(name="mail")

    #* check if user is authenticated
    @rx.var
    def is_authenticated(self) -> bool:
        return bool(self.username and self.mail)

    #* redirect to register page if user is not authenticated
    @rx.event
    def check_auth(self):
        if not self.is_authenticated:
            return rx.redirect("/register")
        return rx.redirect("/tours")

    #* set user data for another files
    def set_user_data(self, username: str, mail: str):
        self.username = username
        self.mail = mail
    
    # ! test LocalStorage
    def login(self):
        print(f"User:{self.username} logged in")