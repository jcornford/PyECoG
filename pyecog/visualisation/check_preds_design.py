# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check_preds_design_v2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.full_splitter = QtWidgets.QSplitter(self.centralwidget)
        self.full_splitter.setOrientation(QtCore.Qt.Vertical)
        self.full_splitter.setObjectName("full_splitter")
        self.top_splitter = QtWidgets.QSplitter(self.full_splitter)
        self.top_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.top_splitter.setObjectName("top_splitter")
        self.treeWidget = QtWidgets.QTreeWidget(self.top_splitter)
        self.treeWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.treeWidget.setFont(font)
        self.treeWidget.setAutoExpandDelay(-1)
        self.treeWidget.setColumnCount(8)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.treeWidget.headerItem().setFont(0, font)
        self.treeWidget.headerItem().setText(1, "2")
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.treeWidget.headerItem().setFont(1, font)
        self.treeWidget.headerItem().setText(2, "3")
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.treeWidget.headerItem().setFont(2, font)
        self.treeWidget.headerItem().setText(3, "4")
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.treeWidget.headerItem().setFont(3, font)
        self.treeWidget.headerItem().setText(4, "5")
        self.treeWidget.headerItem().setText(5, "6")
        self.treeWidget.headerItem().setText(6, "7")
        self.treeWidget.headerItem().setText(7, "8")
        self.treeWidget.header().setDefaultSectionSize(50)
        self.treeWidget.header().setMinimumSectionSize(5)
        self.GraphicsLayoutWidget = GraphicsLayoutWidget(self.top_splitter)
        self.GraphicsLayoutWidget.setEnabled(True)
        self.GraphicsLayoutWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.GraphicsLayoutWidget.setObjectName("GraphicsLayoutWidget")
        self.overview_plot = GraphicsLayoutWidget(self.full_splitter)
        self.overview_plot.setMinimumSize(QtCore.QSize(0, 300))
        self.overview_plot.setBaseSize(QtCore.QSize(0, 300))
        self.overview_plot.setObjectName("overview_plot")
        self.bottom_splitter = QtWidgets.QSplitter(self.full_splitter)
        self.bottom_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.bottom_splitter.setObjectName("bottom_splitter")
        self.layoutWidget = QtWidgets.QWidget(self.bottom_splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_1 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_1.setObjectName("gridLayout_1")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 12)
        self.gridLayout_3.setHorizontalSpacing(30)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(0, 31))
        self.label_6.setMaximumSize(QtCore.QSize(210, 16777215))
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.tid_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tid_spinBox.sizePolicy().hasHeightForWidth())
        self.tid_spinBox.setSizePolicy(sizePolicy)
        self.tid_spinBox.setMinimumSize(QtCore.QSize(0, 31))
        self.tid_spinBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.tid_spinBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tid_spinBox.setObjectName("tid_spinBox")
        self.gridLayout_3.addWidget(self.tid_spinBox, 0, 1, 1, 1)
        self.checkBox_scrolling = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_scrolling.setObjectName("checkBox_scrolling")
        self.gridLayout_3.addWidget(self.checkBox_scrolling, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 31))
        self.label_5.setMaximumSize(QtCore.QSize(190, 16777215))
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 3, 1, 1)
        self.xrange_spinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xrange_spinBox.sizePolicy().hasHeightForWidth())
        self.xrange_spinBox.setSizePolicy(sizePolicy)
        self.xrange_spinBox.setMinimumSize(QtCore.QSize(0, 31))
        self.xrange_spinBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.xrange_spinBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.xrange_spinBox.setMaximum(3600.0)
        self.xrange_spinBox.setObjectName("xrange_spinBox")
        self.gridLayout_3.addWidget(self.xrange_spinBox, 0, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 31))
        self.label_3.setMaximumSize(QtCore.QSize(210, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.predictions_file_display = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.predictions_file_display.sizePolicy().hasHeightForWidth())
        self.predictions_file_display.setSizePolicy(sizePolicy)
        self.predictions_file_display.setMinimumSize(QtCore.QSize(0, 31))
        self.predictions_file_display.setObjectName("predictions_file_display")
        self.gridLayout_3.addWidget(self.predictions_file_display, 1, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 31))
        self.label.setMaximumSize(QtCore.QSize(190, 16777215))
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 3, 1, 1)
        self.scroll_speed_box = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll_speed_box.sizePolicy().hasHeightForWidth())
        self.scroll_speed_box.setSizePolicy(sizePolicy)
        self.scroll_speed_box.setMinimumSize(QtCore.QSize(0, 31))
        self.scroll_speed_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.scroll_speed_box.setMinimum(1)
        self.scroll_speed_box.setObjectName("scroll_speed_box")
        self.gridLayout_3.addWidget(self.scroll_speed_box, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 31))
        self.label_4.setMaximumSize(QtCore.QSize(210, 16777215))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.h5_folder_display = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.h5_folder_display.sizePolicy().hasHeightForWidth())
        self.h5_folder_display.setSizePolicy(sizePolicy)
        self.h5_folder_display.setMinimumSize(QtCore.QSize(0, 31))
        self.h5_folder_display.setDragEnabled(True)
        self.h5_folder_display.setReadOnly(True)
        self.h5_folder_display.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.h5_folder_display.setObjectName("h5_folder_display")
        self.gridLayout_3.addWidget(self.h5_folder_display, 2, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 31))
        self.label_2.setMaximumSize(QtCore.QSize(190, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 3, 1, 1)
        self.blink_box = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blink_box.sizePolicy().hasHeightForWidth())
        self.blink_box.setSizePolicy(sizePolicy)
        self.blink_box.setObjectName("blink_box")
        self.gridLayout_3.addWidget(self.blink_box, 2, 4, 1, 1)
        self.gridLayout_1.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QtCore.QSize(0, 31))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_6.addWidget(self.label_15, 0, 0, 1, 1)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_3.setMinimumSize(QtCore.QSize(0, 100))
        self.plainTextEdit_3.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.gridLayout_6.addWidget(self.plainTextEdit_3, 1, 0, 1, 1)
        self.gridLayout_1.addWidget(self.groupBox, 1, 0, 1, 1)
        self.verticalGroupBox_5 = QtWidgets.QGroupBox(self.bottom_splitter)
        self.verticalGroupBox_5.setObjectName("verticalGroupBox_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.verticalGroupBox_5)
        self.gridLayout_5.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_16 = QtWidgets.QLabel(self.verticalGroupBox_5)
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 0, 0, 1, 1)
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.verticalGroupBox_5)
        self.plainTextEdit_4.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.gridLayout_5.addWidget(self.plainTextEdit_4, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.full_splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1280, 31))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuAnalyse = QtWidgets.QMenu(self.menuBar)
        self.menuAnalyse.setObjectName("menuAnalyse")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSave_annotations = QtWidgets.QAction(MainWindow)
        self.actionSave_annotations.setObjectName("actionSave_annotations")
        self.actionLoad_Library = QtWidgets.QAction(MainWindow)
        self.actionLoad_Library.setObjectName("actionLoad_Library")
        self.actionLoad_Predictions = QtWidgets.QAction(MainWindow)
        self.actionLoad_Predictions.setObjectName("actionLoad_Predictions")
        self.actionLoad_h5_folder = QtWidgets.QAction(MainWindow)
        self.actionLoad_h5_folder.setObjectName("actionLoad_h5_folder")
        self.actionConvert_dir_to_h5 = QtWidgets.QAction(MainWindow)
        self.actionConvert_dir_to_h5.setObjectName("actionConvert_dir_to_h5")
        self.actionConvert_ndf_to_h5 = QtWidgets.QAction(MainWindow)
        self.actionConvert_ndf_to_h5.setObjectName("actionConvert_ndf_to_h5")
        self.actionLibrary_logistics = QtWidgets.QAction(MainWindow)
        self.actionLibrary_logistics.setObjectName("actionLibrary_logistics")
        self.actionAdd_to_library = QtWidgets.QAction(MainWindow)
        self.actionAdd_to_library.setObjectName("actionAdd_to_library")
        self.actionAdd_labels_to_library = QtWidgets.QAction(MainWindow)
        self.actionAdd_labels_to_library.setObjectName("actionAdd_labels_to_library")
        self.actionAdd_features_to_library = QtWidgets.QAction(MainWindow)
        self.actionAdd_features_to_library.setObjectName("actionAdd_features_to_library")
        self.actionClassifier_components = QtWidgets.QAction(MainWindow)
        self.actionClassifier_components.setObjectName("actionClassifier_components")
        self.actionRun_classifer_on_h5_dir = QtWidgets.QAction(MainWindow)
        self.actionRun_classifer_on_h5_dir.setObjectName("actionRun_classifer_on_h5_dir")
        self.actionRun_classifer_on_ndf_dir = QtWidgets.QAction(MainWindow)
        self.actionRun_classifer_on_ndf_dir.setObjectName("actionRun_classifer_on_ndf_dir")
        self.actionSet_default_folder = QtWidgets.QAction(MainWindow)
        self.actionSet_default_folder.setObjectName("actionSet_default_folder")
        self.actionAdd_features_to_h5_folder = QtWidgets.QAction(MainWindow)
        self.actionAdd_features_to_h5_folder.setObjectName("actionAdd_features_to_h5_folder")
        self.actionFolder_for_substates = QtWidgets.QAction(MainWindow)
        self.actionFolder_for_substates.setObjectName("actionFolder_for_substates")
        self.actionSubstates_Window = QtWidgets.QAction(MainWindow)
        self.actionSubstates_Window.setObjectName("actionSubstates_Window")
        self.actionOpen_in_Jupyter_notebook = QtWidgets.QAction(MainWindow)
        self.actionOpen_in_Jupyter_notebook.setObjectName("actionOpen_in_Jupyter_notebook")
        self.menuFile.addAction(self.actionLoad_Library)
        self.menuFile.addAction(self.actionLoad_Predictions)
        self.menuFile.addAction(self.actionLoad_h5_folder)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_annotations)
        self.menuFile.addAction(self.actionSet_default_folder)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSubstates_Window)
        self.menuAnalyse.addAction(self.actionConvert_ndf_to_h5)
        self.menuAnalyse.addSeparator()
        self.menuAnalyse.addAction(self.actionAdd_features_to_h5_folder)
        self.menuAnalyse.addSeparator()
        self.menuAnalyse.addAction(self.actionLibrary_logistics)
        self.menuAnalyse.addSeparator()
        self.menuAnalyse.addAction(self.actionClassifier_components)
        self.menuAnalyse.addSeparator()
        self.menuAnalyse.addSeparator()
        self.menuAnalyse.addAction(self.actionOpen_in_Jupyter_notebook)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAnalyse.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Tid for h5 folder "))
        self.checkBox_scrolling.setText(_translate("MainWindow", "Scrolling  "))
        self.label_5.setText(_translate("MainWindow", "Xrange (sec)"))
        self.label_3.setText(_translate("MainWindow", "Prediction file:"))
        self.label.setText(_translate("MainWindow", "Scroll speed"))
        self.label_4.setText(_translate("MainWindow", "h5 folder:"))
        self.label_2.setText(_translate("MainWindow", "Scroll type"))
        self.blink_box.setText(_translate("MainWindow", "Blinking"))
        self.label_15.setText(_translate("MainWindow", "Mouse functionality"))
        self.plainTextEdit_3.setPlainText(_translate("MainWindow", "Scroll when hovering over either axis in the main plot to zoom that axis only. Scrolling when in the middle will zoom both axes at the same time - you probably don\'t want that."))
        self.label_16.setText(_translate("MainWindow", "Keyboard shortcuts"))
        self.plainTextEdit_4.setPlainText(_translate("MainWindow", "Up: Zoom in / speed up \n"
"Down: Zoom out / slow down \n"
"Right arrow: Step right / scroll forwards \n"
"Left arrow: Step left / scroll backwards\n"
"Number key: Set plot time interval \n"
"B key: Toggle blink vs scroll \n"
"SPACE: Start scrolling (or blinking)"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAnalyse.setTitle(_translate("MainWindow", "Analyse"))
        self.actionSave_annotations.setText(_translate("MainWindow", "Save annotations"))
        self.actionLoad_Library.setText(_translate("MainWindow", "Load Library"))
        self.actionLoad_Predictions.setText(_translate("MainWindow", "Load Predictions"))
        self.actionLoad_h5_folder.setText(_translate("MainWindow", "Load h5 folder"))
        self.actionConvert_dir_to_h5.setText(_translate("MainWindow", "Convert dir to h5"))
        self.actionConvert_ndf_to_h5.setText(_translate("MainWindow", "Convert ndf folder to h5"))
        self.actionLibrary_logistics.setText(_translate("MainWindow", "Library logistics"))
        self.actionAdd_to_library.setText(_translate("MainWindow", "Add to library"))
        self.actionAdd_labels_to_library.setText(_translate("MainWindow", "Add labels to library"))
        self.actionAdd_features_to_library.setText(_translate("MainWindow", "Add features to library"))
        self.actionClassifier_components.setText(_translate("MainWindow", "Classifier components"))
        self.actionRun_classifer_on_h5_dir.setText(_translate("MainWindow", "Run classifer on h5 dir"))
        self.actionRun_classifer_on_ndf_dir.setText(_translate("MainWindow", "Run classifer on ndf dir"))
        self.actionSet_default_folder.setText(_translate("MainWindow", "Set default folder"))
        self.actionAdd_features_to_h5_folder.setText(_translate("MainWindow", "Add features to h5 folder"))
        self.actionFolder_for_substates.setText(_translate("MainWindow", "Folder for substates"))
        self.actionSubstates_Window.setText(_translate("MainWindow", "Substates Window"))
        self.actionOpen_in_Jupyter_notebook.setText(_translate("MainWindow", "Open in Jupyter notebook"))

from pyqtgraph import GraphicsLayoutWidget
