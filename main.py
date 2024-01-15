"""

"""
import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow

from MWidgets.uis.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    class Ui(Ui_MainWindow):
        def setupUi(self, main_window):
            super().setupUi(main_window)
            self.action_about_Qt.triggered.connect(QApplication.aboutQt)
            self.action_about_program.triggered.connect(main_window.tst)
    
    def __init__(self):
        super().__init__()
        self.Ui().setupUi(self)
    
    def tst(self):
        dial = QDialog(self)
        dial.setLayout()
        dial.exec()


def main():
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    win = MainWindow()
    win.show()
    print(app.arguments())
    app.exec()


if __name__ == '__main__':
    main()
