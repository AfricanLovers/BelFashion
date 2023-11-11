from PyQt5.QtWidgets import QMainWindow, QLineEdit
from loader import db
from design.layouts.authorization_layout import Ui_MainWindow
from .helper import show_error_message


class Authorization(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, main_window=None):
        super(Authorization, self).__init__(*args)
        self.setupUi(self)

        self.main_window = main_window
        self.showPasswordCheckBox.stateChanged.connect(self.show_password)
        self.registerButton.clicked.connect(self.show_registration)
        self.loginButton.clicked.connect(self.login)

    def show_password(self):
        mode = QLineEdit.Normal if self.showPasswordCheckBox.isChecked() else QLineEdit.Password
        self.passwordEdit.setEchoMode(mode)

    def show_registration(self):
        if self.main_window is not None:
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.registration)

    def validate_inputs(self, username, password):
        if not username or not password:
            show_error_message("Пожалуйста, заполните все поля")
            return False
        return True

    def login(self):
        username = self.usernameEdit.text().strip()
        password = self.passwordEdit.text().strip()

        if not self.validate_inputs(username, password):
            return

        if db.check_user(username, password):
            user_id = db.get_user(username)[0]
            if db.is_admin(username, password):
                self.main_window.admin_panel.set_user_id(user_id)
                self.main_window.stacked_widget.setCurrentWidget(self.main_window.admin_panel)
            else:
                self.main_window.mainMenu.set_user_id(user_id)
                self.main_window.stacked_widget.setCurrentWidget(self.main_window.mainMenu)
        else:
            show_error_message("Неверный логин или пароль")
