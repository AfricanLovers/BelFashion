from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from .helper import show_error_message, show_question_message
from design.layouts.add_clothes_layout import Ui_ClothesAddMainWindow
from loader import default_image, db


class AddClothesView(QtWidgets.QMainWindow, Ui_ClothesAddMainWindow):
    def __init__(self, *args, main_window=None, is_edit=False):
        super().__init__(*args)
        self.setupUi(self)

        self.main_window = main_window
        self.imagePath = None
        self.clothes_id = -1
        self.is_edit = False
        self.question_text = "Вы уверены, что хотите добавить одежду?"

        self.initUI()
        if is_edit:
            QTimer.singleShot(0, self.modify_to_edit)

    def initUI(self):
        self.addClothesButton.clicked.connect(self.addClothes)
        self.chooseCoverButton.clicked.connect(self.chooseImage)
        self.backBtn.clicked.connect(self.back)

        self.load_categories()
        self.setupImageLabel()

    def setupImageLabel(self):
        pixmap = QPixmap()
        pixmap.loadFromData(default_image)
        self.coverLabel.setPixmap(pixmap)
        self.coverLabel.setAlignment(Qt.AlignCenter)
        self.coverLabel.setScaledContents(True)

    def modify_to_edit(self):
        self.addClothesButton.setText("Изменить данные")
        self.mainTitleLabel.setText("Изменить одежду")
        self.question_text = "Вы уверены, что хотите изменить одежду?"
        self.is_edit = True

    def modify_to_add(self):
        self.addClothesButton.setText("Добавить одежду")
        self.mainTitleLabel.setText("Добавить одежду")
        self.question_text = "Вы уверены что хотите добавить одежду?"
        self.clothes_id = -1
        self.is_edit = False

    def load_categories(self):
        self.categoryComboBox.addItems([category[1] for category in db.get_all_categories()])

    def set_clothes_id(self, clothes_id):
        self.clothes_id = clothes_id
        QTimer.singleShot(0, self.modify_to_edit)
        self.modify_to_edit()
        self.load_info()

    def load_info(self):
        if self.clothes_id == -1:
            return

        clothes = db.get_clothes_by_id(self.clothes_id)

        self.clothesNameLineEdit.setText(clothes[2])
        self.brandLineEdit.setText(clothes[3])
        self.yearSpinBox.setValue(clothes[4])
        self.descriptionTextEdit.setText(clothes[5])
        self.priceDoubleSpinBox.setValue(clothes[6])
        pixmap = QPixmap()
        pixmap.loadFromData(clothes[7])
        self.coverLabel.setPixmap(pixmap)
        self.imagePath = clothes[7]

    def chooseImage(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter('Pictures (*.png *.jpg *.jpeg *.bmp)')

        if file_dialog.exec_():
            self.imagePath = file_dialog.selectedFiles()[0]
            pixmap = QPixmap(self.imagePath)
            self.coverLabel.setPixmap(pixmap)

    def addClothes(self):
        title = self.get_title()
        brand = self.get_brand()
        year = self.get_year()
        description = self.get_description()
        price = self.get_price()

        if not title.strip() or not brand.strip() or not year.strip() or not description.strip() or price <= 0:
            show_error_message("Пожалуйста, заполните все поля корректно.")
            return

        if show_question_message(self.question_text):
            category_id = db.get_category_id(self.categoryComboBox.currentText())
            if self.is_edit:
                db.update_clothes(self.clothes_id, category_id=category_id, clothes_name=title, brand=brand, year=year, description=description, price=price, cover=self.imagePath)
            else:
                db.add_clothes(title, brand, year, description, price, category_id, self.imagePath)

            if self.main_window is not None:
                self.main_window.admin_panel.clear_products()
                self.main_window.admin_panel.load_clothes()
                self.main_window.stacked_widget.setCurrentWidget(self.main_window.admin_panel)
                self.clear_all_fields()

    def back(self):
        if show_question_message("Вы точно хотите выйти?"):
            self.clear_all_fields()
            self.modify_to_add()
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.admin_panel)

    def clear_all_fields(self):
        self.clothesNameLineEdit.clear()
        self.brandLineEdit.clear()
        self.yearSpinBox.clear()
        self.descriptionTextEdit.clear()
        self.priceDoubleSpinBox.setValue(self.priceDoubleSpinBox.minimum())
        self.setupImageLabel()
        self.imagePath = None

    def get_title(self):
        return self.clothesNameLineEdit.text()

    def get_brand(self):
        return self.brandLineEdit.text()

    def get_year(self):
        return self.yearSpinBox.text()

    def get_description(self):
        return self.descriptionTextEdit.toPlainText()

    def get_price(self):
        return float(self.priceDoubleSpinBox.value())