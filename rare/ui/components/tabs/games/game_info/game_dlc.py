# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rare/ui/components/tabs/games/game_info/game_dlc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GameDlc(object):
    def setupUi(self, GameDlc):
        GameDlc.setObjectName("GameDlc")
        GameDlc.resize(287, 366)
        self.game_dlc_layout = QtWidgets.QVBoxLayout(GameDlc)
        self.game_dlc_layout.setObjectName("game_dlc_layout")
        self.game_title = QtWidgets.QLabel(GameDlc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_title.sizePolicy().hasHeightForWidth())
        self.game_title.setSizePolicy(sizePolicy)
        self.game_title.setText("error")
        self.game_title.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.game_title.setObjectName("game_title")
        self.game_dlc_layout.addWidget(self.game_title, 0, QtCore.Qt.AlignTop)
        self.installed_dlc_group = QtWidgets.QGroupBox(GameDlc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.installed_dlc_group.sizePolicy().hasHeightForWidth())
        self.installed_dlc_group.setSizePolicy(sizePolicy)
        self.installed_dlc_group.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.installed_dlc_group.setObjectName("installed_dlc_group")
        self.installed_dlc_group_layout = QtWidgets.QVBoxLayout(self.installed_dlc_group)
        self.installed_dlc_group_layout.setObjectName("installed_dlc_group_layout")
        self.installed_dlc_label = QtWidgets.QLabel(self.installed_dlc_group)
        self.installed_dlc_label.setObjectName("installed_dlc_label")
        self.installed_dlc_group_layout.addWidget(self.installed_dlc_label)
        self.installed_dlc_scroll = QtWidgets.QScrollArea(self.installed_dlc_group)
        self.installed_dlc_scroll.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.installed_dlc_scroll.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.installed_dlc_scroll.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.installed_dlc_scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.installed_dlc_scroll.setWidgetResizable(True)
        self.installed_dlc_scroll.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.installed_dlc_scroll.setObjectName("installed_dlc_scroll")
        self.installed_dlc_contents = QtWidgets.QWidget()
        self.installed_dlc_contents.setGeometry(QtCore.QRect(0, 0, 255, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.installed_dlc_contents.sizePolicy().hasHeightForWidth())
        self.installed_dlc_contents.setSizePolicy(sizePolicy)
        self.installed_dlc_contents.setObjectName("installed_dlc_contents")
        self.installed_dlc_contents_layout = QtWidgets.QVBoxLayout(self.installed_dlc_contents)
        self.installed_dlc_contents_layout.setSpacing(6)
        self.installed_dlc_contents_layout.setObjectName("installed_dlc_contents_layout")
        self.installed_dlc_scroll.setWidget(self.installed_dlc_contents)
        self.installed_dlc_group_layout.addWidget(self.installed_dlc_scroll)
        self.game_dlc_layout.addWidget(self.installed_dlc_group)
        self.available_dlc_group = QtWidgets.QGroupBox(GameDlc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.available_dlc_group.sizePolicy().hasHeightForWidth())
        self.available_dlc_group.setSizePolicy(sizePolicy)
        self.available_dlc_group.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.available_dlc_group.setObjectName("available_dlc_group")
        self.available_dlc_group_layout = QtWidgets.QVBoxLayout(self.available_dlc_group)
        self.available_dlc_group_layout.setObjectName("available_dlc_group_layout")
        self.available_dlc_label = QtWidgets.QLabel(self.available_dlc_group)
        self.available_dlc_label.setObjectName("available_dlc_label")
        self.available_dlc_group_layout.addWidget(self.available_dlc_label)
        self.available_dlc_scroll = QtWidgets.QScrollArea(self.available_dlc_group)
        self.available_dlc_scroll.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.available_dlc_scroll.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.available_dlc_scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.available_dlc_scroll.setWidgetResizable(True)
        self.available_dlc_scroll.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.available_dlc_scroll.setObjectName("available_dlc_scroll")
        self.available_dlc_contents = QtWidgets.QWidget()
        self.available_dlc_contents.setGeometry(QtCore.QRect(0, 0, 255, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.available_dlc_contents.sizePolicy().hasHeightForWidth())
        self.available_dlc_contents.setSizePolicy(sizePolicy)
        self.available_dlc_contents.setObjectName("available_dlc_contents")
        self.available_dlc_contents_layout = QtWidgets.QVBoxLayout(self.available_dlc_contents)
        self.available_dlc_contents_layout.setSpacing(6)
        self.available_dlc_contents_layout.setObjectName("available_dlc_contents_layout")
        self.available_dlc_scroll.setWidget(self.available_dlc_contents)
        self.available_dlc_group_layout.addWidget(self.available_dlc_scroll)
        self.game_dlc_layout.addWidget(self.available_dlc_group)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.game_dlc_layout.addItem(spacerItem)

        self.retranslateUi(GameDlc)
        QtCore.QMetaObject.connectSlotsByName(GameDlc)

    def retranslateUi(self, GameDlc):
        _translate = QtCore.QCoreApplication.translate
        GameDlc.setWindowTitle(_translate("GameDlc", "GameDlc"))
        self.installed_dlc_group.setTitle(_translate("GameDlc", "Installed DLCs"))
        self.installed_dlc_label.setText(_translate("GameDlc", "No Downloadable Content has been installed."))
        self.available_dlc_group.setTitle(_translate("GameDlc", "Available DLCs"))
        self.available_dlc_label.setText(_translate("GameDlc", "No Downloadable Content is available"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GameDlc = QtWidgets.QWidget()
    ui = Ui_GameDlc()
    ui.setupUi(GameDlc)
    GameDlc.show()
    sys.exit(app.exec_())