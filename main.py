import argparse

from PySide6.QtCore import Slot
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QDialog, QGraphicsScene, QGraphicsView, QInputDialog, QMainWindow

from MWidgets.MGraphicsView import MGraphicsView
from MWidgets.resources.aboutFPG import Ui_Dialog
from MWidgets.resources.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    graphics_View: MGraphicsView
    
    class Ui(Ui_MainWindow):
        def setupUi(self, main_window: "MainWindow"):
            super().setupUi(main_window)
            scene = QGraphicsScene()
            scene.setMinimumRenderSize(0.1)
            scene.setBackgroundBrush(QColor(255, 255, 255))
            self.graphics_View.setScene(scene)
            self.graphics_View.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
            self.graphics_View.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
            self.graphics_View.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.SmartViewportUpdate)
            
            self.graphics_View.rules_list = self.rules_list
            self.graphics_View.axiom = self.axiom
            self.graphics_View.number_of_iterations = self.number_of_iter
            self.graphics_View.line_width = self.line_width
            self.graphics_View.length_of_line = self.line_length
            self.graphics_View.angle_of_rotation = self.rotation_angle
            self.graphics_View.color_list = self.colors_list
            
            self.start_button.clicked.connect(self.graphics_View.draw_fractal)
            
            self.action_about_Qt.triggered.connect(QApplication.aboutQt)
            self.action_about_program.triggered.connect(main_window.about_program)
            self.action_zoom_in.triggered.connect(self.graphics_View.zoom_in)
            self.action_zoom_out.triggered.connect(self.graphics_View.zoom_out)
            self.action_reset_zoom_to_actual_size.triggered.connect(self.graphics_View.reset_zoom)
            self.action_escape.triggered.connect(main_window.close)
            self.action_new_file.triggered.connect(main_window.open_new_file)
            main_window.graphics_View = self.graphics_View
    
    def __init__(self):
        super().__init__()
        Ui = self.Ui()
        Ui.setupUi(self)
    
    @Slot(name = 'about_program')
    def about_program(self):
        dial = QDialog(self)
        Ui_Dialog().setupUi(dial)
        dial.exec()
    
    @Slot(name = 'open_new_file')
    def open_new_file(self):
        self.graphics_View.load_file(QInputDialog.getText(self, 'Открыть файл', 'Выберите фай'))


def main():
    _parser = argparse.ArgumentParser()
    _parser.add_argument('-f', '--file', type = argparse.FileType(encoding = 'utf-8'))
    args = _parser.parse_args()
    print(args)
    app = QApplication()
    app.setStyle('fusion')
    win = MainWindow()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()
