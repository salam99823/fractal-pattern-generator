"""
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'multilinedialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
"""
from PySide6.QtCore import (QMetaObject, Qt)
from PySide6.QtWidgets import (QDialogButtonBox,
                               QLabel, QPlainTextEdit, QVBoxLayout)


class Ui_multiline_dialog(object):
    def setupUi(self, multiline_dialog):
        if not multiline_dialog.objectName():
            multiline_dialog.setObjectName(u"multiline_dialog")
        multiline_dialog.resize(274, 262)
        self.vboxLayout = QVBoxLayout(multiline_dialog)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.label = QLabel(multiline_dialog)
        self.label.setObjectName(u"label")
        
        self.vboxLayout.addWidget(self.label)
        
        self.plainTextEdit = QPlainTextEdit(multiline_dialog)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        
        self.vboxLayout.addWidget(self.plainTextEdit)
        
        self.buttonBox = QDialogButtonBox(multiline_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(False)
        
        self.vboxLayout.addWidget(self.buttonBox)
        
        self.retranslateUi(multiline_dialog)
        self.buttonBox.accepted.connect(multiline_dialog.accept)
        self.buttonBox.rejected.connect(multiline_dialog.reject)
        
        QMetaObject.connectSlotsByName(multiline_dialog)
    
    # setupUi
    
    def retranslateUi(self, multiline_dialog):
        pass
    # retranslateUi
