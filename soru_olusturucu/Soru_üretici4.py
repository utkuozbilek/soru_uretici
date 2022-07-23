# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Soru_üretici4.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(323, 319)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 12, 1, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 12, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(Form)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 11, 0, 1, 2)
        self.checkBox_12 = QtWidgets.QCheckBox(Form)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout.addWidget(self.checkBox_12, 10, 0, 1, 2)
        self.checkBox_7 = QtWidgets.QCheckBox(Form)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 8, 0, 1, 2)
        self.checkBox_8 = QtWidgets.QCheckBox(Form)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 6, 0, 1, 2)
        self.checkBox_10 = QtWidgets.QCheckBox(Form)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout.addWidget(self.checkBox_10, 7, 0, 1, 2)
        self.checkBox_11 = QtWidgets.QCheckBox(Form)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout.addWidget(self.checkBox_11, 9, 0, 1, 2)
        self.checkBox_9 = QtWidgets.QCheckBox(Form)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout.addWidget(self.checkBox_9, 5, 0, 1, 2)
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 1, 0, 1, 2)
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 2, 0, 1, 2)
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 3, 0, 1, 2)
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 2)
        self.checkBox_6 = QtWidgets.QCheckBox(Form)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 4, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "ÇALIŞTIR"))
        self.radioButton.setText(_translate("Form", "KARIŞTIR"))
        self.checkBox_5.setText(_translate("Form", "CUMHURİYET ESERLERİ"))
        self.checkBox_12.setText(_translate("Form", "CUMHURİYET YAZARLARI"))
        self.checkBox_7.setText(_translate("Form", "CUMHURİYET HİKAYE YAZARLARI"))
        self.checkBox_8.setText(_translate("Form", "CUMHURİYET ROMAN YAZARLARI"))
        self.checkBox_10.setText(_translate("Form", "CUMHURİYET ROMAN"))
        self.checkBox_11.setText(_translate("Form", "CUMHURİYET HİKAYE"))
        self.checkBox_9.setText(_translate("Form", "TANZİMAT/SERVETİFİNUN ESERLERİ"))
        self.checkBox_3.setText(_translate("Form", "TANZİMAT/SERVETİFİNUN ROMAN VE HİKAYE "))
        self.checkBox_4.setText(_translate("Form", "TANZİMAT/SERVETİFİNUN ŞAİRLERİ"))
        self.checkBox_2.setText(_translate("Form", "TANZİMAT/SERVETİFİNUN ŞİİRLERİ"))
        self.checkBox.setText(_translate("Form", "TANZİMAT/SERVETİFİNUN ROMAN VE HİKAYE YAZARLARI"))
        self.checkBox_6.setText(_translate("Form", "TANZİMAT/SERVETİFİNUN  YAZARLARI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())