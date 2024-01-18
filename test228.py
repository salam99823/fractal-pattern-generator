import sys

from PySide6.QtGui import Qt
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit, QDateTimeEdit, QDial, QDoubleSpinBox,
                               QFontComboBox, QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
                               QProgressBar, QPushButton, QRadioButton, QSlider, QSpinBox, QTimeEdit, QVBoxLayout,
                               QWidget)

from MWidgets.MList_Widgets.MColor_list_Widget import MColor_list_Widget

sys.argv += ['-platform', 'windows']


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Widgets App")
        self.setStyleSheet(
                """
QDialogButtonBox { dialogbuttonbox-buttons-have-icons: 1; }
QPlainTextEdit {
    border-width: 5px;
    border-style: solid;
    border-color: white;
    border-radius: 10px;
    bottom: 50px;
    alternate-background-color: blue;
    background-image: url(:/icons/icons/icons8-down-96.png);
    background-repeat: repeat-;
    background-position: center;
    background-attachment: fixed;
    background-origin: content;
    background-clip: padding;
}
                """
        )
        widget = QWidget(self)
        layout = QVBoxLayout(widget)
        widgets = [
            QPushButton,
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLineEdit,
            QProgressBar,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
            QLabel
        ]
        TextEdit = QPlainTextEdit(widget)
        TextEdit.setMinimumSize(300, 300)
        layout.addWidget(TextEdit)
        box = MColor_list_Widget()
        box.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        layout.addWidget(box)
        for w in widgets:
            layout.addWidget(w())
        
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
app.setStyle('Fusion')
window = MainWindow()
window.show()
app.exec()
