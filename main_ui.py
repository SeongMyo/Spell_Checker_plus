# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spell_check_windowSCTysM.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 797)
        icon = QIcon()
        icon.addFile(u":/icon/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_original = QLabel(self.centralwidget)
        self.label_original.setObjectName(u"label_original")
        font = QFont()
        font.setFamilies([u"\ub098\ub214\uc2a4\ud018\uc5b4\ub77c\uc6b4\ub4dc ExtraBold"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_original.setFont(font)

        self.gridLayout.addWidget(self.label_original, 3, 0, 1, 1)

        self.label_checked = QLabel(self.centralwidget)
        self.label_checked.setObjectName(u"label_checked")
        self.label_checked.setFont(font)

        self.gridLayout.addWidget(self.label_checked, 3, 2, 1, 1)

        self.input_text = QPlainTextEdit(self.centralwidget)
        self.input_text.setObjectName(u"input_text")
        self.input_text.setMinimumSize(QSize(250, 450))
        font1 = QFont()
        font1.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        self.input_text.setFont(font1)

        self.gridLayout.addWidget(self.input_text, 4, 0, 1, 2)

        self.output_text = QTextBrowser(self.centralwidget)
        self.output_text.setObjectName(u"output_text")
        self.output_text.setMinimumSize(QSize(250, 450))
        self.output_text.setFont(font1)

        self.gridLayout.addWidget(self.output_text, 4, 2, 1, 2)

        self.pushButton_check = QPushButton(self.centralwidget)
        self.pushButton_check.setObjectName(u"pushButton_check")

        self.gridLayout.addWidget(self.pushButton_check, 2, 1, 1, 1)

        self.pushButton_reset = QPushButton(self.centralwidget)
        self.pushButton_reset.setObjectName(u"pushButton_reset")

        self.gridLayout.addWidget(self.pushButton_reset, 2, 2, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_cat_2_color = QLabel(self.centralwidget)
        self.label_cat_2_color.setObjectName(u"label_cat_2_color")
        self.label_cat_2_color.setStyleSheet(u"color:#00CC00")
        self.label_cat_2_color.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_cat_2_color, 1, 0, 1, 1)

        self.label_cat_3_title = QLabel(self.centralwidget)
        self.label_cat_3_title.setObjectName(u"label_cat_3_title")

        self.gridLayout_2.addWidget(self.label_cat_3_title, 0, 3, 1, 1)

        self.label_cat_4_color = QLabel(self.centralwidget)
        self.label_cat_4_color.setObjectName(u"label_cat_4_color")
        self.label_cat_4_color.setStyleSheet(u"color:#3B78FF")
        self.label_cat_4_color.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_cat_4_color, 1, 2, 1, 1)

        self.label_cat_1_title = QLabel(self.centralwidget)
        self.label_cat_1_title.setObjectName(u"label_cat_1_title")

        self.gridLayout_2.addWidget(self.label_cat_1_title, 0, 1, 1, 1)

        self.label_cat_3_color = QLabel(self.centralwidget)
        self.label_cat_3_color.setObjectName(u"label_cat_3_color")
        self.label_cat_3_color.setStyleSheet(u"color:#CC00CC")
        self.label_cat_3_color.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_cat_3_color, 0, 2, 1, 1)

        self.label_cat_1_title_2 = QLabel(self.centralwidget)
        self.label_cat_1_title_2.setObjectName(u"label_cat_1_title_2")

        self.gridLayout_2.addWidget(self.label_cat_1_title_2, 1, 1, 1, 1)

        self.label_cat_1_color = QLabel(self.centralwidget)
        self.label_cat_1_color.setObjectName(u"label_cat_1_color")
        self.label_cat_1_color.setStyleSheet(u"color: #CC0000")
        self.label_cat_1_color.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_cat_1_color, 0, 0, 1, 1)

        self.label_cat_4_title = QLabel(self.centralwidget)
        self.label_cat_4_title.setObjectName(u"label_cat_4_title")

        self.gridLayout_2.addWidget(self.label_cat_4_title, 1, 3, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 3, 1, 1)

        self.label_letter_count = QLabel(self.centralwidget)
        self.label_letter_count.setObjectName(u"label_letter_count")

        self.gridLayout.addWidget(self.label_letter_count, 3, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionOpen)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\ub9de\ucda4\ubc95 \uac80\uc0ac\uae30 plus v1.0", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open(O)", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit(Q)", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.label_original.setText(QCoreApplication.translate("MainWindow", u"\uc6d0\ubb38", None))
        self.label_checked.setText(QCoreApplication.translate("MainWindow", u"\uad50\uc815 \uacb0\uacfc", None))
        self.pushButton_check.setText(QCoreApplication.translate("MainWindow", u"\ub9de\ucda4\ubc95 \uac80\uc0ac", None))
        self.pushButton_reset.setText(QCoreApplication.translate("MainWindow", u"\ucd08\uae30\ud654", None))
        self.label_cat_2_color.setText(QCoreApplication.translate("MainWindow", u"\u25cf", None))
        self.label_cat_3_title.setText(QCoreApplication.translate("MainWindow", u"\ud45c\uc900\uc5b4\uc758\uc2ec", None))
        self.label_cat_4_color.setText(QCoreApplication.translate("MainWindow", u"\u25cf", None))
        self.label_cat_1_title.setText(QCoreApplication.translate("MainWindow", u"\ub9de\ucda4\ubc95", None))
        self.label_cat_3_color.setText(QCoreApplication.translate("MainWindow", u"\u25cf", None))
        self.label_cat_1_title_2.setText(QCoreApplication.translate("MainWindow", u"\ub744\uc5b4\uc4f0\uae30", None))
        self.label_cat_1_color.setText(QCoreApplication.translate("MainWindow", u"\u25cf", None))
        self.label_cat_4_title.setText(QCoreApplication.translate("MainWindow", u"\ud1b5\uacc4\uc801\uad50\uc815", None))
        self.label_letter_count.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c", None))
    # retranslateUi

