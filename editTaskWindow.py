from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditTaskWindow(object):
    def setupUi(self, EditTaskWindow):
        EditTaskWindow.setObjectName("EditTaskWindow")
        EditTaskWindow.resize(509, 449)
        EditTaskWindow.setStyleSheet("QWidget#centralwidget {\n"
"    background-color: #1F2A2F;\n"
"}\n"
"\n"
"QLineEdit, QTextEdit {\n"
"    background-color: #3F514B;\n"
"    color: #A8D5BA;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 6px;\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #4A7C59;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5A9F73;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(EditTaskWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleEdit_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.titleEdit_lineEdit.setGeometry(QtCore.QRect(10, 10, 491, 91))
        self.titleEdit_lineEdit.setObjectName("titleEdit_lineEdit")
        self.descEdit_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.descEdit_textEdit.setGeometry(QtCore.QRect(10, 110, 491, 261))
        self.descEdit_textEdit.setObjectName("descEdit_textEdit")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(50, 380, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(260, 380, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        EditTaskWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EditTaskWindow)
        QtCore.QMetaObject.connectSlotsByName(EditTaskWindow)

    def retranslateUi(self, EditTaskWindow):
        _translate = QtCore.QCoreApplication.translate
        EditTaskWindow.setWindowTitle(_translate("EditTaskWindow", "MainWindow"))
        self.save_button.setText(_translate("EditTaskWindow", "Save"))
        self.cancel_button.setText(_translate("EditTaskWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditTaskWindow = QtWidgets.QMainWindow()
    ui = Ui_EditTaskWindow()
    ui.setupUi(EditTaskWindow)
    EditTaskWindow.show()
    sys.exit(app.exec_())
