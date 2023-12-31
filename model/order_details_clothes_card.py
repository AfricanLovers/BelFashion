from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from design.layouts.clothes_card_layout import Ui_ClothesCard


class OrderDetailsClothesCard(QtWidgets.QWidget, Ui_ClothesCard):
    def __init__(self, clothes_id, title, brand, category, size, image, price=0, quantity=1, main_window=None, parent=None, parent_window=None):
        super().__init__(parent)
        self.setupUi(self)

        self.clothes_id = clothes_id
        self.main_window = main_window
        self.parent_window = parent_window

        self.init_ui_elements(title, brand, category, size, image, price, quantity)
        self.setup_buttons()

    def init_ui_elements(self, title, brand, category, size, image, price, quantity):
        self.clothesTitle.setText(title)
        self.clothesBrand.setText(f"Бренд: {brand}")
        self.clothesCategory.setText(f"Категория: {category}")
        self.clothesSize.setText(f"Размер: {size}")
        self.clothesPrice.setText(f"Цена: {price}")
        self.countSpinBox.setValue(int(quantity))
        self.countSpinBox.setReadOnly(True)

        if image is not None:
            pixmap = QPixmap()
            pixmap.loadFromData(image)
            self.clothesImage.setPixmap(pixmap)
            self.clothesImage.setAlignment(Qt.AlignCenter)
            self.clothesImage.setScaledContents(True)

        self.addCartBtn.hide()

    def setup_buttons(self):
        self.infoBtn.clicked.connect(self.show_clothes_info)

    def show_clothes_info(self):
        if self.main_window is not None:
            self.main_window.clothes_info_view.set_last_window(self.parent_window)
            self.main_window.clothes_info_view.set_clothes_id(self.clothes_id)
            self.main_window.clothes_info_view.set_is_admin(True)
            self.main_window.clothes_info_view.set_parent_window(self)
            self.main_window.clothes_info_view.hide_buttons()
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.clothes_info_view)