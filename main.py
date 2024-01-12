"""

"""
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from icons import resources_rc
from untitled import Ui_MainWindow


class Main_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.file_menu.triggered.connect(print)


def main():
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    # setup stylesheet
    #apply_stylesheet(app, theme='dark_cyan.xml')
    win = Main_window()
    win.show()
    print(app.arguments())
    app.exec()


if __name__ == '__main__':
    try:
        main()
    finally:
        resources_rc.qCleanupResources()
