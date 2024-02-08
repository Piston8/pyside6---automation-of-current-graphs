# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_2uUgxQY.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QDoubleSpinBox, QFrame,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)
from . import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1006, 600)
        self.exit_action = QAction(MainWindow)
        self.exit_action.setObjectName(u"exit_action")
        icon = QIcon()
        icon.addFile(u":/icons_feather/icons/icons_feather/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_action.setIcon(icon)
        self.about_qt_action = QAction(MainWindow)
        self.about_qt_action.setObjectName(u"about_qt_action")
        self.about_author_action = QAction(MainWindow)
        self.about_author_action.setObjectName(u"about_author_action")
        self.initial_data_action = QAction(MainWindow)
        self.initial_data_action.setObjectName(u"initial_data_action")
        self.initial_data_action.setChecked(False)
        self.table_action = QAction(MainWindow)
        self.table_action.setObjectName(u"table_action")
        self.table_action.setChecked(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.phases_tabWidget = QTabWidget(self.centralwidget)
        self.phases_tabWidget.setObjectName(u"phases_tabWidget")
        self.base_tab = QWidget()
        self.base_tab.setObjectName(u"base_tab")
        self.verticalLayout_6 = QVBoxLayout(self.base_tab)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.base_tabWidget = QTabWidget(self.base_tab)
        self.base_tabWidget.setObjectName(u"base_tabWidget")
        self.base_tab_1 = QWidget()
        self.base_tab_1.setObjectName(u"base_tab_1")
        self.verticalLayout_9 = QVBoxLayout(self.base_tab_1)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.info_label_1 = QLabel(self.base_tab_1)
        self.info_label_1.setObjectName(u"info_label_1")
        self.info_label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.info_label_1)

        self.base_tabWidget.addTab(self.base_tab_1, "")
        self.base_tab_2 = QWidget()
        self.base_tab_2.setObjectName(u"base_tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.base_tab_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.info_label_2 = QLabel(self.base_tab_2)
        self.info_label_2.setObjectName(u"info_label_2")
        self.info_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.info_label_2)

        self.base_tabWidget.addTab(self.base_tab_2, "")
        self.base_tab_3 = QWidget()
        self.base_tab_3.setObjectName(u"base_tab_3")
        self.verticalLayout_7 = QVBoxLayout(self.base_tab_3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.info_label_3 = QLabel(self.base_tab_3)
        self.info_label_3.setObjectName(u"info_label_3")
        self.info_label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.info_label_3)

        self.base_tabWidget.addTab(self.base_tab_3, "")

        self.verticalLayout_6.addWidget(self.base_tabWidget)

        self.phases_tabWidget.addTab(self.base_tab, "")
        self.main_tab = QWidget()
        self.main_tab.setObjectName(u"main_tab")
        self.verticalLayout_2 = QVBoxLayout(self.main_tab)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_tabWidget = QTabWidget(self.main_tab)
        self.main_tabWidget.setObjectName(u"main_tabWidget")
        self.main_tab_1 = QWidget()
        self.main_tab_1.setObjectName(u"main_tab_1")
        self.verticalLayout_10 = QVBoxLayout(self.main_tab_1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.info_label_4 = QLabel(self.main_tab_1)
        self.info_label_4.setObjectName(u"info_label_4")
        self.info_label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.info_label_4)

        self.main_tabWidget.addTab(self.main_tab_1, "")
        self.main_tab_2 = QWidget()
        self.main_tab_2.setObjectName(u"main_tab_2")
        self.verticalLayout_11 = QVBoxLayout(self.main_tab_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.info_label_5 = QLabel(self.main_tab_2)
        self.info_label_5.setObjectName(u"info_label_5")
        self.info_label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.info_label_5)

        self.main_tabWidget.addTab(self.main_tab_2, "")
        self.main_tab_3 = QWidget()
        self.main_tab_3.setObjectName(u"main_tab_3")
        self.verticalLayout_12 = QVBoxLayout(self.main_tab_3)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.info_label_6 = QLabel(self.main_tab_3)
        self.info_label_6.setObjectName(u"info_label_6")
        self.info_label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.info_label_6)

        self.main_tabWidget.addTab(self.main_tab_3, "")

        self.verticalLayout_2.addWidget(self.main_tabWidget)

        self.phases_tabWidget.addTab(self.main_tab, "")
        self.time_tab = QWidget()
        self.time_tab.setObjectName(u"time_tab")
        self.verticalLayout_3 = QVBoxLayout(self.time_tab)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.time_tabWidget = QTabWidget(self.time_tab)
        self.time_tabWidget.setObjectName(u"time_tabWidget")
        self.time_tab_1 = QWidget()
        self.time_tab_1.setObjectName(u"time_tab_1")
        self.verticalLayout_13 = QVBoxLayout(self.time_tab_1)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.info_label_7 = QLabel(self.time_tab_1)
        self.info_label_7.setObjectName(u"info_label_7")
        self.info_label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.info_label_7)

        self.time_tabWidget.addTab(self.time_tab_1, "")
        self.time_tab_2 = QWidget()
        self.time_tab_2.setObjectName(u"time_tab_2")
        self.verticalLayout_14 = QVBoxLayout(self.time_tab_2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.info_label_8 = QLabel(self.time_tab_2)
        self.info_label_8.setObjectName(u"info_label_8")
        self.info_label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.info_label_8)

        self.time_tabWidget.addTab(self.time_tab_2, "")
        self.time_tab_3 = QWidget()
        self.time_tab_3.setObjectName(u"time_tab_3")
        self.verticalLayout_15 = QVBoxLayout(self.time_tab_3)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.info_label_9 = QLabel(self.time_tab_3)
        self.info_label_9.setObjectName(u"info_label_9")
        self.info_label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.info_label_9)

        self.time_tabWidget.addTab(self.time_tab_3, "")

        self.verticalLayout_3.addWidget(self.time_tabWidget)

        self.phases_tabWidget.addTab(self.time_tab, "")
        self.modulation_tab = QWidget()
        self.modulation_tab.setObjectName(u"modulation_tab")
        self.verticalLayout_4 = QVBoxLayout(self.modulation_tab)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.modulation_tabWidget = QTabWidget(self.modulation_tab)
        self.modulation_tabWidget.setObjectName(u"modulation_tabWidget")
        self.modulation_tab_1 = QWidget()
        self.modulation_tab_1.setObjectName(u"modulation_tab_1")
        self.verticalLayout_16 = QVBoxLayout(self.modulation_tab_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.info_label_10 = QLabel(self.modulation_tab_1)
        self.info_label_10.setObjectName(u"info_label_10")
        self.info_label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.info_label_10)

        self.modulation_tabWidget.addTab(self.modulation_tab_1, "")
        self.modulation_tab_2 = QWidget()
        self.modulation_tab_2.setObjectName(u"modulation_tab_2")
        self.verticalLayout_17 = QVBoxLayout(self.modulation_tab_2)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.info_label_11 = QLabel(self.modulation_tab_2)
        self.info_label_11.setObjectName(u"info_label_11")
        self.info_label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.info_label_11)

        self.modulation_tabWidget.addTab(self.modulation_tab_2, "")
        self.modulation_tab_3 = QWidget()
        self.modulation_tab_3.setObjectName(u"modulation_tab_3")
        self.verticalLayout_18 = QVBoxLayout(self.modulation_tab_3)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.info_label_12 = QLabel(self.modulation_tab_3)
        self.info_label_12.setObjectName(u"info_label_12")
        self.info_label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.info_label_12)

        self.modulation_tabWidget.addTab(self.modulation_tab_3, "")

        self.verticalLayout_4.addWidget(self.modulation_tabWidget)

        self.phases_tabWidget.addTab(self.modulation_tab, "")
        self.phase_tab = QWidget()
        self.phase_tab.setObjectName(u"phase_tab")
        self.verticalLayout_22 = QVBoxLayout(self.phase_tab)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.phase_tabWidget = QTabWidget(self.phase_tab)
        self.phase_tabWidget.setObjectName(u"phase_tabWidget")
        self.phase_tab_1 = QWidget()
        self.phase_tab_1.setObjectName(u"phase_tab_1")
        self.verticalLayout_19 = QVBoxLayout(self.phase_tab_1)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.info_label_13 = QLabel(self.phase_tab_1)
        self.info_label_13.setObjectName(u"info_label_13")
        self.info_label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.info_label_13)

        self.phase_tabWidget.addTab(self.phase_tab_1, "")
        self.phase_tab_2 = QWidget()
        self.phase_tab_2.setObjectName(u"phase_tab_2")
        self.verticalLayout_20 = QVBoxLayout(self.phase_tab_2)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.info_label_14 = QLabel(self.phase_tab_2)
        self.info_label_14.setObjectName(u"info_label_14")
        self.info_label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.info_label_14)

        self.phase_tabWidget.addTab(self.phase_tab_2, "")
        self.phase_tab_3 = QWidget()
        self.phase_tab_3.setObjectName(u"phase_tab_3")
        self.verticalLayout_21 = QVBoxLayout(self.phase_tab_3)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.info_label_15 = QLabel(self.phase_tab_3)
        self.info_label_15.setObjectName(u"info_label_15")
        self.info_label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.info_label_15)

        self.phase_tabWidget.addTab(self.phase_tab_3, "")

        self.verticalLayout_22.addWidget(self.phase_tabWidget)

        self.phases_tabWidget.addTab(self.phase_tab, "")

        self.verticalLayout.addWidget(self.phases_tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1006, 22))
        self.file_menu = QMenu(self.menubar)
        self.file_menu.setObjectName(u"file_menu")
        self.help_menu = QMenu(self.menubar)
        self.help_menu.setObjectName(u"help_menu")
        self.view_menu = QMenu(self.menubar)
        self.view_menu.setObjectName(u"view_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.initial_data_dockWidget = QDockWidget(MainWindow)
        self.initial_data_dockWidget.setObjectName(u"initial_data_dockWidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.initial_data_dockWidget.sizePolicy().hasHeightForWidth())
        self.initial_data_dockWidget.setSizePolicy(sizePolicy)
        self.initial_data_dockWidgetContents = QWidget()
        self.initial_data_dockWidgetContents.setObjectName(u"initial_data_dockWidgetContents")
        sizePolicy.setHeightForWidth(self.initial_data_dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.initial_data_dockWidgetContents.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.initial_data_dockWidgetContents)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.files_groupBox = QGroupBox(self.initial_data_dockWidgetContents)
        self.files_groupBox.setObjectName(u"files_groupBox")
        self.gridLayout_3 = QGridLayout(self.files_groupBox)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.file_1_lineEdit = QLineEdit(self.files_groupBox)
        self.file_1_lineEdit.setObjectName(u"file_1_lineEdit")

        self.gridLayout_3.addWidget(self.file_1_lineEdit, 0, 0, 1, 1)

        self.file_1_pushButton = QPushButton(self.files_groupBox)
        self.file_1_pushButton.setObjectName(u"file_1_pushButton")
        self.file_1_pushButton.setMinimumSize(QSize(30, 0))
        self.file_1_pushButton.setMaximumSize(QSize(30, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icons_feather/icons/icons_feather/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.file_1_pushButton.setIcon(icon1)

        self.gridLayout_3.addWidget(self.file_1_pushButton, 0, 1, 1, 1)

        self.file_2_lineEdit = QLineEdit(self.files_groupBox)
        self.file_2_lineEdit.setObjectName(u"file_2_lineEdit")

        self.gridLayout_3.addWidget(self.file_2_lineEdit, 1, 0, 1, 1)

        self.file_2_pushButton = QPushButton(self.files_groupBox)
        self.file_2_pushButton.setObjectName(u"file_2_pushButton")
        self.file_2_pushButton.setMinimumSize(QSize(30, 0))
        self.file_2_pushButton.setMaximumSize(QSize(30, 16777215))
        self.file_2_pushButton.setIcon(icon1)

        self.gridLayout_3.addWidget(self.file_2_pushButton, 1, 1, 1, 1)

        self.file_3_lineEdit = QLineEdit(self.files_groupBox)
        self.file_3_lineEdit.setObjectName(u"file_3_lineEdit")

        self.gridLayout_3.addWidget(self.file_3_lineEdit, 2, 0, 1, 1)

        self.file_3_pushButton = QPushButton(self.files_groupBox)
        self.file_3_pushButton.setObjectName(u"file_3_pushButton")
        self.file_3_pushButton.setMinimumSize(QSize(30, 0))
        self.file_3_pushButton.setMaximumSize(QSize(30, 16777215))
        self.file_3_pushButton.setIcon(icon1)

        self.gridLayout_3.addWidget(self.file_3_pushButton, 2, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.files_groupBox)

        self.data_groupBox = QGroupBox(self.initial_data_dockWidgetContents)
        self.data_groupBox.setObjectName(u"data_groupBox")
        self.gridLayout_2 = QGridLayout(self.data_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(2)
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.data_label_1_1 = QLabel(self.data_groupBox)
        self.data_label_1_1.setObjectName(u"data_label_1_1")
        self.data_label_1_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.data_label_1_1, 0, 1, 1, 1)

        self.data_label_1_2 = QLabel(self.data_groupBox)
        self.data_label_1_2.setObjectName(u"data_label_1_2")
        self.data_label_1_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.data_label_1_2, 0, 2, 1, 1)

        self.data_label_2_1 = QLabel(self.data_groupBox)
        self.data_label_2_1.setObjectName(u"data_label_2_1")

        self.gridLayout_2.addWidget(self.data_label_2_1, 1, 0, 1, 1)

        self.data_lineEdit_1_1 = QLineEdit(self.data_groupBox)
        self.data_lineEdit_1_1.setObjectName(u"data_lineEdit_1_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.data_lineEdit_1_1.sizePolicy().hasHeightForWidth())
        self.data_lineEdit_1_1.setSizePolicy(sizePolicy1)
        self.data_lineEdit_1_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.data_lineEdit_1_1, 1, 1, 1, 1)

        self.data_lineEdit_1_2 = QLineEdit(self.data_groupBox)
        self.data_lineEdit_1_2.setObjectName(u"data_lineEdit_1_2")
        sizePolicy1.setHeightForWidth(self.data_lineEdit_1_2.sizePolicy().hasHeightForWidth())
        self.data_lineEdit_1_2.setSizePolicy(sizePolicy1)
        self.data_lineEdit_1_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.data_lineEdit_1_2, 1, 2, 1, 1)

        self.data_label_2_2 = QLabel(self.data_groupBox)
        self.data_label_2_2.setObjectName(u"data_label_2_2")

        self.gridLayout_2.addWidget(self.data_label_2_2, 2, 0, 1, 1)

        self.data_lineEdit_2_1 = QLineEdit(self.data_groupBox)
        self.data_lineEdit_2_1.setObjectName(u"data_lineEdit_2_1")
        sizePolicy1.setHeightForWidth(self.data_lineEdit_2_1.sizePolicy().hasHeightForWidth())
        self.data_lineEdit_2_1.setSizePolicy(sizePolicy1)
        self.data_lineEdit_2_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.data_lineEdit_2_1, 2, 1, 1, 1)

        self.data_lineEdit_2_2 = QLineEdit(self.data_groupBox)
        self.data_lineEdit_2_2.setObjectName(u"data_lineEdit_2_2")
        sizePolicy1.setHeightForWidth(self.data_lineEdit_2_2.sizePolicy().hasHeightForWidth())
        self.data_lineEdit_2_2.setSizePolicy(sizePolicy1)
        self.data_lineEdit_2_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.data_lineEdit_2_2, 2, 2, 1, 1)


        self.verticalLayout_5.addWidget(self.data_groupBox)

        self.correction_groupBox = QGroupBox(self.initial_data_dockWidgetContents)
        self.correction_groupBox.setObjectName(u"correction_groupBox")
        self.gridLayout = QGridLayout(self.correction_groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.correction_doubleSpinBox = QDoubleSpinBox(self.correction_groupBox)
        self.correction_doubleSpinBox.setObjectName(u"correction_doubleSpinBox")
        self.correction_doubleSpinBox.setMaximum(2.000000000000000)
        self.correction_doubleSpinBox.setSingleStep(0.010000000000000)

        self.gridLayout.addWidget(self.correction_doubleSpinBox, 0, 1, 1, 1)

        self.reset_correction_pushButton = QPushButton(self.correction_groupBox)
        self.reset_correction_pushButton.setObjectName(u"reset_correction_pushButton")

        self.gridLayout.addWidget(self.reset_correction_pushButton, 0, 2, 1, 1)

        self.correction_title_label = QLabel(self.correction_groupBox)
        self.correction_title_label.setObjectName(u"correction_title_label")

        self.gridLayout.addWidget(self.correction_title_label, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.correction_groupBox)

        self.plot_pushButton = QPushButton(self.initial_data_dockWidgetContents)
        self.plot_pushButton.setObjectName(u"plot_pushButton")
        self.plot_pushButton.setEnabled(False)

        self.verticalLayout_5.addWidget(self.plot_pushButton)

        self.initial_data_verticalSpacer = QSpacerItem(20, 153, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.initial_data_verticalSpacer)

        self.initial_data_dockWidget.setWidget(self.initial_data_dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.initial_data_dockWidget)
        self.table_dockWidget = QDockWidget(MainWindow)
        self.table_dockWidget.setObjectName(u"table_dockWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.table_dockWidget.sizePolicy().hasHeightForWidth())
        self.table_dockWidget.setSizePolicy(sizePolicy2)
        self.table_dockWidgetContents = QWidget()
        self.table_dockWidgetContents.setObjectName(u"table_dockWidgetContents")
        sizePolicy2.setHeightForWidth(self.table_dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.table_dockWidgetContents.setSizePolicy(sizePolicy2)
        self.gridLayout_4 = QGridLayout(self.table_dockWidgetContents)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.line_6 = QFrame(self.table_dockWidgetContents)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_6, 1, 0, 1, 3)

        self.i1_rab_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.i1_rab_lineEdit.setObjectName(u"i1_rab_lineEdit")
        self.i1_rab_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.i1_rab_lineEdit, 3, 8, 1, 1)

        self.tp_time_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.tp_time_lineEdit.setObjectName(u"tp_time_lineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tp_time_lineEdit.sizePolicy().hasHeightForWidth())
        self.tp_time_lineEdit.setSizePolicy(sizePolicy3)
        self.tp_time_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.tp_time_lineEdit, 4, 1, 2, 2)

        self.isr_rab_title_label = QLabel(self.table_dockWidgetContents)
        self.isr_rab_title_label.setObjectName(u"isr_rab_title_label")
        self.isr_rab_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.isr_rab_title_label, 4, 8, 1, 1)

        self.razg_time_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.razg_time_lineEdit.setObjectName(u"razg_time_lineEdit")
        self.razg_time_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.razg_time_lineEdit, 3, 2, 1, 1)

        self.line_4 = QFrame(self.table_dockWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_4, 0, 13, 6, 1)

        self.table_verticalSpacer = QSpacerItem(818, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.table_verticalSpacer, 6, 0, 1, 20)

        self.i2_rab_title_label = QLabel(self.table_dockWidgetContents)
        self.i2_rab_title_label.setObjectName(u"i2_rab_title_label")
        self.i2_rab_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.i2_rab_title_label, 2, 9, 1, 1)

        self.i3_rab_title_label = QLabel(self.table_dockWidgetContents)
        self.i3_rab_title_label.setObjectName(u"i3_rab_title_label")
        self.i3_rab_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.i3_rab_title_label, 2, 10, 1, 1)

        self.tp_time_title_label = QLabel(self.table_dockWidgetContents)
        self.tp_time_title_label.setObjectName(u"tp_time_title_label")
        self.tp_time_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.tp_time_title_label, 4, 0, 2, 1)

        self.razg_time_title_label = QLabel(self.table_dockWidgetContents)
        self.razg_time_title_label.setObjectName(u"razg_time_title_label")
        self.razg_time_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.razg_time_title_label, 2, 2, 1, 1)

        self.current_title_label = QLabel(self.table_dockWidgetContents)
        self.current_title_label.setObjectName(u"current_title_label")
        self.current_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.current_title_label, 0, 4, 1, 7)

        self.line_5 = QFrame(self.table_dockWidgetContents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_5, 0, 17, 6, 1)

        self.time_title_label = QLabel(self.table_dockWidgetContents)
        self.time_title_label.setObjectName(u"time_title_label")
        self.time_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.time_title_label, 0, 0, 1, 3)

        self.mod2_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.mod2_lineEdit.setObjectName(u"mod2_lineEdit")
        self.mod2_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.mod2_lineEdit, 3, 15, 1, 1)

        self.mod2_title_label = QLabel(self.table_dockWidgetContents)
        self.mod2_title_label.setObjectName(u"mod2_title_label")
        self.mod2_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.mod2_title_label, 2, 15, 1, 1)

        self.i3_rab_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.i3_rab_lineEdit.setObjectName(u"i3_rab_lineEdit")
        self.i3_rab_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.i3_rab_lineEdit, 3, 10, 1, 1)

        self.sigma_mod_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.sigma_mod_lineEdit.setObjectName(u"sigma_mod_lineEdit")
        self.sigma_mod_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.sigma_mod_lineEdit, 5, 15, 1, 2)

        self.sigma_rab_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.sigma_rab_lineEdit.setObjectName(u"sigma_rab_lineEdit")
        self.sigma_rab_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.sigma_rab_lineEdit, 5, 9, 1, 2)

        self.sigma_mod_title_label = QLabel(self.table_dockWidgetContents)
        self.sigma_mod_title_label.setObjectName(u"sigma_mod_title_label")
        self.sigma_mod_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.sigma_mod_title_label, 5, 14, 1, 1)

        self.isr_pusk_title_label = QLabel(self.table_dockWidgetContents)
        self.isr_pusk_title_label.setObjectName(u"isr_pusk_title_label")
        self.isr_pusk_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.isr_pusk_title_label, 4, 4, 1, 1)

        self.i2_rab_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.i2_rab_lineEdit.setObjectName(u"i2_rab_lineEdit")
        self.i2_rab_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.i2_rab_lineEdit, 3, 9, 1, 1)

        self.spectr_d_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.spectr_d_lineEdit.setObjectName(u"spectr_d_lineEdit")
        sizePolicy3.setHeightForWidth(self.spectr_d_lineEdit.sizePolicy().hasHeightForWidth())
        self.spectr_d_lineEdit.setSizePolicy(sizePolicy3)
        self.spectr_d_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.spectr_d_lineEdit, 3, 18, 3, 1)

        self.line_2 = QFrame(self.table_dockWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 2, 7, 4, 1)

        self.sigma_pusk_title_label = QLabel(self.table_dockWidgetContents)
        self.sigma_pusk_title_label.setObjectName(u"sigma_pusk_title_label")
        self.sigma_pusk_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.sigma_pusk_title_label, 5, 4, 1, 1)

        self.line_3 = QFrame(self.table_dockWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 2, 11, 4, 1)

        self.mod_sr_title_label = QLabel(self.table_dockWidgetContents)
        self.mod_sr_title_label.setObjectName(u"mod_sr_title_label")
        self.mod_sr_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.mod_sr_title_label, 4, 14, 1, 1)

        self.isr_rab_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.isr_rab_lineEdit.setObjectName(u"isr_rab_lineEdit")
        self.isr_rab_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.isr_rab_lineEdit, 4, 9, 1, 2)

        self.spectr_d_title_label = QLabel(self.table_dockWidgetContents)
        self.spectr_d_title_label.setObjectName(u"spectr_d_title_label")
        self.spectr_d_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.spectr_d_title_label, 2, 18, 1, 1)

        self.i3_pusk_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.i3_pusk_lineEdit.setObjectName(u"i3_pusk_lineEdit")
        self.i3_pusk_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.i3_pusk_lineEdit, 3, 6, 1, 1)

        self.modulation_title_label = QLabel(self.table_dockWidgetContents)
        self.modulation_title_label.setObjectName(u"modulation_title_label")
        self.modulation_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.modulation_title_label, 0, 14, 1, 3)

        self.spectrum_title_label = QLabel(self.table_dockWidgetContents)
        self.spectrum_title_label.setObjectName(u"spectrum_title_label")
        self.spectrum_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.spectrum_title_label, 0, 18, 1, 2)

        self.isr_pusk_isr_rab_ititle_label = QLabel(self.table_dockWidgetContents)
        self.isr_pusk_isr_rab_ititle_label.setObjectName(u"isr_pusk_isr_rab_ititle_label")
        self.isr_pusk_isr_rab_ititle_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.isr_pusk_isr_rab_ititle_label, 2, 12, 1, 1)

        self.act_time_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.act_time_lineEdit.setObjectName(u"act_time_lineEdit")
        self.act_time_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.act_time_lineEdit, 3, 0, 1, 1)

        self.sigma_pusk_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.sigma_pusk_lineEdit.setObjectName(u"sigma_pusk_lineEdit")
        self.sigma_pusk_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.sigma_pusk_lineEdit, 5, 5, 1, 2)

        self.i1_rab_title_label = QLabel(self.table_dockWidgetContents)
        self.i1_rab_title_label.setObjectName(u"i1_rab_title_label")
        self.i1_rab_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.i1_rab_title_label, 2, 8, 1, 1)

        self.isr_pusk_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.isr_pusk_lineEdit.setObjectName(u"isr_pusk_lineEdit")
        self.isr_pusk_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.isr_pusk_lineEdit, 4, 5, 1, 2)

        self.i2_pusk_title_label = QLabel(self.table_dockWidgetContents)
        self.i2_pusk_title_label.setObjectName(u"i2_pusk_title_label")
        self.i2_pusk_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.i2_pusk_title_label, 2, 5, 1, 1)

        self.mod1_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.mod1_lineEdit.setObjectName(u"mod1_lineEdit")
        self.mod1_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.mod1_lineEdit, 3, 14, 1, 1)

        self.spectr_v_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.spectr_v_lineEdit.setObjectName(u"spectr_v_lineEdit")
        sizePolicy3.setHeightForWidth(self.spectr_v_lineEdit.sizePolicy().hasHeightForWidth())
        self.spectr_v_lineEdit.setSizePolicy(sizePolicy3)
        self.spectr_v_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.spectr_v_lineEdit, 3, 19, 3, 1)

        self.i2_pusk_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.i2_pusk_lineEdit.setObjectName(u"i2_pusk_lineEdit")
        self.i2_pusk_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.i2_pusk_lineEdit, 3, 5, 1, 1)

        self.line = QFrame(self.table_dockWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 0, 3, 6, 1)

        self.i3_pusk_title_label = QLabel(self.table_dockWidgetContents)
        self.i3_pusk_title_label.setObjectName(u"i3_pusk_title_label")
        self.i3_pusk_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.i3_pusk_title_label, 2, 6, 1, 1)

        self.i1_pusk_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.i1_pusk_lineEdit.setObjectName(u"i1_pusk_lineEdit")
        self.i1_pusk_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.i1_pusk_lineEdit, 3, 4, 1, 1)

        self.str_time_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.str_time_lineEdit.setObjectName(u"str_time_lineEdit")
        self.str_time_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.str_time_lineEdit, 3, 1, 1, 1)

        self.mod_sr_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.mod_sr_lineEdit.setObjectName(u"mod_sr_lineEdit")
        self.mod_sr_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.mod_sr_lineEdit, 4, 15, 1, 2)

        self.line_9 = QFrame(self.table_dockWidgetContents)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_9, 1, 18, 1, 2)

        self.sigma_rab_title_label = QLabel(self.table_dockWidgetContents)
        self.sigma_rab_title_label.setObjectName(u"sigma_rab_title_label")
        self.sigma_rab_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.sigma_rab_title_label, 5, 8, 1, 1)

        self.mod3_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.mod3_lineEdit.setObjectName(u"mod3_lineEdit")
        self.mod3_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.mod3_lineEdit, 3, 16, 1, 1)

        self.i1_pusk_title_label = QLabel(self.table_dockWidgetContents)
        self.i1_pusk_title_label.setObjectName(u"i1_pusk_title_label")
        self.i1_pusk_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.i1_pusk_title_label, 2, 4, 1, 1)

        self.mod1_title_label = QLabel(self.table_dockWidgetContents)
        self.mod1_title_label.setObjectName(u"mod1_title_label")
        self.mod1_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.mod1_title_label, 2, 14, 1, 1)

        self.line_7 = QFrame(self.table_dockWidgetContents)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_7, 1, 4, 1, 9)

        self.str_time_title_label = QLabel(self.table_dockWidgetContents)
        self.str_time_title_label.setObjectName(u"str_time_title_label")
        self.str_time_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.str_time_title_label, 2, 1, 1, 1)

        self.mod3_title_label = QLabel(self.table_dockWidgetContents)
        self.mod3_title_label.setObjectName(u"mod3_title_label")
        self.mod3_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.mod3_title_label, 2, 16, 1, 1)

        self.line_8 = QFrame(self.table_dockWidgetContents)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_8, 1, 14, 1, 3)

        self.isr_pusk_isr_rab_lineEdit = QLineEdit(self.table_dockWidgetContents)
        self.isr_pusk_isr_rab_lineEdit.setObjectName(u"isr_pusk_isr_rab_lineEdit")
        sizePolicy3.setHeightForWidth(self.isr_pusk_isr_rab_lineEdit.sizePolicy().hasHeightForWidth())
        self.isr_pusk_isr_rab_lineEdit.setSizePolicy(sizePolicy3)
        self.isr_pusk_isr_rab_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.isr_pusk_isr_rab_lineEdit, 3, 12, 3, 1)

        self.spectr_v_title_label = QLabel(self.table_dockWidgetContents)
        self.spectr_v_title_label.setObjectName(u"spectr_v_title_label")
        self.spectr_v_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.spectr_v_title_label, 2, 19, 1, 1)

        self.act_time_title_label = QLabel(self.table_dockWidgetContents)
        self.act_time_title_label.setObjectName(u"act_time_title_label")
        self.act_time_title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.act_time_title_label, 2, 0, 1, 1)

        self.table_dockWidget.setWidget(self.table_dockWidgetContents)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.table_dockWidget)

        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.view_menu.menuAction())
        self.menubar.addAction(self.help_menu.menuAction())
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.exit_action)
        self.help_menu.addAction(self.about_qt_action)
        self.view_menu.addAction(self.initial_data_action)
        self.view_menu.addAction(self.table_action)

        self.retranslateUi(MainWindow)
        self.exit_action.triggered.connect(MainWindow.close)
        self.initial_data_action.triggered.connect(self.initial_data_dockWidget.show)
        self.table_action.triggered.connect(self.table_dockWidget.show)

        self.phases_tabWidget.setCurrentIndex(0)
        self.base_tabWidget.setCurrentIndex(0)
        self.main_tabWidget.setCurrentIndex(0)
        self.time_tabWidget.setCurrentIndex(0)
        self.modulation_tabWidget.setCurrentIndex(0)
        self.phase_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.exit_action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
#if QT_CONFIG(shortcut)
        self.exit_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.about_qt_action.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.about_author_action.setText(QCoreApplication.translate("MainWindow", u"About Author", None))
        self.initial_data_action.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.table_action.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430", None))
        self.info_label_1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u044c \u0434\u0430\u043d\u043d\u044b\u0435\n"
"\u041d\u0430\u0436\u043c\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.base_tabWidget.setTabText(self.base_tabWidget.indexOf(self.base_tab_1), QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u0430 \"A\"", None))
        self.info_label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u044c \u0434\u0430\u043d\u043d\u044b\u0435\n"
"\u041d\u0430\u0436\u043c\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.base_tabWidget.setTabText(self.base_tabWidget.indexOf(self.base_tab_2), QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u0430 \"B\"", None))
        self.info_label_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u044c \u0434\u0430\u043d\u043d\u044b\u0435\n"
"\u041d\u0430\u0436\u043c\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.base_tabWidget.setTabText(self.base_tabWidget.indexOf(self.base_tab_3), QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u0430 \"C\"", None))
        self.phases_tabWidget.setTabText(self.phases_tabWidget.indexOf(self.base_tab), QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u043e\u0432\u044b\u0439", None))
        self.info_label_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u044c \u0434\u0430\u043d\u043d\u044b\u0435\n"
"\u041d\u0430\u0436\u043c\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.main_tab_1), QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u0430 \"A\"", None))
        self.info_label_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u044c \u0434\u0430\u043d\u043d\u044b\u0435\n"
"\u041d\u0430\u0436\u043c\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.main_tab_2), QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u0430 \"B\"", None))
        self.info_label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u044c \u0434\u0430\u043d\u043d\u044b\u0435\n"
"\u041d\u0430\u0436\u043c\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.main_tab_3), QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u0430 \"C\"", None))
        self.phases_tabWidget.setTabText(self.phases_tabWidget.indexOf(self.main_tab), QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439", None))
        self.info_label_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u044c \u0434\u0430\u043d\u043d\u044b\u0435\n"
"\u041d\u0430\u0436\u043c\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.time_tabWidget.setTabText(self.time_tabWidget.indexOf(self.time_tab_1), QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u0430 \"A\"", None))
        self.info_label_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u044c \u0434\u0430\u043d\u043d\u044b\u0435\n"
"\u041d\u0430\u0436\u043c\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.time_tabWidget.setTabText(self.time_tabWidget.indexOf(self.time_tab_2), QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u0430 \"B\"", None))
        self.info_label_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u044c \u0434\u0430\u043d\u043d\u044b\u0435\n"
"\u041d\u0430\u0436\u043c\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.time_tabWidget.setTabText(self.time_tabWidget.indexOf(self.time_tab_3), QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u0430 \"C\"", None))
        self.phases_tabWidget.setTabText(self.phases_tabWidget.indexOf(self.time_tab), QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f (\u0430\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u0438, \u0441\u0442\u0440\u0430\u0433\u0438\u0432\u0430\u043d\u0438\u044f, \u0440\u0430\u0437\u0433\u043e\u043d\u0430)", None))
        self.info_label_10.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u044c \u0434\u0430\u043d\u043d\u044b\u0435\n"
"\u041d\u0430\u0436\u043c\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.modulation_tabWidget.setTabText(self.modulation_tabWidget.indexOf(self.modulation_tab_1), QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u0430 \"A\"", None))
        self.info_label_11.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u044c \u0434\u0430\u043d\u043d\u044b\u0435\n"
"\u041d\u0430\u0436\u043c\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.modulation_tabWidget.setTabText(self.modulation_tabWidget.indexOf(self.modulation_tab_2), QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u0430 \"B\"", None))
        self.info_label_12.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u044c \u0434\u0430\u043d\u043d\u044b\u0435\n"
"\u041d\u0430\u0436\u043c\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.modulation_tabWidget.setTabText(self.modulation_tabWidget.indexOf(self.modulation_tab_3), QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u0430 \"C\"", None))
        self.phases_tabWidget.setTabText(self.phases_tabWidget.indexOf(self.modulation_tab), QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044f\u0446\u0438\u044f", None))
        self.info_label_13.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u044c \u0434\u0430\u043d\u043d\u044b\u0435\n"
"\u041d\u0430\u0436\u043c\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.phase_tabWidget.setTabText(self.phase_tabWidget.indexOf(self.phase_tab_1), QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u0430 \"A\"", None))
        self.info_label_14.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u044c \u0434\u0430\u043d\u043d\u044b\u0435\n"
"\u041d\u0430\u0436\u043c\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.phase_tabWidget.setTabText(self.phase_tabWidget.indexOf(self.phase_tab_2), QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u0430 \"B\"", None))
        self.info_label_15.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u044c \u0434\u0430\u043d\u043d\u044b\u0435\n"
"\u041d\u0430\u0436\u043c\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.phase_tabWidget.setTabText(self.phase_tabWidget.indexOf(self.phase_tab_3), QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u0430 \"C\"", None))
        self.phases_tabWidget.setTabText(self.phases_tabWidget.indexOf(self.phase_tab), QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0444\u0430\u0437\u044b", None))
        self.file_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.help_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.view_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434", None))
        self.initial_data_dockWidget.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.files_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b\u044b", None))
        self.file_1_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u0430 \"A\"", None))
        self.file_1_pushButton.setText("")
        self.file_2_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u0430 \"B\"", None))
        self.file_2_pushButton.setText("")
        self.file_3_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u0430 \"C\"", None))
        self.file_3_pushButton.setText("")
        self.data_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435", None))
        self.data_label_1_1.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e \u043e\u0431\u043e\u0440\u043e\u0442\u043e\u0432,\n"
"\u043e\u0431/\u043c\u0438\u043d ", None))
        self.data_label_1_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0448\u043a\u0438\u0432\u0430,\n"
"\u043c\u043c", None))
        self.data_label_2_1.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u043d\u0442\u0438\u043b\u044f\u0442\u043e\u0440", None))
        self.data_label_2_2.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c", None))
        self.correction_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0440\u0435\u043a\u0446\u0438\u044f", None))
        self.reset_correction_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.correction_title_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0440\u0435\u043a\u0446\u0438\u044f \u0432\u0445\u043e\u0434\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.plot_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.table_dockWidget.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430", None))
        self.isr_rab_title_label.setText(QCoreApplication.translate("MainWindow", u"I\u0440 \u0441\u0440", None))
        self.i2_rab_title_label.setText(QCoreApplication.translate("MainWindow", u"I\u0440B", None))
        self.i3_rab_title_label.setText(QCoreApplication.translate("MainWindow", u"I\u0440C", None))
        self.tp_time_title_label.setText(QCoreApplication.translate("MainWindow", u"t\u043f", None))
        self.razg_time_title_label.setText(QCoreApplication.translate("MainWindow", u"t\u0440\u0430\u0437\u0433", None))
        self.current_title_label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043a\u043e\u0432\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b, \u0410", None))
        self.time_title_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b, \u0441", None))
        self.mod2_title_label.setText(QCoreApplication.translate("MainWindow", u"mB", None))
        self.sigma_mod_title_label.setText(QCoreApplication.translate("MainWindow", u"\u03b4(m)", None))
        self.isr_pusk_title_label.setText(QCoreApplication.translate("MainWindow", u"I\u043f \u0441\u0440", None))
        self.sigma_pusk_title_label.setText(QCoreApplication.translate("MainWindow", u"\u03b4(I\u043f)", None))
        self.mod_sr_title_label.setText(QCoreApplication.translate("MainWindow", u"m\u0441\u0440", None))
        self.spectr_d_title_label.setText(QCoreApplication.translate("MainWindow", u"A(f.\u044d\u0434)", None))
        self.modulation_title_label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044f\u0446\u0438\u044f, %", None))
        self.spectrum_title_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0441\u043f\u0435\u043a\u0442\u0440\u0430, \u0434\u0411", None))
        self.isr_pusk_isr_rab_ititle_label.setText(QCoreApplication.translate("MainWindow", u"I\u043f\u0441\u0440/I\u0440\u0441\u0440", None))
        self.i1_rab_title_label.setText(QCoreApplication.translate("MainWindow", u"I\u0440A", None))
        self.i2_pusk_title_label.setText(QCoreApplication.translate("MainWindow", u"I\u043fB", None))
        self.i3_pusk_title_label.setText(QCoreApplication.translate("MainWindow", u"I\u043fC", None))
        self.sigma_rab_title_label.setText(QCoreApplication.translate("MainWindow", u"\u03b4(I\u0440)", None))
        self.i1_pusk_title_label.setText(QCoreApplication.translate("MainWindow", u"I\u043fA", None))
        self.mod1_title_label.setText(QCoreApplication.translate("MainWindow", u"mA", None))
        self.str_time_title_label.setText(QCoreApplication.translate("MainWindow", u"t\u0441\u0442\u0440", None))
        self.mod3_title_label.setText(QCoreApplication.translate("MainWindow", u"mC", None))
        self.spectr_v_title_label.setText(QCoreApplication.translate("MainWindow", u"A(f.\u0432)", None))
        self.act_time_title_label.setText(QCoreApplication.translate("MainWindow", u"t\u0430\u043a\u0442", None))
    # retranslateUi

