from PySide6.QtGui import QColor, QPainter, QPen, QPixmap, QRgba64, Qt
from PySide6.QtWidgets import QColorDialog

from .Modified_list_widget import Modified_list_widget, QListWidgetItem, QWidget


class MColorDialog(QColorDialog):
    def __init__(
            self,
            initial: QColor | QRgba64 | Qt.GlobalColor | str | int = None,
            parent: QWidget | None = None,
    ):
        super().__init__(initial, parent)
    
    def get_color(self) -> tuple[QColor, bool]:
        result = bool(self.exec())
        return self.selectedColor(), result


class MColor_list_Widget(Modified_list_widget):
    
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.icon = QPixmap(30, 30)
        self.icon.fill(QColor(0, 0, 0, 0))
    
    def edit_current_item(self):
        """
        Only works with the current item, if it is not None,
        calls MColorDialog with the color of the current item,
        if the accept button is not clicked,
        the color remains the same.
        :return: None
        """
        item = self.item(self.currentRow())
        if item is not None:
            color, accepted = MColorDialog(
                    item.text(), self.parent()
            ).get_color()
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
            color, accepted = MColorDialog(parent = self).get_color()
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
