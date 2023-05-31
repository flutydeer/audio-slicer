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
    QProgressBar, QPushButton, QSpacerItem, QCheckBox,
    QSizePolicy, QVBoxLayout, QWidget, QAbstractItemView, QGraphicsView)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(768, 480)
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI")
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAddFiles = QPushButton(self.centralwidget)
        self.btnAddFiles.setObjectName(u"btnAddFiles")
        self.btnAddFiles.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAddFiles.sizePolicy().hasHeightForWidth())
        self.btnAddFiles.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.btnAddFiles)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnAbout = QPushButton(self.centralwidget)
        self.btnAbout.setObjectName(u"btnAbout")

        self.horizontalLayout_2.addWidget(self.btnAbout)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lwTaskList = QListWidget(self.groupBox)
        self.lwTaskList.setObjectName(u"lwTaskList")
        self.lwTaskList.setFrameShadow(QFrame.Plain)
        self.lwTaskList.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_2.addWidget(self.lwTaskList)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btnRemove = QPushButton(self.groupBox)
        self.btnRemove.setObjectName(u"btnRemove")

        self.horizontalLayout_5.addWidget(self.btnRemove)

        self.btnClearList = QPushButton(self.groupBox)
        self.btnClearList.setObjectName(u"btnClearList")

        self.horizontalLayout_5.addWidget(self.btnClearList)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.leThreshold = QLineEdit(self.groupBox_2)
        self.leThreshold.setObjectName(u"leThreshold")
        self.leThreshold.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.leThreshold)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.leMinInterval = QLineEdit(self.groupBox_2)
        self.leMinInterval.setObjectName(u"leMinInterval")
        self.leMinInterval.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.leMinInterval)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.leHopSize = QLineEdit(self.groupBox_2)
        self.leHopSize.setObjectName(u"leHopSize")
        self.leHopSize.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.leHopSize)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.leMaxSilence = QLineEdit(self.groupBox_2)
        self.leMaxSilence.setObjectName(u"leMaxSilence")
        self.leMaxSilence.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.leMaxSilence)

        self.leMinLen = QLineEdit(self.groupBox_2)
        self.leMinLen.setObjectName(u"leMinLen")
        self.leMinLen.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.leMinLen)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.btnPreviewSelection = QPushButton(self.groupBox_2)
        self.btnPreviewSelection.setObjectName(u"btnPreviewSelection")

        self.verticalLayout_3.addWidget(self.btnPreviewSelection)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.leOutputDir = QLineEdit(self.groupBox_2)
        self.leOutputDir.setObjectName(u"leOutputDir")
        self.leOutputDir.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.leOutputDir)

        self.btnBrowse = QPushButton(self.groupBox_2)
        self.btnBrowse.setObjectName(u"btnBrowse")

        self.horizontalLayout_4.addWidget(self.btnBrowse)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.cbxOpenOutuptDirectory = QCheckBox(self.groupBox_2)
        self.cbxOpenOutuptDirectory.setObjectName(u"cbxOpenOutuptDirectory")

        self.verticalLayout_3.addWidget(self.cbxOpenOutuptDirectory)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout_3.addWidget(self.progressBar)

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
        self.btnAddFiles.setText(QCoreApplication.translate("MainWindow", u"Add Audio Files...", None))
        self.btnAbout.setText(QCoreApplication.translate("MainWindow", u"About...", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Task List", None))
        self.btnRemove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.btnClearList.setText(QCoreApplication.translate("MainWindow", u"Clear List", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
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
        self.btnPreviewSelection.setText(QCoreApplication.translate("MainWindow", u"Preview Selection", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Output Directory (default to the same as the audio)", None))
        self.leOutputDir.setText("")
        self.btnBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.cbxOpenOutuptDirectory.setText(QCoreApplication.translate("MainWindow", u"Open output directory when finished", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

