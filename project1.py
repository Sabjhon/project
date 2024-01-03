import sys
from PyQt5 import QtCore, QtWidgets
from mpl_canvas import MplCanvas
from data_plotter import get_parameter_list  # Assuming this function is defined in data_plotter.py

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1096, 850)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-70, 20, 1331, 811))
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 40, 1101, 771))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox_5")
        self.verticalLayout.addWidget(self.comboBox)

        # Create a list to store MplCanvas instances
        self.mpl_canvases = []

        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setGeometry(QtCore.QRect(90, 0, 151, 31))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMaximum(4)
        self.spinBox.valueChanged.connect(self.update_widgets)

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(500, 0, 93, 28))
        self.pushButton.setStyleSheet("\n"
                                      "background-color: rgb(155, 170, 200);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 0, 93, 28))
        self.pushButton_2.setStyleSheet("background-color: rgb(155, 170, 200);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(790, 0, 93, 28))
        self.pushButton_3.setStyleSheet("background-color: rgb(155, 170, 200);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(920, 0, 93, 28))
        self.pushButton_4.setStyleSheet("background-color: rgb(155, 170, 200);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 55, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 0, 55, 16))
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.pushButton_4.setText(_translate("MainWindow", "Close"))
        self.label.setText(_translate("MainWindow", "Windows"))
        self.label_2.setText(_translate("MainWindow", "Time"))

    parameters = []

    def update_widgets(self, value):
        # Clear all widgets
        for i in reversed(range(self.verticalLayout.count())):
            item = self.verticalLayout.takeAt(i)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

        # Recreate widgets based on the updated count
        self.mpl_canvases = []  # Clear the list before creating new instances
        for i in range(value):
            combo_box = QtWidgets.QComboBox(self.verticalLayoutWidget)
            combo_box.setObjectName(f"comboBox_{i}")
            combo_box.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            self.verticalLayout.addWidget(combo_box)

            parameters = get_parameter_list()
            combo_box.addItems(parameters)

            mpl_canvas = MplCanvas(self.verticalLayoutWidget)
            mpl_canvas.setObjectName(f"mplCanvas_{i}")
            mpl_canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout.addWidget(mpl_canvas)

            self.mpl_canvases.append(mpl_canvas) 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
