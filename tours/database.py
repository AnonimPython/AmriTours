import reflex as rx
from typing import Optional, List
from sqlmodel import Field
from sqlalchemy import JSON, Column
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
    country: str = Field(default="")
    description: str = Field(default="")
    days: str = Field(default="")
    time: str = Field(default="")
    address: str = Field(default="")
    price: int = Field(default=0)
    stars: int = Field(default=0)
    popular: bool = Field(default=False)
    beach: bool = Field(default=False)
    type_living: str = Field(default="")
    meal_plan: List[str] = Field(
        default=[],
        sa_column=Column(JSON)
    )
    
    @property
    def url_tour(self) -> str:
        return f"/tour/{self.id}"
    # ! need add checkbox for "Sales" and after tap on , adding new fields to add fresh price

#* TICKETS SUPPORT
class Tickets(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str = Field(default="")
    
#* AD CARD


#* PLANE TIKETS


#* JOURNAL



#* ATTRACTIONS


