import reflex as rx
from typing import Optional
from sqlmodel import Field
# reflex db makemigrations && reflex db migrate
#* REGISTER
class RegisterUser(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(min_length=3, max_length=50)
    mail: str
    password: str
    confirm_password: str
    
#* TOURS
class Tours(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    src_img: str = Field(default="")
    text: str = Field(default="")
    url_tour: str = Field(default="")
    price: int = Field(default=0)
    stars: int = Field(default=0)
    popular: bool = Field(default=False)
    # ! need add checkbox for "Sales" and after tap on , adding new fields to add fresh price
    
    
#* AD CARD


#* PLANE TIKETS


#* JOURNAL



#* ATTRACTIONS


