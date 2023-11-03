import sys
from PyQt5.QtWidgets import *
from qt_material import apply_stylesheet


class Main(QMainWindow):

    def __init__(self, *args):
        super(Main, self).__init__(*args)
        self.setMinimumWidth(850)
        self.setMinimumHeight(600)

        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, 'dark_cyan.xml')
    window = Main()
    window.show()
    sys.exit(app.exec_())
