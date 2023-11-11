from PyQt5.QtWidgets import QWidget
from design.layouts.order_card import Ui_OrderCard

# pyuic5 -o .\\design\\layouts\\order_card.py .\\design\\ui\\order_card.ui


class OrderCard(QWidget, Ui_OrderCard):

    def __init__(self, order_id, user_id, payment_type, price, address, email, phone, parent=None, main_window=None, parent_window=None, current_user_id=-1):
        super(OrderCard, self).__init__(parent)
        self.setupUi(self)

        self.main_window = main_window
        self.current_user_id = current_user_id
        self.order_id = order_id
        self.parent_window = parent_window

        self.orderIdLabel.setText(f"ID Заказа: {order_id}")
        self.userIdLabel.setText(f"ID Пользователя: {user_id}")
        self.paymentTypeLabel.setText(f"Способ оплаты: {'Картой' if payment_type == 0 else 'Наличными'}")
        self.priceLabel.setText(f"Стоимость: {price}")
        self.addressLabel.setText(f"Адрес: {address}")
        self.emailLabel.setText(f"Электронная почта: {email}")
        self.phoneLabel.setText(f"Номер телефона: {phone}")

        self.detailsBtn.clicked.connect(self.show_details)

    def show_details(self):
        if self.main_window is not None:
            self.main_window.orderDetailsView.set_order_id(self.order_id)
            self.main_window.orderDetailsView.set_parent_window(self.parent_window)
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.orderDetailsView)

