# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rare/ui/components/tabs/games/import_sync/egl_sync_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EGLSyncGroup(object):
    def setupUi(self, EGLSyncGroup):
        EGLSyncGroup.setObjectName("EGLSyncGroup")
        EGLSyncGroup.resize(680, 430)
        self.egl_sync_layout = QtWidgets.QFormLayout(EGLSyncGroup)
        self.egl_sync_layout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.egl_sync_layout.setObjectName("egl_sync_layout")
        self.export_import_layout = QtWidgets.QHBoxLayout()
        self.export_import_layout.setObjectName("export_import_layout")
        self.export_group = QtWidgets.QGroupBox(EGLSyncGroup)
        self.export_group.setObjectName("export_group")
        self.export_layout = QtWidgets.QVBoxLayout(self.export_group)
        self.export_layout.setObjectName("export_layout")
        self.export_label = QtWidgets.QLabel(self.export_group)
        self.export_label.setObjectName("export_label")
        self.export_layout.addWidget(self.export_label)
        self.export_list = QtWidgets.QListWidget(self.export_group)
        self.export_list.setAlternatingRowColors(True)
        self.export_list.setObjectName("export_list")
        self.export_layout.addWidget(self.export_list)
        self.export_buttons_layout = QtWidgets.QHBoxLayout()
        self.export_buttons_layout.setObjectName("export_buttons_layout")
        self.export_select_all_button = QtWidgets.QPushButton(self.export_group)
        self.export_select_all_button.setObjectName("export_select_all_button")
        self.export_buttons_layout.addWidget(self.export_select_all_button)
        self.export_select_none_button = QtWidgets.QPushButton(self.export_group)
        self.export_select_none_button.setObjectName("export_select_none_button")
        self.export_buttons_layout.addWidget(self.export_select_none_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.export_buttons_layout.addItem(spacerItem)
        self.export_button = QtWidgets.QPushButton(self.export_group)
        self.export_button.setObjectName("export_button")
        self.export_buttons_layout.addWidget(self.export_button)
        self.export_layout.addLayout(self.export_buttons_layout)
        self.export_import_layout.addWidget(self.export_group)
        self.import_group = QtWidgets.QGroupBox(EGLSyncGroup)
        self.import_group.setObjectName("import_group")
        self.import_layout = QtWidgets.QVBoxLayout(self.import_group)
        self.import_layout.setObjectName("import_layout")
        self.import_label = QtWidgets.QLabel(self.import_group)
        self.import_label.setObjectName("import_label")
        self.import_layout.addWidget(self.import_label)
        self.import_list = QtWidgets.QListWidget(self.import_group)
        self.import_list.setAlternatingRowColors(True)
        self.import_list.setObjectName("import_list")
        self.import_layout.addWidget(self.import_list)
        self.import_buttons_layout = QtWidgets.QHBoxLayout()
        self.import_buttons_layout.setObjectName("import_buttons_layout")
        self.import_select_all_button = QtWidgets.QPushButton(self.import_group)
        self.import_select_all_button.setObjectName("import_select_all_button")
        self.import_buttons_layout.addWidget(self.import_select_all_button)
        self.import_select_none_button = QtWidgets.QPushButton(self.import_group)
        self.import_select_none_button.setObjectName("import_select_none_button")
        self.import_buttons_layout.addWidget(self.import_select_none_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.import_buttons_layout.addItem(spacerItem1)
        self.import_button = QtWidgets.QPushButton(self.import_group)
        self.import_button.setObjectName("import_button")
        self.import_buttons_layout.addWidget(self.import_button)
        self.import_layout.addLayout(self.import_buttons_layout)
        self.export_import_layout.addWidget(self.import_group)
        self.egl_sync_layout.setLayout(4, QtWidgets.QFormLayout.SpanningRole, self.export_import_layout)
        self.egl_path_layout = QtWidgets.QVBoxLayout()
        self.egl_path_layout.setObjectName("egl_path_layout")
        self.egl_sync_layout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.egl_path_layout)
        self.egl_path_label = QtWidgets.QLabel(EGLSyncGroup)
        self.egl_path_label.setObjectName("egl_path_label")
        self.egl_sync_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.egl_path_label)
        self.egl_path_info_label = QtWidgets.QLabel(EGLSyncGroup)
        self.egl_path_info_label.setObjectName("egl_path_info_label")
        self.egl_sync_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.egl_path_info_label)
        self.egl_path_info = QtWidgets.QLabel(EGLSyncGroup)
        self.egl_path_info.setText("")
        self.egl_path_info.setObjectName("egl_path_info")
        self.egl_sync_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.egl_path_info)
        self.egl_auto_check = QtWidgets.QCheckBox(EGLSyncGroup)
        self.egl_auto_check.setText("")
        self.egl_auto_check.setObjectName("egl_auto_check")
        self.egl_sync_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.egl_auto_check)
        self.refresh_button = QtWidgets.QPushButton(EGLSyncGroup)
        self.refresh_button.setObjectName("refresh_button")
        self.egl_sync_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.refresh_button)
        self.egl_auto_check_label = QtWidgets.QLabel(EGLSyncGroup)
        self.egl_auto_check_label.setObjectName("egl_auto_check_label")
        self.egl_sync_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.egl_auto_check_label)

        self.retranslateUi(EGLSyncGroup)
        QtCore.QMetaObject.connectSlotsByName(EGLSyncGroup)

    def retranslateUi(self, EGLSyncGroup):
        _translate = QtCore.QCoreApplication.translate
        EGLSyncGroup.setWindowTitle(_translate("EGLSyncGroup", "EGLSyncGroup"))
        EGLSyncGroup.setTitle(_translate("EGLSyncGroup", "Sync with Epic Games Launcher"))
        self.export_group.setTitle(_translate("EGLSyncGroup", "Exportable games"))
        self.export_label.setText(_translate("EGLSyncGroup", "No games to export to EGS"))
        self.export_list.setSortingEnabled(True)
        self.export_select_all_button.setText(_translate("EGLSyncGroup", "Select all"))
        self.export_select_none_button.setText(_translate("EGLSyncGroup", "Select none"))
        self.export_button.setText(_translate("EGLSyncGroup", "Export"))
        self.import_group.setTitle(_translate("EGLSyncGroup", "Importable games"))
        self.import_label.setText(_translate("EGLSyncGroup", "No games to import from EGS"))
        self.import_list.setSortingEnabled(True)
        self.import_select_all_button.setText(_translate("EGLSyncGroup", "Select all"))
        self.import_select_none_button.setText(_translate("EGLSyncGroup", "Select none"))
        self.import_button.setText(_translate("EGLSyncGroup", "Import"))
        self.egl_path_label.setText(_translate("EGLSyncGroup", "Manifest path"))
        self.egl_path_info_label.setText(_translate("EGLSyncGroup", "Estimated path"))
        self.refresh_button.setText(_translate("EGLSyncGroup", "Refresh"))
        self.egl_auto_check_label.setText(_translate("EGLSyncGroup", "Enable automatic sync"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EGLSyncGroup = QtWidgets.QGroupBox()
    ui = Ui_EGLSyncGroup()
    ui.setupUi(EGLSyncGroup)
    EGLSyncGroup.show()
    sys.exit(app.exec_())