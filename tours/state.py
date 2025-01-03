import reflex as rx


class UserData(rx.State):
    username: str = rx.LocalStorage(name="username")
    mail: str = rx.LocalStorage(name="mail")

    def set_user_data(self, username: str, mail: str):
        self.username = username
        self.mail = mail
        
    def login(self):
        print(f"User:{self.username} logged in")