import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QStyle

from untitled import Ui_MainWindow


class Main_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action_open_file.setIcon(self.style().standardPixmap(QStyle.StandardPixmap.SP_DialogOpenButton))
        self.action_open_file_2.setIcon(self.style().standardPixmap(QStyle.StandardPixmap.SP_DialogOpenButton))
        self.action_new_file.setIcon(self.style().standardPixmap(QStyle.StandardPixmap.SP_FileIcon))
        self.action_new_file_2.setIcon(self.style().standardPixmap(QStyle.StandardPixmap.SP_FileIcon))
        QIcon
        self.action_save_file_2.setIcon(self.style().standardPixmap(QStyle.StandardPixmap.SP_DialogSaveAllButton))
        self.action_about_Qt.setIcon(self.style().standardPixmap(QStyle.StandardPixmap.SP_TitleBarMenuButton))
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
    main()
