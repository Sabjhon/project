from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1077, 740)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.centralwidget.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )

        self.horizontalLayoutMain = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayoutMain.setObjectName("horizontalLayoutMain")
        self.horizontalLayoutMain.setSpacing(5)

        # Top box (spinBox and buttons)
        self.verticalLayoutTop = QtWidgets.QVBoxLayout()
        self.verticalLayoutTop.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.verticalLayoutTop.setContentsMargins(30, 30, 30, 30)

        # SpinBox
        self.label2 = QtWidgets.QLabel("Number of Windows", self.centralwidget)
        self.verticalLayoutTop.addWidget(self.label2)

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.verticalLayoutTop.addWidget(self.spinBox)
        self.spinBox.setMaximum(4)

        # Buttons
        self.startButton = QtWidgets.QPushButton("Start", self.centralwidget)
        self.verticalLayoutTop.addWidget(self.startButton)

        self.clearButton = QtWidgets.QPushButton("Clear", self.centralwidget)
        self.verticalLayoutTop.addWidget(self.clearButton)

        self.stopButton = QtWidgets.QPushButton("Stop", self.centralwidget)
        self.verticalLayoutTop.addWidget(self.stopButton)

        self.horizontalLayoutMain.addLayout(self.verticalLayoutTop)

        # Left box (remaining controls)
        self.verticalLayoutControls = QtWidgets.QVBoxLayout()
        self.verticalLayoutControls.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.verticalLayoutControls.setContentsMargins(30, 30, 30, 30)

        # Labels for spinBox2
        self.label3 = QtWidgets.QLabel("Time", self.centralwidget)
        self.verticalLayoutControls.addWidget(self.label3)
        self.verticalLayoutControls.setSpacing(10)

        self.spinBox2 = QtWidgets.QSpinBox(self.centralwidget)
        self.verticalLayoutControls.addWidget(self.spinBox2)

        # ... Add more controls as needed ...

        self.horizontalLayoutMain.addLayout(self.verticalLayoutControls)

        # Right box
        self.widgetContainer = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutMain.addWidget(self.widgetContainer)

        self.gridLayoutWidgets = QtWidgets.QGridLayout(self.widgetContainer)
        self.gridLayoutWidgets.setObjectName("gridLayoutWidgets")
        self.gridLayoutWidgets.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidgets.setSpacing(0)

        self.comboBoxWidgets = []
        self.openGLWidgets = []

        for i in range(1, 5):
            combo_box = QtWidgets.QComboBox(self.widgetContainer)
            combo_box.setObjectName(f"comboBox_{i}")
            combo_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
            combo_box.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            self.comboBoxWidgets.append(combo_box)

            opengl_widget = QtWidgets.QOpenGLWidget(self.widgetContainer)
            opengl_widget.setObjectName(f"openGLWidget_{i}")
            opengl_widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            self.openGLWidgets.append(opengl_widget)

            self.gridLayoutWidgets.addWidget(combo_box, (i - 1) * 2, 0)
            self.gridLayoutWidgets.addWidget(opengl_widget, (i - 1) * 2 + 1, 0)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.spinBox.valueChanged.connect(self.updateWidgets)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def updateWidgets(self, value):
        for i in range(4):
            self.comboBoxWidgets[i].setVisible(i < value)
            self.openGLWidgets[i].setVisible(i < value)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
