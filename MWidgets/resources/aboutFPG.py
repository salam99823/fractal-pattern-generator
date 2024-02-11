from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtWidgets import (QDialogButtonBox, QGraphicsScene, QVBoxLayout)

from MWidgets.MGraphicsView import MGraphicsView


class Ui_Dialog(object):
    buttonBox = None
    
    def setupUi(self, Dialog):
        Dialog.resize(350, 300)
        verticalLayout = QVBoxLayout(Dialog)
        pixm = QPixmap(':/FPGresources/icons96/icons8-history-folder.png')
        view = MGraphicsView()
        view.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        view.setScene(QGraphicsScene(0, 0, 2000, 2000))
        view.setDragMode(view.DragMode.ScrollHandDrag)
        view.scene().addPixmap(pixm)
        verticalLayout.addWidget(view)
        print(view.translate(10, 10))
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok, Dialog)
        verticalLayout.addWidget(self.buttonBox)
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        QMetaObject.connectSlotsByName(Dialog)
    
    # setupUi
    
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
    # retranslateUi
