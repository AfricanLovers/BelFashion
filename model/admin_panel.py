from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMainWindow
from loader import db
from model.clothes_card import ClothesCard
from model.order_card import OrderCard
from design.layouts.admin_layout import Ui_AdminPanel
from .helper import show_question_message


class AdminPanel(QMainWindow, Ui_AdminPanel):
    def __init__(self, *args, main_window=None, current_user_id=-1):
        super().__init__(*args)
        self.setupUi(self)

        self.main_window = main_window
        self.current_user_id = current_user_id

        self.setupUI()

    def setupUI(self):
        self.load_clothes()
        self.load_orders()

        self.searchBar.textChanged.connect(self.search_clothes)
        self.orderSearchBar.textChanged.connect(self.search_orders)
        self.orderSearchBar.setValidator(QIntValidator())
        self.addClothesBtn.clicked.connect(self.add_clothes)
        self.exitAccountBtn.clicked.connect(self.exit_account)

    def set_user_id(self, user_id):
        self.current_user_id = user_id
        self.clear_orders()
        self.load_orders()

    def load_clothes(self, clothes=None):
        if clothes is None:
            clothes = db.get_all_clothes()

        clothes_cards = []

        for clothes in clothes:
            clothes_card = ClothesCard(clothes[0], clothes[2], clothes[3], db.get_category_name(clothes[1]), clothes[4], clothes[5], clothes[7],
                                     clothes[6], True, self.main_window, parent_window=self)
            clothes_cards.append(clothes_card)
            self.clothesLayout.addWidget(clothes_card)

        ClothesCard.check_clothes(clothes_cards)

    def load_orders(self, orders=None):
        if orders is None:
            orders = db.get_all_orders()

        for order in orders:
            order_card = OrderCard(order[0], order[1], order[6], order[2], order[3], order[4], order[5], main_window=self.main_window, parent_window=self)
            self.ordersLayout.addWidget(order_card)

    def clear_products(self):
        self.clear_layout(self.clothesLayout)

    def clear_orders(self):
        self.clear_layout(self.ordersLayout)

    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def search_clothes(self):
        text = self.searchBar.text()
        clothes = None

        if len(text.strip()) != 0:
            clothes = db.search_clothes_name(self.searchBar.text())

        self.clear_products()
        self.load_clothes(clothes)

    def search_orders(self):
        text = self.orderSearchBar.text()

        orders = None

        if len(text.strip()) != 0:
            orders = db.get_orders_by_user(int(self.orderSearchBar.text()))

        self.clear_orders()
        self.load_orders(orders)

    def add_clothes(self):
        if self.main_window is not None:
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.add_clothes_view)

    def exit_account(self):
        if show_question_message("Вы точно хотите выйти с аккаунта?"):
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.authorization)