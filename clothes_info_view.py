from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import *
from design.layouts.clothes_info_layout import Ui_ClothesDetails
from loader import db, cart
from .helper import show_question_message


class clothesInfoView(QMainWindow, Ui_clothesDetails):

    def __init__(self, *args, clothes_id=-1, main_window=None, current_user_id=-1, is_admin=False):
        super(ClothesInfoView, self).__init__(*args)
        self.setupUi(self)

        self.clothes_id = clothes_id
        self.main_window = main_window
        self.current_user_id = current_user_id
        self.is_admin = is_admin
        self.last_window = None
        self.parent_window = None

        cart.addOnAddCallback(self.on_add_clothes)
        cart.addOnRemoveCallback(self.on_remove_clothes)

        self.load_info()
        self.backButton.clicked.connect(self.go_back)
        self.cartButton.clicked.connect(self.add_to_cart)

        if is_admin:
            QTimer.singleShot(0, self.modify_to_admin)

    def modify_to_admin(self):
        self.cartButton.clicked.disconnect()

        self.cartButton.setText("Удалить одежду")
        self.cartButton.setStyleSheet('background-color: rgb(100, 0, 51);')
        self.cartButton.clicked.connect(self.click_delete)

        if self.bottom_buttons_layout.layout().count() < 2:
            self.editButton = QPushButton(self)
            self.editButton.setText("Редактировать одежду")
            self.editButton.setMinimumHeight(30)
            self.editButton.setFont(QFont("Arial", 12))
            self.editButton.clicked.connect(self.show_edit_clothes_screen)
            self.bottom_buttons_layout.addWidget(self.editButton)

    def load_info(self):
        clothes = db.get_clothes_by_id(self.clothes_id)

        if clothes is None: return

        if clothes[7] is not None:
            pixmap = QPixmap()
            pixmap.loadFromData(clothes[7])
            self.coverImageLabel.setPixmap(pixmap)
            self.coverImageLabel.setAlignment(Qt.AlignCenter)
            self.coverImageLabel.setScaledContents(True)

        self.clothesNameLabel.setText(clothes[2])
        self.authorLabel.setText(clothes[3])
        self.yearLabel.setText(str(clothes[4]))
        self.categoryLabel.setText(db.get_category_name(clothes[1]))
        self.descriptionLabel.setText(clothes[5])
        self.priceLabel.setText(str(clothes[6]))

    def set_last_window(self, last_window):
        self.last_window = last_window

    def set_parent_window(self, parent_window):
        self.parent_window = parent_window

    def set_is_admin(self, is_admin):
        self.is_admin = is_admin

        if is_admin:
            self.modify_to_admin()

    def set_clothes_id(self, clothes_id):
        self.clothes_id = clothes_id
        self.load_info()

        if clothes_id in cart.get_clothess_ids():
            self.set_added()
        else:
            self.set_removed()

    def go_back(self):
        if self.main_window is not None:
            self.main_window.stacked_widget.setCurrentWidget(self.last_window)
            self.cartButton.show()

    def add_to_cart(self):
        if self.clothes_id not in cart.get_clothess_ids():
            cart.add_clothes(self.clothes_id)
            self.set_added()
        else:
            cart.remove_clothes(self.clothes_id)
            self.set_removed()

    def set_added(self):
        self.cartButton.setText("Убрать Из Корзины")
        self.cartButton.setStyleSheet('background-color: rgb(100, 0, 51);')

    def set_removed(self):
        self.cartButton.setText("Добавить В Корзину")
        self.cartButton.setStyleSheet('background-color: rgb(0, 100, 51);')

    def on_add_clothes(self, clothes_id, *args):
        if self.clothes_id == clothes_id:
            self.set_added()

    def on_remove_clothes(self, clothes_id):
        if self.clothes_id == clothes_id:
            self.set_removed()

    def hide_buttons(self):
        self.cartButton.hide()

    def click_delete(self):
        if show_question_message("Вы уверены, что хотите удалить эту одежду?"):
            db.remove_clothes(self.clothes_id)

            if self.parent_window is not None:
                self.parent_window.deleteLater()
            else:
                self.main_window.admin_panel.clear_products()
                self.main_window.admin_panel.load_clothess()

            self.main_window.stacked_widget.setCurrentWidget(self.main_window.admin_panel)
            self.cartButton.show()

    def show_edit_clothes_screen(self):
        if self.main_window is not None:
            self.main_window.add_clothes_view.set_is_edit(self.clothes_id)
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.add_clothes_view)
