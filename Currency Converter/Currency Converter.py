# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Nhat\Desktop\QTDesigner\Currency Converter\Currency Converter.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
import sys

class Ui_CurrencyConverter(object):
    def setupUi(self, CurrencyConverter):
        CurrencyConverter.setObjectName("CurrencyConverter")
        CurrencyConverter.resize(688, 427)
        CurrencyConverter.setStyleSheet("background-color: rgb(29, 116, 122);")
        CurrencyConverter.setTabShape(QtWidgets.QTabWidget.Rounded)
        CurrencyConverter.setWindowIcon(QtGui.QIcon('munnie.ico'))
        self.centralwidget = QtWidgets.QWidget(CurrencyConverter)
        self.centralwidget.setObjectName("centralwidget")
        self.currencyPicker = QtWidgets.QComboBox(self.centralwidget)
        self.currencyPicker.setGeometry(QtCore.QRect(280, 90, 121, 22))
        self.currencyPicker.setAcceptDrops(False)
        self.currencyPicker.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Rockwell\";")
        self.currencyPicker.setFrame(True)
        self.currencyPicker.setObjectName("currencyPicker")
        self.currencyLabel = QtWidgets.QLabel(self.centralwidget)
        self.currencyLabel.setGeometry(QtCore.QRect(310, 60, 71, 20))
        self.currencyLabel.setStyleSheet("font: 11pt \"Rockwell\";\n"
"")
        self.currencyLabel.setIndent(-1)
        self.currencyLabel.setObjectName("currencyLabel")
        self.convertCurrency = QtWidgets.QLineEdit(self.centralwidget)
        self.convertCurrency.setGeometry(QtCore.QRect(120, 210, 141, 21))
        self.convertCurrency.setStyleSheet("background-color:white;\n"
"font: 9pt \"NSimSun\";")
        self.convertCurrency.setObjectName("convertCurrency")
        self.usdCurrency = QtWidgets.QTextEdit(self.centralwidget)
        self.usdCurrency.setGeometry(QtCore.QRect(420, 210, 141, 21))
        self.usdCurrency.setStyleSheet("background-color:white;\n"
"font: 9pt \"NSimSun\";\n"
"")
        self.usdCurrency.setReadOnly(True)
        self.usdCurrency.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.usdCurrency.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.usdCurrency.setObjectName("usdCurrency")
        self.chosenNameLabel = QtWidgets.QTextEdit(self.centralwidget)
        self.chosenNameLabel.setGeometry(QtCore.QRect(140, 160, 120, 16))
        self.chosenNameLabel.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Rockwell\";\n"
"")
        self.chosenNameLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.chosenNameLabel.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.chosenNameLabel.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.chosenNameLabel.setObjectName("chosenNameLabel")
        self.usdNameLabel = QtWidgets.QTextEdit(self.centralwidget)
        self.usdNameLabel.setGeometry(QtCore.QRect(440, 160, 104, 16))
        self.usdNameLabel.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Rockwell\";\n"
"")
        self.usdNameLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.usdNameLabel.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.usdNameLabel.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.usdNameLabel.setObjectName("usdNameLabel")
        self.arrow = QtWidgets.QLabel(self.centralwidget)
        self.arrow.setGeometry(QtCore.QRect(300, 180, 91, 20))
        self.arrow.setStyleSheet("font: 81 12pt \"Rockwell Extra Bold\";")
        self.arrow.setObjectName("arrow")
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(290, 260, 101, 41))
        self.convertButton.setStyleSheet("font: 75 14p t \"Rockwell\";\n"
"background-color: rgb(232, 232, 232);\n"
"\n"
"")
        self.convertButton.setAutoDefault(False)
        self.convertButton.setDefault(False)
        self.convertButton.setFlat(False)
        self.convertButton.setObjectName("convertButton")
        CurrencyConverter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CurrencyConverter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuMenu.setStyleSheet("background-color:gray")
        CurrencyConverter.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CurrencyConverter)
        self.statusbar.setObjectName("statusbar")
        CurrencyConverter.setStatusBar(self.statusbar)
        self.actionInfo = QtWidgets.QAction(CurrencyConverter)
        self.actionInfo.setObjectName("actionInfo")
        self.actionQuit = QtWidgets.QAction(CurrencyConverter)
        self.actionQuit.setObjectName("actionQuit")
        self.menuMenu.addAction(self.actionInfo)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionQuit)
        self.menuMenu.addSeparator()
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(CurrencyConverter)
        QtCore.QMetaObject.connectSlotsByName(CurrencyConverter)

        currencyList = ["Pound(Britain)", "Canadian Dollar", "Won(Korean)", "Yen(Japanese)", "Peso(Mexico)", "Rupee(India)", "Dong(Vietnamese)"]
        self.currencyPicker.addItems(currencyList)
        self.chosenNameLabel.setText(self.currencyPicker.currentText())
        self.usdNameLabel.setText("US Dollars")
        self.currencyPicker.currentIndexChanged.connect(self.changeCurrencyLabel)

        self.convertButton.clicked.connect(self.checker)

        self.actionQuit.triggered.connect(self.quit)
       	
       	self.actionInfo.triggered.connect(self.printInfo)


    def retranslateUi(self, CurrencyConverter):
        _translate = QtCore.QCoreApplication.translate
        CurrencyConverter.setWindowTitle(_translate("CurrencyConverter", "Munnify"))
        self.currencyLabel.setText(_translate("CurrencyConverter", "Currency"))
        self.arrow.setText(_translate("CurrencyConverter", "=======>"))
        self.convertButton.setText(_translate("CurrencyConverter", "Convert"))
        self.menuMenu.setTitle(_translate("CurrencyConverter", "Menu"))
        self.actionInfo.setText(_translate("CurrencyConverter", "Info"))
        self.actionQuit.setText(_translate("CurrencyConverter", "Quit"))


    def printInfo(self):
    	msgBox = QMessageBox()
    	msgBox.setIcon(QMessageBox.Information)
    	msgBox.setText("Nhat's Complex Currency Converter")
    	msgBox.setWindowTitle("About")
    	msgBox.setStandardButtons(QMessageBox.Ok)
    	msgBox.exec_()


    def quit():
    	self.exit()

    def checker(self):
    	self.current_currency = self.currencyPicker.currentText()
    	if self.current_currency == "Won(Korean)":
    		self.korean2USD()
    	elif self.current_currency == "Yen(Japanese)":
    		self.japanese2USD()
    	elif self.current_currency == "Peso(Mexico)":
    		self.mexico2USD()
    	elif self.current_currency == "Rupee(India)":
    		self.india2USD()
    	elif self.current_currency == "Dong(Vietnamese)":
    		self.vietnamese2USD()
    	elif self.current_currency == "Canadian Dollar":
    		self.canada2USD()
    	elif self.current_currency == "Pound(Britain)":
    		self.britain2USD()

    def changeCurrencyLabel(self):
    	self.chosenNameLabel.setText(self.currencyPicker.currentText())
    	
    def korean2USD(self):
    	try:
    		self.usdCurrency.clear()
    		x = 0.00084
    		value = self.convertCurrency.text()
    		converted = float(value)*x
    		self.usdCurrency.append(str(converted))
    	except:
    		self.usdCurrency.append("Incorrect Values")

    def japanese2USD(self):
    	try:
    		self.usdCurrency.clear()
    		x = 0.0092
    		value = self.convertCurrency.text()
    		converted = float(value)*x
    		self.usdCurrency.append(str(converted))
    	except:
    		self.usdCurrency.append("Incorrect Values")

    def mexico2USD(self):
    	try:
    		self.usdCurrency.clear()
    		x = 0.052
    		value = self.convertCurrency.text()
    		converted = float(value)*x
    		self.usdCurrency.append(str(converted))
    	except:
    		self.usdCurrency.append("Incorrect Values")

    def india2USD(self):
    	try:
    		self.usdCurrency.clear()
    		x = 0.014
    		value = self.convertCurrency.text()
    		converted = float(value)*x
    		self.usdCurrency.append(str(converted))
    	except:
    		self.usdCurrency.append("Incorrect Values")

    def vietnamese2USD(self):
    	try:
    		self.usdCurrency.clear()
    		x = 0.000043
    		value = self.convertCurrency.text()
    		converted = float(value)*x
    		self.usdCurrency.append(str(converted))
    	except:
    		self.usdCurrency.append("Incorrect Values")

    def canada2USD(self):
    	try:
    		self.usdCurrency.clear()
    		x = 0.74
    		value = self.convertCurrency.text()
    		converted = float(value)*x
    		self.usdCurrency.append(str(converted))
    	except:
    		self.usdCurrency.append("Incorrect Values")

    def britain2USD(self):
    	try:
    		self.usdCurrency.clear()
    		x = 1.26
    		value = self.convertCurrency.text()
    		converted = float(value)*x
    		self.usdCurrency.append(str(converted))
    	except:
    		self.usdCurrency.append("Incorrect Values")






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CurrencyConverter = QtWidgets.QMainWindow()
    ui = Ui_CurrencyConverter()
    ui.setupUi(CurrencyConverter)
    CurrencyConverter.show()
    sys.exit(app.exec_())

