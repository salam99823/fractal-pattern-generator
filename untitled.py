# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDockWidget, QDoubleSpinBox,
    QFormLayout, QGraphicsView, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QToolBar, QToolButton, QVBoxLayout,
    QWidget)

from MWidgets.MList_Widgets.MColor_list_Widget import MColor_list_Widget
from MWidgets.MList_Widgets.MText_list_Widget import MText_list_Widget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(968, 748)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        MainWindow.setAcceptDrops(False)
        self.action_open_file = QAction(MainWindow)
        self.action_open_file.setObjectName(u"action_open_file")
        self.action_save_file = QAction(MainWindow)
        self.action_save_file.setObjectName(u"action_save_file")
        self.action_save_file_as = QAction(MainWindow)
        self.action_save_file_as.setObjectName(u"action_save_file_as")
        self.action_save_image = QAction(MainWindow)
        self.action_save_image.setObjectName(u"action_save_image")
        self.action_escape = QAction(MainWindow)
        self.action_escape.setObjectName(u"action_escape")
        self.action_escape.setMenuRole(QAction.QuitRole)
        self.action_about_Qt = QAction(MainWindow)
        self.action_about_Qt.setObjectName(u"action_about_Qt")
        self.action_about_Qt.setMenuRole(QAction.AboutQtRole)
        self.action_new_file = QAction(MainWindow)
        self.action_new_file.setObjectName(u"action_new_file")
        self.action_new_file_2 = QAction(MainWindow)
        self.action_new_file_2.setObjectName(u"action_new_file_2")
        self.action_open_file_2 = QAction(MainWindow)
        self.action_open_file_2.setObjectName(u"action_open_file_2")
        self.action_open_file_2.setMenuRole(QAction.TextHeuristicRole)
        self.action_save_file_2 = QAction(MainWindow)
        self.action_save_file_2.setObjectName(u"action_save_file_2")
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
        self.dock_Widget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
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
        self._3 = QVBoxLayout(self.groupBox)
        self._3.setObjectName(u"_3")
        self.rules_list = MText_list_Widget(self.groupBox)
        self.rules_list.setObjectName(u"rules_list")
        self.rules_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.rules_list.setDragDropMode(QAbstractItemView.InternalMove)

        self._3.addWidget(self.rules_list)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.dock_Widget_Contents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self._2 = QVBoxLayout(self.groupBox_2)
        self._2.setObjectName(u"_2")
        self.colors_list = MColor_list_Widget(self.groupBox_2)
        self.colors_list.setObjectName(u"colors_list")
        self.colors_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.colors_list.setDragDropMode(QAbstractItemView.InternalMove)

        self._2.addWidget(self.colors_list)


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
        self.file_menu = QMenu(self.menuBar)
        self.file_menu.setObjectName(u"file_menu")
        self.menu_3 = QMenu(self.file_menu)
        self.menu_3.setObjectName(u"menu_3")
        self.about_menu = QMenu(self.menuBar)
        self.about_menu.setObjectName(u"about_menu")
        MainWindow.setMenuBar(self.menuBar)
        self.tool_Bar = QToolBar(MainWindow)
        self.tool_Bar.setObjectName(u"tool_Bar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.tool_Bar)

        self.menuBar.addAction(self.file_menu.menuAction())
        self.menuBar.addAction(self.about_menu.menuAction())
        self.file_menu.addAction(self.action_new_file)
        self.file_menu.addAction(self.action_open_file)
        self.file_menu.addAction(self.menu_3.menuAction())
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.action_save_file)
        self.file_menu.addAction(self.action_save_file_as)
        self.file_menu.addAction(self.action_save_image)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.action_escape)
        self.about_menu.addAction(self.action_about_Qt)
        self.tool_Bar.addAction(self.action_new_file_2)
        self.tool_Bar.addAction(self.action_open_file_2)
        self.tool_Bar.addAction(self.action_save_file_2)

        self.retranslateUi(MainWindow)
        self.rules_list.customContextMenuRequested.connect(self.rules_list.show_menu)
        self.colors_list.customContextMenuRequested.connect(self.colors_list.show_menu)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_open_file.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.action_save_file.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.action_save_file_as.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a...", None))
        self.action_save_image.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u043d\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.action_escape.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.action_about_Qt.setText(QCoreApplication.translate("MainWindow", u"\u041e Qt", None))
        self.action_new_file.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439", None))
        self.action_new_file_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0444\u0430\u0439\u043b", None))
#if QT_CONFIG(tooltip)
        self.action_new_file_2.setToolTip(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0444\u0430\u0439\u043b", None))
#endif // QT_CONFIG(tooltip)
        self.action_open_file_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b", None))
#if QT_CONFIG(tooltip)
        self.action_open_file_2.setToolTip(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b", None))
#endif // QT_CONFIG(tooltip)
        self.action_save_file_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.action_save_file_2.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.label_line_width.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0443\u0431\u0438\u043d\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u043d\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043e\u043b \u043f\u043e\u0432\u043e\u0440\u043e\u0442\u0430", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435 \u0434\u043b\u0438\u043d\u043d\u044b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u0430", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0441\u0438\u043e\u043c\u0430", None))
        self.text_editing.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u0438\u043b\u0430", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442\u0430", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043f", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.file_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0434\u0430\u0432\u043d\u043e \u043e\u0442\u043a\u0440\u044b\u0442\u044b\u0435", None))
        self.about_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.tool_Bar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

