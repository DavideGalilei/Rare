# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shop_game_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_shop_info(object):
    def setupUi(self, shop_info):
        shop_info.setObjectName("shop_info")
        shop_info.resize(702, 468)
        self.verticalLayout = QtWidgets.QVBoxLayout(shop_info)
        self.verticalLayout.setObjectName("verticalLayout")
        self.back_button = QtWidgets.QPushButton(shop_info)
        self.back_button.setObjectName("back_button")
        self.verticalLayout.addWidget(self.back_button)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.image_stack = QtWidgets.QStackedWidget(shop_info)
        self.image_stack.setObjectName("image_stack")
        self.horizontalLayout.addWidget(self.image_stack)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title = QtWidgets.QLabel(shop_info)
        self.title.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.title.setObjectName("title")
        self.verticalLayout_2.addWidget(self.title)
        self.dev = QtWidgets.QLabel(shop_info)
        self.dev.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.dev.setObjectName("dev")
        self.verticalLayout_2.addWidget(self.dev)
        self.owned_label = QtWidgets.QLabel(shop_info)
        self.owned_label.setObjectName("owned_label")
        self.verticalLayout_2.addWidget(self.owned_label)
        self.price = QtWidgets.QLabel(shop_info)
        self.price.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.price.setObjectName("price")
        self.verticalLayout_2.addWidget(self.price)
        self.discount_price = QtWidgets.QLabel(shop_info)
        self.discount_price.setObjectName("discount_price")
        self.verticalLayout_2.addWidget(self.discount_price)
        self.open_store_button = QtWidgets.QPushButton(shop_info)
        self.open_store_button.setObjectName("open_store_button")
        self.verticalLayout_2.addWidget(self.open_store_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.req_group_box = QtWidgets.QGroupBox(shop_info)
        self.req_group_box.setObjectName("req_group_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.req_group_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout.addWidget(self.req_group_box)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(shop_info)
        self.image_stack.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(shop_info)

    def retranslateUi(self, shop_info):
        _translate = QtCore.QCoreApplication.translate
        shop_info.setWindowTitle(_translate("shop_info", "Form"))
        self.back_button.setText(_translate("shop_info", "Back"))
        self.title.setText(_translate("shop_info", "Error"))
        self.dev.setText(_translate("shop_info", "TextLabel"))
        self.owned_label.setText(_translate("shop_info", "You already own this game"))
        self.price.setText(_translate("shop_info", "TextLabel"))
        self.discount_price.setText(_translate("shop_info", "TextLabel"))
        self.open_store_button.setText(_translate("shop_info", "Buy Game in Epic Games Store"))
        self.req_group_box.setTitle(_translate("shop_info", "Requirements"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    shop_info = QtWidgets.QWidget()
    ui = Ui_shop_info()
    ui.setupUi(shop_info)
    shop_info.show()
    sys.exit(app.exec_())
