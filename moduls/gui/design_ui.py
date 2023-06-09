# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/max/PycharmProjects/lab1/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_lab1(object):
    def setupUi(self, lab1):
        lab1.setObjectName("lab1")
        lab1.setEnabled(True)
        lab1.resize(862, 600)
        lab1.setAcceptDrops(False)
        lab1.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(lab1)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 861, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.main_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setObjectName("main_layout")
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setObjectName("buttons_layout")
        self.persons_count = QtWidgets.QSlider(self.gridLayoutWidget)
        self.persons_count.setEnabled(True)
        self.persons_count.setMaximum(10)
        self.persons_count.setPageStep(1)
        self.persons_count.setOrientation(QtCore.Qt.Horizontal)
        self.persons_count.setObjectName("persons_count")
        self.buttons_layout.addWidget(self.persons_count)
        self.start_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.start_btn.setFont(font)
        self.start_btn.setObjectName("start_btn")
        self.buttons_layout.addWidget(self.start_btn)
        self.console_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.console_btn.setFont(font)
        self.console_btn.setObjectName("console_btn")
        self.buttons_layout.addWidget(self.console_btn)
        self.main_layout.addLayout(self.buttons_layout, 0, 0, 1, 1)
        self.progress_bars_layout = QtWidgets.QVBoxLayout()
        self.progress_bars_layout.setObjectName("progress_bars_layout")
        self.progress1_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.progress1_label.setFont(font)
        self.progress1_label.setObjectName("progress1_label")
        self.progress_bars_layout.addWidget(self.progress1_label)
        self.progress2_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.progress2_label.setFont(font)
        self.progress2_label.setObjectName("progress2_label")
        self.progress_bars_layout.addWidget(self.progress2_label)
        self.progress3_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.progress3_label.setFont(font)
        self.progress3_label.setObjectName("progress3_label")
        self.progress_bars_layout.addWidget(self.progress3_label)
        self.main_layout.addLayout(self.progress_bars_layout, 1, 0, 1, 1)
        lab1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(lab1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 862, 22))
        self.menubar.setObjectName("menubar")
        lab1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(lab1)
        self.statusbar.setEnabled(True)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        lab1.setStatusBar(self.statusbar)

        self.retranslateUi(lab1)
        QtCore.QMetaObject.connectSlotsByName(lab1)

    def retranslateUi(self, lab1):
        _translate = QtCore.QCoreApplication.translate
        lab1.setWindowTitle(_translate("lab1", "lab 1"))
        self.start_btn.setText(_translate("lab1", "Start"))
        self.console_btn.setText(_translate("lab1", "Console"))
        self.progress1_label.setText(_translate("lab1", "Person1Progres"))
        self.progress2_label.setText(_translate("lab1", "Person2Progres"))
        self.progress3_label.setText(_translate("lab1", "Person3Progres"))
