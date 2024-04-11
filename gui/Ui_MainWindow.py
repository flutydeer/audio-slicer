# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFormLayout, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(768, 480)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonAddFiles = QPushButton(self.centralwidget)
        self.pushButtonAddFiles.setObjectName(u"pushButtonAddFiles")
        self.pushButtonAddFiles.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAddFiles.sizePolicy().hasHeightForWidth())
        self.pushButtonAddFiles.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.pushButtonAddFiles)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


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
        self.listWidgetTaskList = QListWidget(self.groupBox)
        self.listWidgetTaskList.setObjectName(u"listWidgetTaskList")
        self.listWidgetTaskList.setFrameShadow(QFrame.Plain)

        self.verticalLayout_2.addWidget(self.listWidgetTaskList)

        self.pushButtonClearList = QPushButton(self.groupBox)
        self.pushButtonClearList.setObjectName(u"pushButtonClearList")

        self.verticalLayout_2.addWidget(self.pushButtonClearList)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineEditThreshold = QLineEdit(self.groupBox_2)
        self.lineEditThreshold.setObjectName(u"lineEditThreshold")
        self.lineEditThreshold.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditThreshold)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.lineEditMinLen = QLineEdit(self.groupBox_2)
        self.lineEditMinLen.setObjectName(u"lineEditMinLen")
        self.lineEditMinLen.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditMinLen)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.lineEditMinInterval = QLineEdit(self.groupBox_2)
        self.lineEditMinInterval.setObjectName(u"lineEditMinInterval")
        self.lineEditMinInterval.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEditMinInterval)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.lineEditHopSize = QLineEdit(self.groupBox_2)
        self.lineEditHopSize.setObjectName(u"lineEditHopSize")
        self.lineEditHopSize.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEditHopSize)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.lineEditMaxSilence = QLineEdit(self.groupBox_2)
        self.lineEditMaxSilence.setObjectName(u"lineEditMaxSilence")
        self.lineEditMaxSilence.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEditMaxSilence)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEditOutputDir = QLineEdit(self.groupBox_2)
        self.lineEditOutputDir.setObjectName(u"lineEditOutputDir")
        self.lineEditOutputDir.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lineEditOutputDir)

        self.pushButtonBrowse = QPushButton(self.groupBox_2)
        self.pushButtonBrowse.setObjectName(u"pushButtonBrowse")

        self.horizontalLayout_4.addWidget(self.pushButtonBrowse)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.radioButton = QRadioButton(self.groupBox_2)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.horizontalLayout_5.addWidget(self.radioButton, 0, Qt.AlignHCenter)

        self.radioButton_1 = QRadioButton(self.groupBox_2)
        self.buttonGroup.addButton(self.radioButton_1)
        self.radioButton_1.setObjectName(u"radioButton_1")

        self.horizontalLayout_5.addWidget(self.radioButton_1, 0, Qt.AlignHCenter)

        self.radioButton_2 = QRadioButton(self.groupBox_2)
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setEnabled(True)

        self.horizontalLayout_5.addWidget(self.radioButton_2, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonAbout = QPushButton(self.centralwidget)
        self.pushButtonAbout.setObjectName(u"pushButtonAbout")

        self.horizontalLayout_3.addWidget(self.pushButtonAbout)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout_3.addWidget(self.progressBar)

        self.pushButtonStart = QPushButton(self.centralwidget)
        self.pushButtonStart.setObjectName(u"pushButtonStart")

        self.horizontalLayout_3.addWidget(self.pushButtonStart)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonAddFiles.setText(QCoreApplication.translate("MainWindow", u"Add Audio Files...", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Task List", None))
        self.pushButtonClearList.setText(QCoreApplication.translate("MainWindow", u"Clear List", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Threshold (dB)", None))
        self.lineEditThreshold.setText(QCoreApplication.translate("MainWindow", u"-40", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Minimum Length (ms)", None))
        self.lineEditMinLen.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Minimum Interval (ms)", None))
        self.lineEditMinInterval.setText(QCoreApplication.translate("MainWindow", u"300", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Hop Size (ms)", None))
        self.lineEditHopSize.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Maximum Silence Length (ms)", None))
        self.lineEditMaxSilence.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Output Directory (default to the same as the audio)", None))
        self.lineEditOutputDir.setText("")
        self.pushButtonBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Output Format", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"wav", None))
        self.radioButton_1.setText(QCoreApplication.translate("MainWindow", u"flac", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"mp3", None))
        self.pushButtonAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.pushButtonStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

