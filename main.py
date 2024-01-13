"""

"""
import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow

from MWidgets.uis.mainwindow import Ui_MainWindow
from MWidgets.uis.rc_resorses import rc_resources


class Main_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action_about_Qt.triggered.connect(QApplication.aboutQt)
        self.action_about_program.triggered.connect(self.tst)
        self.rules_list.customContextMenuRequested.connect(self.rules_list.show_menu)
        self.colors_list.customContextMenuRequested.connect(self.colors_list.show_menu)
    
    def tst(self):
        dial = QDialog(self)
        
        dial.exec()

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
        rc_resources.qCleanupResources()
