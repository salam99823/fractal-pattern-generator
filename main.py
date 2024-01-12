"""

"""
import sys

from PySide6.QtCore import QPoint, Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu

from icons import resources_rc
from uis.mainwindow import Ui_MainWindow


class Main_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action_about_Qt.triggered.connect(QApplication.aboutQt)
        self.rules_list.customContextMenuRequested.connect(self.show_menu)
        self.colors_list.customContextMenuRequested.connect(self.show_menu)
    
    @Slot(QPoint, name = 'show_menu')
    def show_menu(self, position: QPoint):
        menu = QMenu(self)
        menu.addAction(QIcon(':/icons/icons/icons8-add-96.png'), "Добавить", self.sender().addItem)
        menu.addAction(QIcon(':/icons/icons/icons8-edit-240.png'), "Изменить", self.sender().edit_current_item)
        menu.addAction(QIcon(':/icons/icons/icons8-thick-arrow-pointing-up-96.png'), "Вверх", self.sender().raise_item)
        menu.addAction(QIcon(':/icons/icons/icons8-down-96.png'), "Вниз", self.sender().omit_item)
        menu.addAction(QIcon(':/icons/icons/icons8-close-96.png'), "Удалить", self.sender().take_current_item)
        menu.addAction(QIcon(':/icons/icons/icons8-delete-240.png'), "Очистить", self.sender().clear)
        menu.exec(self.sender().mapToGlobal(position))


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
