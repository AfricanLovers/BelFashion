from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from design.layouts.clothes_card_layout import Ui_ClothesCard
from .helper import show_question_message
from loader import cart, db


class ClothesCard(QtWidgets.QWidget, Ui_ClothesCard):

    def __init__(self, clothes_id, title, brand, category, year, description, image, price=0, is_admin=False, main_window=None, parent=None, parent_window=None):
        super(ClothesCard, self).__init__(parent)
        self.setupUi(self)

        self.is_admin = is_admin
        self.main_window = main_window
        self.parent_window = parent_window

        self.clothes_id = clothes_id
        self.description = description
        self.clothes_count = 1

        self.clothesTitle.setText(title)
        self.clothesBrand.setText(f"Брэнд одежды: {brand}")
        self.clothesCategory.setText(f"Категория: {category}")
        self.clothesYear.setText(f"Год пошива: {year}")
        self.clothesPrice.setText(f"Цена: {price}")
        self.countSpinBox.valueChanged.connect(self.change_count)

        if image is not None:
            pixmap = QPixmap()
            pixmap.loadFromData(image)
            self.clothesImage.setPixmap(pixmap)
            self.clothesImage.setAlignment(Qt.AlignCenter)
            self.clothesImage.setScaledContents(True)

        self.addCartBtn.clicked.connect(self.add_to_cart)
        self.infoBtn.clicked.connect(self.show_clothes_info)

        if is_admin:
            QTimer.singleShot(0, self.modify_card)

    def modify_card(self):
        self.addCartBtn.clicked.disconnect()
        self.addCartBtn.setText("Удалить одежду")
        self.addCartBtn.setStyleSheet('background-color: rgb(100, 0, 51);')
        self.addCartBtn.clicked.connect(self.click_delete)

        self.countLabel.hide()
        self.countSpinBox.hide()

    def click_delete(self):
        if show_question_message("Вы уверены, что хотите удалить эту одежду?"):
            db.remove_clothes(self.clothes_id)
            self.deleteLater()

    @staticmethod
    def check_clothes(clothes):
        for clothes in clothes:
            if clothes.clothes_id in cart.get_clothes_ids():
                clothes.set_added()
            else:
                clothes.set_removed()

    def add_to_cart(self):
        if self.clothes_id not in cart.get_clothes_ids():
            cart.add_clothes(self.clothes_id, self.clothes_count)
            self.set_added()
        else:
            cart.remove_clothes(self.clothes_id)
            self.set_removed()

    def set_added(self):
        self.addCartBtn.setText("Убрать Из Корзины")
        self.addCartBtn.setStyleSheet('background-color: rgb(100, 0, 51);')

    def set_removed(self):
        self.addCartBtn.setText("Добавить В Корзину")
        self.addCartBtn.setStyleSheet('background-color: rgb(0, 100, 51);')

    def change_count(self):
        self.clothes_count = int(self.countSpinBox.value())
        cart.update_clothes(self.clothes_id, self.clothes_count)

    def set_count(self, clothes_count):
        self.clothes_count = clothes_count
        self.countSpinBox.setValue(clothes_count)

    def show_clothes_info(self):

        if self.main_window is not None:
            self.main_window.clothes_info_view.set_last_window(self.parent_window)
            self.main_window.clothes_info_view.set_clothes_id(self.clothes_id)
            self.main_window.clothes_info_view.set_is_admin(self.is_admin)
            self.main_window.clothes_info_view.set_parent_window(self)
            self.main_window.clothes_info_view.set_last_window(self.parent_window)
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.clothes_info_view)
