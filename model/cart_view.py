from PyQt5.QtWidgets import *
from loader import db, cart
from model.clothes_card import ClothesCard
from design.layouts.cart_layout import Ui_CothesStoreCart
from .helper import show_error_message


class Cart(QMainWindow, Ui_CothesStoreCart):

    def __init__(self, *args, main_window=None, current_user_id=-1):
        super(Cart, self).__init__(*args)
        self.setupUi(self)

        self.main_window = main_window
        self.current_user_id = current_user_id
        self.price = 0

        cart.addOnAddCallback(self.on_add_remove_clothes)
        cart.addOnRemoveCallback(self.on_add_remove_clothes)
        cart.addOnUpdateCallback(self.update_clothes_count)

        self.backBtn.clicked.connect(self.go_back)
        self.orderBtn.clicked.connect(self.go_order_placement)

    def load_cart(self):
        self.clear_products()

        clothes_cards = []

        for _clothes in cart.get_clothes():
            clothes = self.get_clothes_by_id(_clothes[0])
            clothes_card = ClothesCard(
                clothes[0], clothes[2], clothes[3], self.get_category_name(clothes[1]),
                clothes[4], clothes[5], clothes[7], clothes[6], main_window=self.main_window, parent_window=self
            )
            clothes_card.set_count(_clothes[1])
            clothes_cards.append(clothes_card)
            self.clothesList.addWidget(clothes_card)

        ClothesCard.check_clothes(clothes_cards)

    @staticmethod
    def get_clothes_by_id(clothes_id):
        return db.get_clothes_by_id(clothes_id)

    @staticmethod
    def get_category_name(category_id):
        return db.get_category_name(category_id)

    def clear_products(self):
        layout = self.clothesList.layout()
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def go_back(self):
        if self.main_window:
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.mainMenu)

    def on_add_remove_clothes(self, *args):
        self.clear_products()
        self.load_cart()
        self.calculate_total_price()

    def calculate_total_price(self, *args):
        price = 0
        for clothes in cart.get_clothes():
            price += self.get_clothes_by_id(clothes[0])[6] * clothes[1]
        self.price = price
        self.totalPrice.setText(f"Общая стоимость: {price} ₽")

    def update_clothes_count(self, clothes_id, clothes_count):
        layout = self.clothesList.layout()
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget and isinstance(widget, ClothesCard) and (widget.clothes_id == clothes_id or clothes_id == -1):
                widget.set_count(clothes_count)
        self.calculate_total_price()

    def set_user_id(self, user_id):
        self.current_user_id = user_id

    def go_order_placement(self):
        if not cart.get_clothes():
            show_error_message("Для оформления заказа нужно добавить желаемые товары в корзину.")
            return
        if self.main_window:
            self.main_window.order_placement.set_total_price(self.price)
            self.main_window.order_placement.set_user_id(self.current_user_id)
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.order_placement)
