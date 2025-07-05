from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DetailWindow(object):
    def setupUi(self, DetailWindow):
        DetailWindow.setObjectName("DetailWindow")
        DetailWindow.resize(510, 379)
        DetailWindow.setStyleSheet("QWidget#centralwidget {\n"
"    background-color: #1F2A2F;\n"
"}\n"
"\n"
"QLabel {\n"
"    background-color: #2E3F3A;\n"
"    color: #A8D5BA;\n"
"    border-radius: 14px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(DetailWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.detail_title_label = QtWidgets.QLabel(self.centralwidget)
        self.detail_title_label.setGeometry(QtCore.QRect(10, 10, 491, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.detail_title_label.setFont(font)
        self.detail_title_label.setText("")
        self.detail_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.detail_title_label.setObjectName("detail_title_label")
        self.detail_desc_label = QtWidgets.QLabel(self.centralwidget)
        self.detail_desc_label.setGeometry(QtCore.QRect(10, 90, 491, 281))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.detail_desc_label.setFont(font)
        self.detail_desc_label.setText("")
        self.detail_desc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.detail_desc_label.setObjectName("detail_desc_label")
        DetailWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DetailWindow)
        QtCore.QMetaObject.connectSlotsByName(DetailWindow)

    def retranslateUi(self, DetailWindow):
        _translate = QtCore.QCoreApplication.translate
        DetailWindow.setWindowTitle(_translate("DetailWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DetailWindow = QtWidgets.QMainWindow()
    ui = Ui_DetailWindow()
    ui.setupUi(DetailWindow)
    DetailWindow.show()
    sys.exit(app.exec_())
