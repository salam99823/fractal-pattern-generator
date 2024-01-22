"""

"""
import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow

from MWidgets.uis.aboutFPG import Ui_Dialog
from MWidgets.uis.mainwindow import Ui_MainWindow


# import argparse


class MainWindow(QMainWindow):
    class Ui(Ui_MainWindow):
        def setupUi(self, main_window):
            super().setupUi(main_window)
            self.action_about_Qt.triggered.connect(QApplication.aboutQt)
            self.action_about_program.triggered.connect(main_window.tst)
            # self.start_button.clicked.connect(print)
    
    def __init__(self):
        super().__init__()
        self.Ui().setupUi(self)
    
    def tst(self):
        dial = QDialog(self)
        Ui_Dialog().setupUi(dial)
        
        dial.exec()


def main():
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    win = MainWindow()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()
