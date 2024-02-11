from typing import Iterator

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QWidget,
)


class Modified_list_widget(QListWidget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.addAction(
                QIcon(':/FPGresources/icons96/icons8-add.png'), "Добавить", self.addItem
        )
        self.addAction(
                QIcon(':/FPGresources/icons96/icons8-edit.png'), "Изменить", self.edit_current_item
        )
        self.addAction(
                QIcon(':/FPGresources/icons96/icons8-thick-arrow-pointing-up.png'), "Вверх", self.raise_item
        )
        self.addAction(
                QIcon(':/FPGresources/icons96/icons8-thick-arrow-pointing-down.png'), "Вниз", self.omit_item
        )
        self.addAction(
                QIcon(':/FPGresources/icons96/icons8-eraser-tool.png'), "Удалить", self.take_current_item
        )
        self.addAction(
                QIcon(':/FPGresources/icons96/icons8-delete.png'), "Очистить", self.clear
        )
    
    def addItem(self, item: QListWidgetItem | str):
        item = QListWidgetItem(item)
        super().addItem(item)
        self.setCurrentItem(item)
    
    def edit_current_item(self):
        print("Doesn't work, this is a function prototype")
    
    def raise_item(self):
        current = self.currentRow()
        if current > 0:
            item = self.takeItem(current)
            self.insertItem(current - 1, item)
            self.setCurrentItem(item)
    
    def omit_item(self):
        current = self.currentRow()
        if current < self.count():
            item = self.takeItem(current)
            self.insertItem(current + 1, item)
            self.setCurrentItem(item)
    
    def take_current_item(self) -> QListWidgetItem:
        return self.takeItem(self.currentRow())
    
    @property
    def functions(self) -> tuple:
        return (
            self.addItem,
            self.edit_current_item,
            self.raise_item,
            self.omit_item,
            self.take_current_item,
            self.clear,
        )
    
    def getitems(self) -> Iterator[QListWidgetItem]:
        return (self.item(index) for index in range(self.count()))
    
    def __repr__(self):
        return f'{self.__class__.__name__}{tuple(item.text() for item in self.getitems())}'
