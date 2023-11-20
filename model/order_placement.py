from PyQt5.QtWidgets import QMainWindow
from design.layouts.order_placement_layout import Ui_OrderPlacement
from loader import db, cart
from .helper import show_error_message, show_success_message
import re


EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
PHONE_REGEX = re.compile(r"^\+?\d{1,4}[\s\-]?\(?\d{1,3}?\)?[\s\-]?\d{1,4}[\s\-]?\d{1,4}[\s\-]?\d{1,4}$")


class OrderPlacement(QMainWindow, Ui_OrderPlacement):

    def __init__(self, *args, main_window=None, current_user_id=-1):
        super(OrderPlacement, self).__init__(*args)
        self.setupUi(self)

        self.main_window = main_window
        self.current_user_id = current_user_id
        self.price = 0

        self.confirmOrderButton.clicked.connect(self.confirm_order)
        self.cancelButton.clicked.connect(self.cancel_order)

    def set_total_price(self, price):
        self.price = price

    def set_user_id(self, user_id):
        self.current_user_id = user_id

    def get_address(self):
        return self.addressLineEdit.text().strip()

    def get_email(self):
        email = self.emailLineEdit.text().strip()
        return email if EMAIL_REGEX.match(email) else None

    def get_phone(self):
        phone = self.phoneLineEdit.text().strip()
        return phone if PHONE_REGEX.match(phone) else None

    def confirm_order(self):
        address = self.get_address()
        email = self.get_email()
        phone = self.get_phone()
        is_checked = self.termsCheckBox.isChecked()

        if not address:
            show_error_message("Пожалуйста, введите правильное имя.")
            return

        if not email:
            show_error_message("Пожалуйста, введите действительный адрес электронной почты.")
            return

        if not phone:
            show_error_message("Пожалуйста, введите действительный номер телефона.")
            return

        if not is_checked:
            show_error_message("Пожалуйста, согласитесь с условиями.")
            return

        order_id = db.add_order(self.current_user_id, self.price, address, email, phone, self.paymentComboBox.currentIndex())
        for clothes in cart.get_clothes():
            db.add_order_item(order_id, clothes[0], clothes[1])

        show_success_message("Ваш заказ успешно принят!")
        cart.clear_cart()
        self.clear_fields()
        self.main_window.mainMenu.clear_products()
        self.main_window.mainMenu.load_clothes()
        self.main_window.stacked_widget.setCurrentWidget(self.main_window.mainMenu)

    def cancel_order(self):
        if self.main_window is not None:
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.cart)

    def clear_fields(self):
        self.addressLineEdit.clear()
        self.emailLineEdit.clear()
        self.phoneLineEdit.clear()

        self.termsCheckBox.setChecked(False)

        self.set_total_price(0)
        self.set_user_id(-1)

        self.paymentComboBox.setCurrentIndex(0)
