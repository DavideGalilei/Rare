# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rare/ui/components/dialogs/login/login_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(498, 311)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginDialog.sizePolicy().hasHeightForWidth())
        LoginDialog.setSizePolicy(sizePolicy)
        self.dialog_layout = QtWidgets.QVBoxLayout(LoginDialog)
        self.dialog_layout.setObjectName("dialog_layout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.dialog_layout.addItem(spacerItem)
        self.welcome_label = QtWidgets.QLabel(LoginDialog)
        self.welcome_label.setObjectName("welcome_label")
        self.dialog_layout.addWidget(self.welcome_label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.dialog_layout.addItem(spacerItem1)
        self.login_stack = QtWidgets.QStackedWidget(LoginDialog)
        self.login_stack.setEnabled(True)
        self.login_stack.setMinimumSize(QtCore.QSize(480, 135))
        self.login_stack.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_stack.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_stack.setObjectName("login_stack")
        self.login_page = QtWidgets.QWidget()
        self.login_page.setEnabled(True)
        self.login_page.setObjectName("login_page")
        self.login_page_layout = QtWidgets.QGridLayout(self.login_page)
        self.login_page_layout.setObjectName("login_page_layout")
        self.login_browser_label = QtWidgets.QLabel(self.login_page)
        font = QtGui.QFont()
        font.setItalic(True)
        self.login_browser_label.setFont(font)
        self.login_browser_label.setObjectName("login_browser_label")
        self.login_page_layout.addWidget(self.login_browser_label, 1, 1, 1, 1)
        self.login_label = QtWidgets.QLabel(self.login_page)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.login_label.setFont(font)
        self.login_label.setObjectName("login_label")
        self.login_page_layout.addWidget(self.login_label, 0, 0, 1, 3, QtCore.Qt.AlignTop)
        self.login_import_label = QtWidgets.QLabel(self.login_page)
        font = QtGui.QFont()
        font.setItalic(True)
        self.login_import_label.setFont(font)
        self.login_import_label.setObjectName("login_import_label")
        self.login_page_layout.addWidget(self.login_import_label, 2, 1, 1, 1)
        self.login_import_radio = QtWidgets.QRadioButton(self.login_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_import_radio.sizePolicy().hasHeightForWidth())
        self.login_import_radio.setSizePolicy(sizePolicy)
        self.login_import_radio.setObjectName("login_import_radio")
        self.login_page_layout.addWidget(self.login_import_radio, 2, 0, 1, 1)
        self.login_browser_radio = QtWidgets.QRadioButton(self.login_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_browser_radio.sizePolicy().hasHeightForWidth())
        self.login_browser_radio.setSizePolicy(sizePolicy)
        self.login_browser_radio.setObjectName("login_browser_radio")
        self.login_page_layout.addWidget(self.login_browser_radio, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.login_page_layout.addItem(spacerItem2, 1, 2, 2, 1)
        self.login_stack.addWidget(self.login_page)
        self.dialog_layout.addWidget(self.login_stack)
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setObjectName("button_layout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.button_layout.addItem(spacerItem3)
        self.exit_button = QtWidgets.QPushButton(LoginDialog)
        self.exit_button.setObjectName("exit_button")
        self.button_layout.addWidget(self.exit_button)
        self.back_button = QtWidgets.QPushButton(LoginDialog)
        self.back_button.setObjectName("back_button")
        self.button_layout.addWidget(self.back_button)
        self.next_button = QtWidgets.QPushButton(LoginDialog)
        self.next_button.setObjectName("next_button")
        self.button_layout.addWidget(self.next_button)
        self.dialog_layout.addLayout(self.button_layout)

        self.retranslateUi(LoginDialog)
        self.login_stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Welcome to Rare"))
        self.welcome_label.setText(_translate("LoginDialog", "<h1>Welcome to Rare</h1>"))
        self.login_browser_label.setText(_translate("LoginDialog", "Login using a browser."))
        self.login_label.setText(_translate("LoginDialog", "Select login method"))
        self.login_import_label.setText(_translate("LoginDialog", "Import from Epic Games Launcher"))
        self.login_import_radio.setText(_translate("LoginDialog", "Import"))
        self.login_browser_radio.setText(_translate("LoginDialog", "Browser"))
        self.exit_button.setText(_translate("LoginDialog", "Exit"))
        self.back_button.setText(_translate("LoginDialog", "Back"))
        self.next_button.setText(_translate("LoginDialog", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginDialog = QtWidgets.QDialog()
    ui = Ui_LoginDialog()
    ui.setupUi(LoginDialog)
    LoginDialog.show()
    sys.exit(app.exec_())
