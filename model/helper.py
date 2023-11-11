from PyQt5.QtWidgets import QMessageBox


def show_error_message(message):
    error_dialog = QMessageBox()
    error_dialog.setWindowTitle("Ошибка")
    error_dialog.setIcon(QMessageBox.Critical)
    error_dialog.setText(message)
    error_dialog.setStandardButtons(QMessageBox.Ok)

    error_dialog.setStyleSheet("""
        QMessageBox {
            background-color: #F9EBE0;
            font-size: 16px;
            color: #D43F00;
            border: 2px solid #D43F00;
            border-radius: 5px;
        }
        QMessageBox QLabel {
            background-color: transparent;
            color: #000000;
        }
        QMessageBox QPushButton {
            background-color: #D43F00;
            color: #FFFFFF;
            padding: 10px;
            border-radius: 3px;
            min-width: 80px;
            height: 10px;
        }
        QMessageBox QPushButton:hover {
            background-color: #BF360C;
        }
    """)

    error_dialog.exec_()


def show_success_message(message):
    success_dialog = QMessageBox()
    success_dialog.setWindowTitle("Успех")
    success_dialog.setIcon(QMessageBox.Information)
    success_dialog.setText(message)
    success_dialog.setStandardButtons(QMessageBox.Ok)

    success_dialog.setStyleSheet("""
        QMessageBox {
            background-color: #E6F9E0;
            font-size: 16px;
            color: #008D3F;
            border: 2px solid #008D3F;
            border-radius: 5px;
        }
        QMessageBox QLabel {
            background-color: transparent;
            color: #000000;
        }
        QMessageBox QPushButton {
            background-color: #008D3F;
            color: #FFFFFF;
            padding: 10px;
            border-radius: 3px;
            min-width: 80px;
            height: 10px;
        }
        QMessageBox QPushButton:hover {
            background-color: #006F2E;
        }
    """)

    success_dialog.exec_()


def show_question_message(question) -> bool:
    question_dialog = QMessageBox()
    question_dialog.setWindowTitle("Вопрос")
    question_dialog.setIcon(QMessageBox.Question)
    question_dialog.setText(question)
    question_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

    question_dialog.setStyleSheet("""
        QMessageBox {
            background-color: #E0F0F9;
            font-size: 16px;
            color: #0058D4;
            border: 2px solid #0058D4;
            border-radius: 5px;
        }
        QMessageBox QLabel {
            background-color: transparent;
            color: #000000;
        }
        QMessageBox QPushButton {
            background-color: #0058D4;
            color: #FFFFFF;
            padding: 10px;
            border-radius: 3px;
            min-width: 80px;
            height: 10px;
        }
        QMessageBox QPushButton:hover {
            background-color: #003F8F;
        }
    """)

    return question_dialog.exec_() == QMessageBox.Yes
