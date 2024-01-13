"""

"""
import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow

from MWidgets.uis.mainwindow import Ui_MainWindow
from MWidgets.uis.rc_resorses import rc_resources



class Main_window(QMainWindow):
    class Ui_main_widow(Ui_MainWindow):
        def setupUi(self, MainWindow):
            super().setupUi(MainWindow)
             self.action_about_Qt.triggered.connect(QApplication.aboutQt)
             self.action_about_program.triggered.connect(MainWindow.tst)
             self.rules_list.customContextMenuRequested.connect(self.rules_list.show_menu)
             self.colors_list.customContextMenuRequested.connect(self.colors_list.show_menu)
    def __init__(self):
        super().__init__()
        Ui_main_widow().setupUi(self)
    
    def tst(self):
        dial = QDialog(self)
        dial.setLayout()
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
