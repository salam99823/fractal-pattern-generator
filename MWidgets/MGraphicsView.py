from dataclasses import dataclass
from json import JSONDecodeError, loads

from PySide6.QtCore import QLineF, Slot
from PySide6.QtGui import QColor, QPen, Qt, QWheelEvent
from PySide6.QtWidgets import QDoubleSpinBox, QGraphicsView, QLineEdit, QSpinBox

from Lsystems.Lsystem import LSystem
from MTurtle import MTurtle
from MWidgets.MColor_list_Widget import MColor_list_Widget
from MWidgets.MText_list_Widget import MText_list_Widget


class MGraphicsView(QGraphicsView):
    rules_list: MText_list_Widget
    color_list: MColor_list_Widget
    axiom: QLineEdit
    number_of_iterations: QSpinBox
    line_width: QDoubleSpinBox
    length_of_line: QDoubleSpinBox
    angle_of_rotation: QDoubleSpinBox
    
    @dataclass
    class Params:
        rules: list[str]
        colors: list[str]
        axiom: str
        number_of_iterations: int
        line_width: float
        length_of_line: float
        angle_of_rotation: float
        
        def __post_init__(self):
            print(self.rules, 'Params')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lsystem = LSystem(keywords = ('F', 'B', 'f', 'b', 'L', 'R', 'C'))
        self.turtle = MTurtle(MTurtle.Commands(*(key for key, *_ in self.lsystem.keywords)))
    
    def wheelEvent(self, event: QWheelEvent):
        if event.angleDelta().y() > 0:
            self.zoom_in()
        else:
            self.zoom_out()
        event.accept()
    
    @Slot(name = 'zoom_in')
    def zoom_in(self):
        self.scale(1.1, 1.1)
    
    @Slot(name = 'zoom_out')
    def zoom_out(self):
        self.scale(0.9, 0.9)
    
    @Slot(name = 'draw_fractal')
    def draw_fractal(self):
        rules: tuple = tuple(
                tuple(rul) for rule in self.rules_list.get_texts()
                if len(rul := rule.split(maxsplit = 2)) == 2
        )
        scene = self.scene()
        self.lsystem.rules = rules
        lines = self.turtle.execute(
                self.lsystem.formatting(
                        self.lsystem.use_rules(
                                self.axiom.text(),
                                self.number_of_iterations.value()
                        )
                ),
                self.angle_of_rotation.value(),
                self.length_of_line.value(),
                self.length_of_line.value()
        )
        scene.clear()
        scene.setSceneRect(0, 0, 0, 0)
        colors = tuple(self.color_list.get_colors()) or (QColor('black'),)
        pen = QPen(
                QColor('black'),
                self.line_width.value(),
                Qt.PenStyle.SolidLine,
                Qt.PenCapStyle.RoundCap,
                Qt.PenJoinStyle.RoundJoin
        )
        for ((x1, y1), (x2, y2)), color_index in lines:
            pen.setColor(colors[color_index % len(colors)])
            scene.addLine(QLineF(x1, y1, x2, y2), pen)
        self.turtle.reset()
    
    @Slot(name = 'reset_zoom')
    def reset_zoom(self):
        self.resetTransform()
    
    def load_file(self, file: str, extension: str):
        print(file, extension)  # TODO: добавь способы открытия: json, csv, xml
        try:
            with open(file) as f:
                params = self.Params(**loads(f.read()))
            self.rules_list.clear()
            self.color_list.clear()
            self.axiom.setText(params.axiom)
            self.number_of_iterations.setValue(params.number_of_iterations)
            self.line_width.setValue(params.line_width)
            self.length_of_line.setValue(params.length_of_line)
            self.angle_of_rotation.setValue(params.angle_of_rotation)
            for key, value in params.rules:
                self.rules_list.add_text(f'{key} {value}')
            for color_name in params.colors:
                self.color_list.add_color(QColor(color_name))
        except JSONDecodeError as e:
            print(e)
