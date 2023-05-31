# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QFormLayout, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QProgressBar, QPushButton, QTabWidget,
    QSizePolicy, QVBoxLayout, QWidget, QAbstractItemView, QGraphicsView)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1140, 656)
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI")
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.twImages = QTabWidget(self.centralwidget)
        self.twImages.setObjectName(u"twImages")
        self.twImages.setTabShape(QTabWidget.Rounded)
        self.twImages.setUsesScrollButtons(True)
        self.twImages.setDocumentMode(True)
        self.twImages.setTabsClosable(True)
        self.twImages.setMovable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.twImages.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.twImages.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.twImages)

        self.gbTasks = QGroupBox(self.centralwidget)
        self.gbTasks.setObjectName(u"gbTasks")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbTasks.sizePolicy().hasHeightForWidth())
        self.gbTasks.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.gbTasks)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnAddFiles = QPushButton(self.gbTasks)
        self.btnAddFiles.setObjectName(u"btnAddFiles")
        self.btnAddFiles.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnAddFiles.sizePolicy().hasHeightForWidth())
        self.btnAddFiles.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.btnAddFiles)

        self.lwTaskList = QListWidget(self.gbTasks)
        self.lwTaskList.setObjectName(u"lwTaskList")
        self.lwTaskList.setFrameShadow(QFrame.Plain)
        self.lwTaskList.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_2.addWidget(self.lwTaskList)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btnRemove = QPushButton(self.gbTasks)
        self.btnRemove.setObjectName(u"btnRemove")

        self.horizontalLayout_5.addWidget(self.btnRemove)

        self.btnClearList = QPushButton(self.gbTasks)
        self.btnClearList.setObjectName(u"btnClearList")

        self.horizontalLayout_5.addWidget(self.btnClearList)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.gbTasks)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.leThreshold = QLineEdit(self.gbTasks)
        self.leThreshold.setObjectName(u"leThreshold")
        self.leThreshold.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.leThreshold)

        self.label_3 = QLabel(self.gbTasks)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.gbTasks)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.leMinInterval = QLineEdit(self.gbTasks)
        self.leMinInterval.setObjectName(u"leMinInterval")
        self.leMinInterval.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.leMinInterval)

        self.label_5 = QLabel(self.gbTasks)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.leHopSize = QLineEdit(self.gbTasks)
        self.leHopSize.setObjectName(u"leHopSize")
        self.leHopSize.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.leHopSize)

        self.label_6 = QLabel(self.gbTasks)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.leMaxSilence = QLineEdit(self.gbTasks)
        self.leMaxSilence.setObjectName(u"leMaxSilence")
        self.leMaxSilence.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.leMaxSilence)

        self.leMinLen = QLineEdit(self.gbTasks)
        self.leMinLen.setObjectName(u"leMinLen")
        self.leMinLen.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.leMinLen)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.label_7 = QLabel(self.gbTasks)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.leOutputDir = QLineEdit(self.gbTasks)
        self.leOutputDir.setObjectName(u"leOutputDir")
        self.leOutputDir.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.leOutputDir)

        self.btnBrowse = QPushButton(self.gbTasks)
        self.btnBrowse.setObjectName(u"btnBrowse")

        self.horizontalLayout_4.addWidget(self.btnBrowse)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout.addWidget(self.gbTasks)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnAbout = QPushButton(self.centralwidget)
        self.btnAbout.setObjectName(u"btnAbout")

        self.horizontalLayout_3.addWidget(self.btnAbout)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout_3.addWidget(self.progressBar)

        self.btnPreview = QPushButton(self.centralwidget)
        self.btnPreview.setObjectName(u"btnPreview")

        self.horizontalLayout_3.addWidget(self.btnPreview)

        self.btnStart = QPushButton(self.centralwidget)
        self.btnStart.setObjectName(u"btnStart")

        self.horizontalLayout_3.addWidget(self.btnStart)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.twImages.setTabText(self.twImages.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.twImages.setTabText(self.twImages.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.gbTasks.setTitle(QCoreApplication.translate("MainWindow", u"Tasks", None))
        self.btnAddFiles.setText(QCoreApplication.translate("MainWindow", u"Add Audio Files...", None))
        self.btnRemove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.btnClearList.setText(QCoreApplication.translate("MainWindow", u"Clear List", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Threshold (dB)", None))
        self.leThreshold.setText(QCoreApplication.translate("MainWindow", u"-40", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Minimum Length (ms)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Minimum Interval (ms)", None))
        self.leMinInterval.setText(QCoreApplication.translate("MainWindow", u"300", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Hop Size (ms)", None))
        self.leHopSize.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Maximum Silence Length (ms)", None))
        self.leMaxSilence.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.leMinLen.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Output Directory (default to the same as the audio)", None))
        self.leOutputDir.setText("")
        self.btnBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.btnAbout.setText(QCoreApplication.translate("MainWindow", u"About...", None))
        self.btnPreview.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

