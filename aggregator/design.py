0# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 380)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 380))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 380))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(1000, 380))
        self.centralwidget.setObjectName("centralwidget")
        self.Tutby_chk_box = QtWidgets.QCheckBox(self.centralwidget)
        self.Tutby_chk_box.setGeometry(QtCore.QRect(20, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Tutby_chk_box.setFont(font)
        self.Tutby_chk_box.setObjectName("Tutby_chk_box")
        self.Onliner_chk_box = QtWidgets.QCheckBox(self.centralwidget)
        self.Onliner_chk_box.setGeometry(QtCore.QRect(20, 60, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Onliner_chk_box.setFont(font)
        self.Onliner_chk_box.setObjectName("Onliner_chk_box")
        self.Belta_chk_box = QtWidgets.QCheckBox(self.centralwidget)
        self.Belta_chk_box.setGeometry(QtCore.QRect(20, 110, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Belta_chk_box.setFont(font)
        self.Belta_chk_box.setObjectName("Belta_chk_box")
        self.Parse_btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.Parse_btn_start.setGeometry(QtCore.QRect(280, 310, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Parse_btn_start.setFont(font)
        self.Parse_btn_start.setObjectName("Parse_btn_start")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(20, 160, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(280, 10, 681, 291))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 220, 256, 81))
        self.listWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(750, 310, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 310, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Tutby_chk_box.setText(_translate("MainWindow", "Tut by"))
        self.Onliner_chk_box.setText(_translate("MainWindow", "Onliner"))
        self.Belta_chk_box.setText(_translate("MainWindow", "BelTa"))
        self.Parse_btn_start.setText(_translate("MainWindow", "Просмотреть"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "Технологии и Наука"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "Общество"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MainWindow", "Спорт"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("MainWindow", "Авто"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("MainWindow", "Экономика и финансы"))
        item = self.listWidget_2.item(5)
        item.setText(_translate("MainWindow", "Недвижимость"))
        item = self.listWidget_2.item(6)
        item.setText(_translate("MainWindow", "Здоровье"))
        item = self.listWidget_2.item(7)
        item.setText(_translate("MainWindow", "Леди"))
        item = self.listWidget_2.item(8)
        item.setText(_translate("MainWindow", "Эксклюзив"))
        item = self.listWidget_2.item(9)
        item.setText(_translate("MainWindow", "Происшествия"))
        item = self.listWidget_2.item(10)
        item.setText(_translate("MainWindow", "Афиша"))
        item = self.listWidget_2.item(11)
        item.setText(_translate("MainWindow", "Разное"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Посмотреть статью"))
        self.pushButton_2.setText(_translate("MainWindow", "Cброс"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())