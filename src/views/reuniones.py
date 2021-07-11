# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reuniones.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from database.database import InserReunion, DeleteReunion, getReuniones


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(546, 602)
        self.nombre = QtWidgets.QLineEdit(Frame)
        self.nombre.setGeometry(QtCore.QRect(130, 70, 351, 31))
        self.nombre.setObjectName("nombre")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(50, 70, 71, 21))
        self.label.setObjectName("label")
        self.url = QtWidgets.QLineEdit(Frame)
        self.url.setGeometry(QtCore.QRect(130, 120, 351, 31))
        self.url.setObjectName("url")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(80, 120, 55, 21))
        self.label_2.setObjectName("label_2")
        self.agregar = QtWidgets.QPushButton(Frame)
        self.agregar.setGeometry(QtCore.QRect(360, 170, 121, 31))
        self.agregar.setObjectName("agregar")
        self.agregar.clicked.connect(self.agregarReunion)
        self.tableWidget = QtWidgets.QTableWidget(Frame)
        self.tableWidget.setGeometry(QtCore.QRect(50, 250, 421, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.eliminar = QtWidgets.QPushButton(Frame)
        self.eliminar.setGeometry(QtCore.QRect(230, 170, 111, 28))
        self.eliminar.setObjectName("eliminar")
        self.eliminar.clicked.connect(self.eliminarReunion)

        
        for i in getReuniones():
            index = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(index + 1)
            self.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(i[1]))
            self.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(i[2]))

            index += 1

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def agregarReunion(self):
        try:
            if self.nombre.text() != '' and self.url.text() != '':
                index = self.tableWidget.rowCount()
                self.tableWidget.setRowCount(index + 1)
                self.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(self.nombre.text()))
                self.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(self.url.text()))

                InserReunion(self.nombre.text(), self.url.text())

                index += 1

        except Exception as e:
            print(e)
    
    def eliminarReunion(self):
        try:
            if not self.tableWidget.currentIndex().isValid():
                return

            DeleteReunion(self.tableWidget.currentItem().text())

            self.tableWidget.removeRow(self.tableWidget.currentItem().row())
        except Exception as e:
            print(e)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt;\">Nombre: </span></p></body></html>"))
        self.label_2.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:10pt;\">URL: </span></p></body></html>"))
        self.agregar.setText(_translate("Frame", "Añadir"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "URL"))
        self.eliminar.setText(_translate("Frame", "Eliminar"))
