import argparse
import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow

from MWidgets.resources.aboutFPG import Ui_Dialog
from MWidgets.resources.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    class Ui(Ui_MainWindow):
        def setupUi(self, main_window):
            super().setupUi(main_window)
            self.action_about_Qt.triggered.connect(QApplication.aboutQt)  # type: ignore
            self.action_about_program.triggered.connect(main_window.tst)  # type: ignore
            # self.start_button.clicked.connect(print)
    
    def __init__(self):
        super().__init__()
        self.Ui().setupUi(self)
    
    def tst(self):
        dial = QDialog(self)
        Ui_Dialog().setupUi(dial)
        
        dial.exec()


def main():
    parser_ = argparse.ArgumentParser()
    parser_.add_argument('-f', '--file', type = argparse.FileType(encoding = 'utf-8'))
    args = parser_.parse_args()
    print(args)
    app = QApplication([sys.argv[0]])
    app.setStyle('fusion')
    win = MainWindow()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()
