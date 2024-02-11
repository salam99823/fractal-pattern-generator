import argparse

from PySide6.QtCore import Slot
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QGraphicsScene, QGraphicsView, QMainWindow

from MWidgets.resources.aboutFPG import Ui_Dialog
from MWidgets.resources.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    
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
    
    def __init__(self, _file = None):
        super().__init__()
        self.Ui = self.Ui()
        self.Ui.setupUi(self)
        if _file is not None:
            self.Ui.graphics_View.load_file(_file)
    
    @Slot(name = 'about_program')
    def about_program(self):
        dial = QDialog(self)
        Ui_Dialog().setupUi(dial)
        dial.exec()
    
    @Slot(name = 'open_new_file')
    def open_new_file(self):
        self.Ui.graphics_View.load_file(
                *QFileDialog.getSaveFileName(
                        self,
                        'Открыть новый файл',
                        filter = 'JSON (*.json);;CSV (*.csv);;XML (*.xml)'
                )
        )


def main():
    _parser = argparse.ArgumentParser()
    _parser.add_argument('-f', '--file', type = argparse.FileType(encoding = 'utf-8'))
    file = _parser.parse_args().file
    print(file)
    app = QApplication()
    app.setStyle('fusion')
    win = MainWindow(file)
    size = app.primaryScreen().size()
    win.resize(size.width() / 1.5, size.height() / 1.5)
    win.show()
    app.exec()


if __name__ == '__main__':
    main()
