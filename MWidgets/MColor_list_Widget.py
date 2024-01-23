from PySide6.QtGui import QColor, QIcon, QPainter, QPen, QPixmap
from PySide6.QtWidgets import QColorDialog

from .Modified_list_widget import Modified_list_widget, QListWidgetItem, QWidget


class MColor_list_Widget(Modified_list_widget):
    
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.icon = QPixmap(30, 30)
        self.icon.fill(QColor(0, 0, 0, 0))
    
    def edit_current_item(self):
        """
        :return: None
        """
        item = self.item(self.currentRow())
        if item is not None:
            dialog = QColorDialog(item.text(), self)
            dialog.setWindowIcon(QIcon(':/FPGresources/icons96/icons8-edit.png'))
            dialog.setWindowTitle('Изменение')
            accepted = dialog.exec()
            color = dialog.selectedColor()
            if accepted:
                item.setIcon(self.draw_icon_for_item(color))
                item.setText(color.name(QColor.NameFormat.HexRgb).upper())
    
    def addItem(self, item: QListWidgetItem | QColor | str = None):
        if item is None:
            self.add_color()
        elif isinstance(item, QColor):
            self.add_color(item)
        else:
            super().addItem(item)
    
    def add_color(self, color: QColor = None):
        """
        :raises TypeError:
        :param color:
        :return: None
        """
        if isinstance(color, QColor):
            accepted = True
        elif color is None:
            dialog = QColorDialog(self)
            dialog.setWindowIcon(QIcon(':/FPGresources/icons96/icons8-add.png'))
            dialog.setWindowTitle('Добавление')
            accepted = dialog.exec()
            color = dialog.selectedColor()
        else:
            raise TypeError("The argument must be a QColor")
        if accepted:
            item = QListWidgetItem(
                    self.draw_icon_for_item(color),
                    color.name(QColor.NameFormat.HexRgb).upper(),
            )
            self.addItem(item)
    
    def draw_icon_for_item(self, color: QColor) -> QPixmap:
        icon = self.icon.copy()
        with QPainter(icon) as painter:
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            painter.setPen(QPen(QColor("black"), 2))
            painter.setBrush(color)
            painter.drawEllipse(1, 1, icon.height() - 2, icon.width() - 2)
        return icon
    
    def get_colors(self) -> tuple[QColor, ...]:
        return tuple(QColor(item.text()) for item in self.getitems())
    
    def getitems(self) -> tuple[QListWidgetItem, ...]:
        """
        The color is stored in the MColor_list_Widget.ColorRole
        following Qt.ItemDataRole.UserRole as a QColor object
        :return: list[QListWidgetItem]
        """
        return super().getitems()
