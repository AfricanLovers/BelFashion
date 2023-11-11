import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
import qdarkstyle
from design.layouts.registration_layout import Ui_MainWindow
from loader import db
from .helper import show_error_message


class Registration(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, main_window=None):
        super(Registration, self).__init__(*args)
        self.setupUi(self)

        self.main_window = main_window

        self.showPasswordCheckBox.stateChanged.connect(self.show_password)
        self.loginButton.clicked.connect(self.show_login)
        self.registerButton.clicked.connect(self.register)

    def show_password(self):
        mode = QLineEdit.Normal if self.showPasswordCheckBox.isChecked() else QLineEdit.Password
        self.passwordEdit.setEchoMode(mode)
        self.repeatPasswordLineEdit.setEchoMode(mode)

    def show_login(self):
        if self.main_window is not None:
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.authorization)

    def validate_inputs(self, username, password, confirm_password):
        if not username or not password:
            show_error_message("Пожалуйста, заполните все поля")
            return False
        if len(password) <= 8:
            show_error_message("Пароль слишком короткий. Пароль должен содержать более 8 символов.")
            return False
        if password != confirm_password:
            show_error_message("Пароли не совпадают.")
            return False
        if db.user_in_db(username):
            show_error_message("Пользователь с таким именем существует. Пожалуйста авторизуйтесь или введите другое имя.")
            return False
        return True

    def register(self):
        username = self.usernameEdit.text().strip()
        password = self.passwordEdit.text().strip()
        confirm_password = self.repeatPasswordLineEdit.text().strip()

        if not self.validate_inputs(username, password, confirm_password):
            return

        try:
            db.add_user(username, password)
            self.main_window.mainMenu.set_user_id(db.get_user(username)[0])
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.mainMenu)
        except Exception as e:
            show_error_message(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = Registration()
    window.show()
    sys.exit(app.exec_())
