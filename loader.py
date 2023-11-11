from database.database import Database
from model.cart import Cart

db = Database(".\\data\\database.db")

default_image = db.convert_to_binary_data(".\\images\\default.jpg")

cart = Cart()
