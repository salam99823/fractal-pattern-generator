import sys

import MWidgets.resources.resources_rc
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit, QDateTimeEdit, QDial, QDialogButtonBox,
                               QDoubleSpinBox, QFontComboBox, QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
                               QProgressBar, QPushButton, QRadioButton, QSlider, QSpinBox, QTimeEdit, QVBoxLayout,
                               QWidget)

MWidgets.uis.resources_rc.qInitResources()

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
        box = QDialogButtonBox()
        box.setStandardButtons(QDialogButtonBox.StandardButton.LastButton)
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
