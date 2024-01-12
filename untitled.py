# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            Qt)
from PySide6.QtGui import (QAction)
from PySide6.QtWidgets import (QDockWidget, QDoubleSpinBox, QFormLayout,
                               QGraphicsView, QGroupBox, QHBoxLayout, QLabel,
                               QLineEdit, QListView, QMenu, QMenuBar, QPushButton, QSpinBox, QToolBar, QToolButton,
                               QVBoxLayout,
                               QWidget)

from MWidgets.MList_Widgets.MText_list_Widget import MText_list_Widget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(968, 748)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        MainWindow.setAcceptDrops(False)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.action_7 = QAction(MainWindow)
        self.action_7.setObjectName(u"action_7")
        self.action_8 = QAction(MainWindow)
        self.action_8.setObjectName(u"action_8")
        self.action_10 = QAction(MainWindow)
        self.action_10.setObjectName(u"action_10")
        self.action_Qt = QAction(MainWindow)
        self.action_Qt.setObjectName(u"action_Qt")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.graphics_View = QGraphicsView(self.central_widget)
        self.graphics_View.setObjectName(u"graphics_View")
        
        self.verticalLayout.addWidget(self.graphics_View)
        
        MainWindow.setCentralWidget(self.central_widget)
        self.dock_Widget = QDockWidget(MainWindow)
        self.dock_Widget.setObjectName(u"dock_Widget")
        self.dock_Widget_Contents = QWidget()
        self.dock_Widget_Contents.setObjectName(u"dock_Widget_Contents")
        self.verticalLayout_2 = QVBoxLayout(self.dock_Widget_Contents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.form_layout = QFormLayout()
        self.form_layout.setObjectName(u"form_layout")
        self.label_line_width = QLabel(self.dock_Widget_Contents)
        self.label_line_width.setObjectName(u"label_line_width")
        
        self.form_layout.setWidget(0, QFormLayout.LabelRole, self.label_line_width)
        
        self.line_width = QDoubleSpinBox(self.dock_Widget_Contents)
        self.line_width.setObjectName(u"line_width")
        
        self.form_layout.setWidget(0, QFormLayout.FieldRole, self.line_width)
        
        self.label = QLabel(self.dock_Widget_Contents)
        self.label.setObjectName(u"label")
        
        self.form_layout.setWidget(1, QFormLayout.LabelRole, self.label)
        
        self.number_of_iter = QSpinBox(self.dock_Widget_Contents)
        self.number_of_iter.setObjectName(u"number_of_iter")
        
        self.form_layout.setWidget(1, QFormLayout.FieldRole, self.number_of_iter)
        
        self.label_2 = QLabel(self.dock_Widget_Contents)
        self.label_2.setObjectName(u"label_2")
        
        self.form_layout.setWidget(2, QFormLayout.LabelRole, self.label_2)
        
        self.line_length = QDoubleSpinBox(self.dock_Widget_Contents)
        self.line_length.setObjectName(u"line_length")
        
        self.form_layout.setWidget(2, QFormLayout.FieldRole, self.line_length)
        
        self.label_3 = QLabel(self.dock_Widget_Contents)
        self.label_3.setObjectName(u"label_3")
        
        self.form_layout.setWidget(3, QFormLayout.LabelRole, self.label_3)
        
        self.rotation_angle = QDoubleSpinBox(self.dock_Widget_Contents)
        self.rotation_angle.setObjectName(u"rotation_angle")
        
        self.form_layout.setWidget(3, QFormLayout.FieldRole, self.rotation_angle)
        
        self.label_4 = QLabel(self.dock_Widget_Contents)
        self.label_4.setObjectName(u"label_4")
        
        self.form_layout.setWidget(4, QFormLayout.LabelRole, self.label_4)
        
        self.length_deviation = QDoubleSpinBox(self.dock_Widget_Contents)
        self.length_deviation.setObjectName(u"length_deviation")
        
        self.form_layout.setWidget(4, QFormLayout.FieldRole, self.length_deviation)
        
        self.label_5 = QLabel(self.dock_Widget_Contents)
        self.label_5.setObjectName(u"label_5")
        
        self.form_layout.setWidget(5, QFormLayout.LabelRole, self.label_5)
        
        self.rotation_angle_deviation = QDoubleSpinBox(self.dock_Widget_Contents)
        self.rotation_angle_deviation.setObjectName(u"rotation_angle_deviation")
        
        self.form_layout.setWidget(5, QFormLayout.FieldRole, self.rotation_angle_deviation)
        
        self.label_6 = QLabel(self.dock_Widget_Contents)
        self.label_6.setObjectName(u"label_6")
        
        self.form_layout.setWidget(6, QFormLayout.LabelRole, self.label_6)
        
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.axiom = QLineEdit(self.dock_Widget_Contents)
        self.axiom.setObjectName(u"axiom")
        
        self.horizontalLayout.addWidget(self.axiom)
        
        self.text_editing = QToolButton(self.dock_Widget_Contents)
        self.text_editing.setObjectName(u"text_editing")
        
        self.horizontalLayout.addWidget(self.text_editing)
        
        self.form_layout.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout)
        
        self.verticalLayout_2.addLayout(self.form_layout)
        
        self.groupBox = QGroupBox(self.dock_Widget_Contents)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.rules_list = MText_list_Widget(self.groupBox)
        self.rules_list.setObjectName(u"rules_list")
        
        self.verticalLayout_3.addWidget(self.rules_list)
        
        self.verticalLayout_2.addWidget(self.groupBox)
        
        self.groupBox_2 = QGroupBox(self.dock_Widget_Contents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.colors_list = QListView(self.groupBox_2)
        self.colors_list.setObjectName(u"colors_list")
        
        self.verticalLayout_4.addWidget(self.colors_list)
        
        self.verticalLayout_2.addWidget(self.groupBox_2)
        
        self.start_button = QPushButton(self.dock_Widget_Contents)
        self.start_button.setObjectName(u"start_button")
        
        self.verticalLayout_2.addWidget(self.start_button)
        
        self.stop_button = QPushButton(self.dock_Widget_Contents)
        self.stop_button.setObjectName(u"stop_button")
        
        self.verticalLayout_2.addWidget(self.stop_button)
        
        self.clear_button = QPushButton(self.dock_Widget_Contents)
        self.clear_button.setObjectName(u"clear_button")
        
        self.verticalLayout_2.addWidget(self.clear_button)
        
        self.dock_Widget.setWidget(self.dock_Widget_Contents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dock_Widget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 968, 22))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menuBar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menuBar)
        self.tool_Bar = QToolBar(MainWindow)
        self.tool_Bar.setObjectName(u"tool_Bar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.tool_Bar)
        
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_4)
        self.menu.addSeparator()
        self.menu.addAction(self.action_6)
        self.menu.addAction(self.action_7)
        self.menu.addAction(self.action_8)
        self.menu.addSeparator()
        self.menu.addAction(self.action_10)
        self.menu_2.addAction(self.action_Qt)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None)
            )
        self.action_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0440\u044b",
                None
                )
            )
        self.action_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435",
                None
                )
            )
        self.action_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"\u041d\u0435\u0434\u0430\u0432\u043d\u043e \u043e\u0442\u043a\u0440\u044b\u0442\u044b\u0435", None
                )
            )
        self.action_6.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None)
            )
        self.action_7.setText(
            QCoreApplication.translate(
                "MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a...", None
                )
            )
        self.action_8.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"\u0421\u043e\u0445\u0440\u043d\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435",
                None
                )
            )
        self.action_10.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.action_Qt.setText(QCoreApplication.translate("MainWindow", u"\u041e Qt", None))
        self.label_line_width.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.text_editing.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None)
            )
        self.tool_Bar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

