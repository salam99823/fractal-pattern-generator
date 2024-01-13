from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QListWidgetItem, QWidget

from MWidgets.uis.multilinedialog import Ui_multiline_dialog
from .Modified_list_widget import Modified_list_widget


class Multiline_text_InputDialog(QDialog, Ui_multiline_dialog):
    def __init__(
            self,
            parent: QWidget,
            title: str,
            label: str,
            text: str,
            icon: QIcon = None,
            flag: Qt.WindowType = Qt.WindowType.Dialog,
    ):
        super().__init__(parent, flag)
        self.setupUi(self)
        self.buttonBox.button(
                QDialogButtonBox.StandardButton.Ok
        ).setIcon(
                QIcon(':/icons/icons/icons8-ok-240.png')
        )
        self.buttonBox.button(
                QDialogButtonBox.StandardButton.Cancel
        ).setIcon(
                QIcon(':/icons/icons/icons8-cancel-240.png')
        )
        self.setWindowTitle(title)
        self.label.setText(label)
        self.plainTextEdit.setPlainText(text)
        if isinstance(icon, QIcon):
            self.setWindowIcon(icon)
    
    def textValue(self):
        return self.plainTextEdit.toPlainText()
    
    def getMultiLineText(self) -> tuple[str, bool]:
        result = self.exec()
        return self.textValue(), not not result


class MText_list_Widget(Modified_list_widget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
    
    def addItem(self, item: QListWidgetItem | str | None = None, ):
        """
        :param item: QListWidgetItem | str | None = None
        
        :return: None
        """
        if item is None:
            self.add_text()
        else:
            super().addItem(item)
    
    def add_text(self, text: str | None = None, user_input_text: str = ''):
        """
        :param user_input_text:
        :param text:
        :return: None
        :raises TypeError:
        """
        if not isinstance(user_input_text, str):
            raise TypeError("The text must be a string")
        if isinstance(text, str):
            accepted = True
        elif text is None:
            text, accepted = Multiline_text_InputDialog(
                    self,
                    'Добавление',
                    'Введите текст',
                    user_input_text,
                    QIcon(':/icons/icons/icons8-add-96.png')
            ).getMultiLineText()
        else:
            raise TypeError("The text must be a string")
        if accepted:
            self.addItem(text)
    
    def edit_current_item(self):
        """
        Only works with the current item, if it is not None,
        calls QInputDialog with the text of the current item,
        if the accept button is not clicked or the length of the new text is zero,
        the text remains the same.
        :return: None
        """
        item = self.currentItem()
        if item is not None:
            item_text, accepted = Multiline_text_InputDialog(
                    self,
                    'Изменение',
                    'Введите текст',
                    item.text(),
                    QIcon(':/icons/icons/icons8-edit-240.png')
            ).getMultiLineText()
            if accepted:
                item.setText(item_text)
    
    def get_texts(self) -> tuple[str, ...]:
        # noinspection PyTypeChecker
        return tuple(item.text() for item in self.getitems())
