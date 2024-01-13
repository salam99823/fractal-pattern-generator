from PySide6.QtCore import QPoint, Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QMenu,
    QWidget,
)


class Modified_list_widget(QListWidget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.menu = QMenu(self)
        self.menu.addAction(
                QIcon(':/icons/icons/icons8-add-96.png'), "Добавить", self.addItem
        )
        self.menu.addAction(
                QIcon(':/icons/icons/icons8-edit-240.png'), "Изменить", self.edit_current_item
        )
        self.menu.addAction(
                QIcon(':/icons/icons/icons8-thick-arrow-pointing-up-96.png'), "Вверх", self.raise_item
        )
        self.menu.addAction(
                QIcon(':/icons/icons/icons8-down-96.png'), "Вниз", self.omit_item
        )
        self.menu.addAction(
                QIcon(':/icons/icons/icons8-close-96.png'), "Удалить", self.take_current_item
        )
        self.menu.addAction(
                QIcon(':/icons/icons/icons8-delete-240.png'), "Очистить", self.clear
        )
    
    @Slot(QPoint, name = 'show_menu')
    def show_menu(self, position: QPoint):
        self.menu.exec(self.mapToGlobal(position))
    
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
    
    def getitems(self) -> tuple[QListWidgetItem, ...]:
        return tuple(self.item(index) for index in range(self.count()))
    
    def __repr__(self):
        return f'{self.__class__.__name__}{tuple(item.text() for item in self.getitems())}'
