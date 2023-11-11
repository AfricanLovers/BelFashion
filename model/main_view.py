from PyQt5.QtWidgets import *
from .clothes_card import ClothesCard
from design.layouts.main_layout import Ui_MainWindow
from loader import db, cart
from .helper import show_question_message


class MainView(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, main_window=None, current_user_id=-1):
        super(MainView, self).__init__(*args)
        self.setupUi(self)

        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

        self.main_window = main_window
        self.current_user_id = current_user_id

        cart.addOnAddCallback(self.on_add_clothes)
        cart.addOnRemoveCallback(self.on_remove_clothes)
        cart.addOnUpdateCallback(self.on_update_clothes)

        self.containerLayout.setStretch(0, 1)
        self.containerLayout.setStretch(1, 3)

        self.load_categories()
        self.load_clothes()
        self.categoriesList.itemClicked.connect(self.filter_category)
        self.deleteFiltersBtn.clicked.connect(self.delete_filters)
        self.cartBtn.clicked.connect(self.go_cart)
        self.searchBar.textChanged.connect(self.search_clothes)
        self.exitAccountBtn.clicked.connect(self.exit_account)

    def load_clothes(self, clothes=None):
        if clothes is None:
            clothes = db.get_all_clothes()

        clothes_cards = []

        for clothes in clothes:
            clothes_card = ClothesCard(clothes[0], clothes[2], clothes[3], db.get_category_name(clothes[1]), clothes[4], clothes[5], clothes[7], clothes[6], main_window=self.main_window, parent_window=self)
            clothes_cards.append(clothes_card)
            self.productsVerticalLayout.addWidget(clothes_card)

        ClothesCard.check_clothes(clothes_cards)

    def load_categories(self):
        for category in db.get_all_categories():
            item = QListWidgetItem(category[1])
            item.category_id = category[0]
            self.categoriesList.addItem(item)

    def set_user_id(self, user_id):
        self.current_user_id = user_id

    def clear_products(self):
        layout = self.productsContainer.layout()

        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def filter_category(self, clothes):
        clothes = db.get_clothes_by_category(clothes.category_id)
        self.clear_products()
        self.load_clothes(clothes)

    def delete_filters(self):
        self.clear_products()
        self.load_clothes()

    def search_clothes(self):
        text = self.searchBar.text()
        clothes = None

        if len(text.strip()) != 0:
            clothes = db.search_clothes_name(self.searchBar.text())

        self.clear_products()
        self.load_clothes(clothes)

    def go_cart(self):
        if self.main_window is not None:
            self.main_window.cart.set_user_id(self.current_user_id)
            self.main_window.cart.load_cart()
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.cart)

    def on_add_clothes(self, clothes_id, clothes_count):
        layout = self.productsContainer.layout()

        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget is not None and (widget.clothes_id == clothes_id or clothes_id == -1):
                widget.set_added()
                widget.set_count(clothes_count)

    def on_remove_clothes(self, clothes_id):
        layout = self.productsContainer.layout()

        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget is not None and (widget.clothes_id == clothes_id or clothes_id == -1):
                widget.set_removed()

    def on_update_clothes(self, clothes_id, clothes_count):
        layout = self.productsContainer.layout()

        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget is not None and (widget.clothes_id == clothes_id or clothes_id == -1):
                widget.set_count(clothes_count)

    def exit_account(self):
        if show_question_message("Вы точно хотите выйти с аккаунта?"):
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.authorization)
