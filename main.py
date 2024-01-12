import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from untitled import Ui_MainWindow, QColor


def main():
    argv = sys.argv + ['-platform', 'windows:darkmode']
    app = QApplication(argv)
    app.setStyle('Fusion')
    win = QMainWindow()
    Ui_MainWindow().setupUi(win)
    win.show()
    print(app.arguments())
    app.exec()


if __name__ == '__main__':
    main()
    