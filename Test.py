import sys
import serial
import struct
from PyQt5 import QtCore, QtWidgets
import pyqtgraph as pg
import numpy as np

from gui_program import Ui_MainWindow

class MplCanvas(pg.PlotWidget):
    update_plot_signal = QtCore.pyqtSignal(float, float)

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.curve_f1 = self.plotItem.plot(pen='r', name="F1")
        self.curve_f2 = self.plotItem.plot(pen='g', name="F2")

        self.x_data = np.linspace(0, 10, 100)
        self.data_f1 = [0] * 100
        self.data_f2 = [0] * 100

        self.curve_f1.setData(self.x_data, self.data_f1)
        self.curve_f2.setData(self.x_data, self.data_f2)

        self.update_plot_signal.connect(self.update_plot)

    @QtCore.pyqtSlot(float, float)
    def update_plot(self, f1, f2):
        self.data_f1 = self.data_f1[1:] + [f1]
        self.data_f2 = self.data_f2[1:] + [f2]

        self.curve_f1.setData(self.x_data, self.data_f1)
        self.curve_f2.setData(self.x_data, self.data_f2)

    def clear_data(self):
        self.data_f1 = [0] * 100
        self.data_f2 = [0] * 100

        self.curve_f1.setData(self.x_data, self.data_f1)
        self.curve_f2.setData(self.x_data, self.data_f2)
        self.pushButton_3.clicked.connect(self.clear_data)

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.curve_f1 = self.plotItem.plot(pen='r', name="F1")
        self.curve_f2 = self.plotItem.plot(pen='g', name="F2")

        self.x_data = np.linspace(0, 10, 100)
        self.data_f1 = [0] * 100
        self.data_f2 = [0] * 100

        self.curve_f1.setData(self.x_data, self.data_f1)
        self.curve_f2.setData(self.x_data, self.data_f2)

        self.update_plot_signal.connect(self.update_plot)

    @QtCore.pyqtSlot(float, float)
    def update_plot(self, f1, f2):
        self.data_f1 = self.data_f1[1:] + [f1]
        self.data_f2 = self.data_f2[1:] + [f2]

        self.curve_f1.setData(self.x_data, self.data_f1)
        self.curve_f2.setData(self.x_data, self.data_f2)

    def clear_data(self):
        self.data_f1 = [0] * 100
        self.data_f2 = [0] * 100

        self.curve_f1.setData(self.x_data, self.data_f1)
        self.curve_f2.setData(self.x_data, self.data_f2)

class WorkerSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(float, float)

class Worker(QtCore.QObject):
    def __init__(self, port_name):
        super().__init__()
        self.port_name = port_name
        self.is_running = False
        self.signals = WorkerSignals()
        self.serial_port = None

    def stop(self):
        self.is_running = False

    def run(self):
        try:
            self.serial_port = serial.Serial(self.port_name, 115200, timeout=500)
            print("Connected to Arduino")
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
            self.signals.finished.emit()
            return

        self.is_running = True
        while self.is_running:
            self.read_serial_data()

        if self.serial_port is not None:
            self.serial_port.close()

        self.signals.finished.emit()

    def read_serial_data(self):
        if not self.is_running:
            return

        header1 = self.serial_port.read()
        header2 = self.serial_port.read()

        if header1 == b'\xff' and header2 == b'\xff':
            chksum = 255 + 255
            pl_sz = ord(self.serial_port.read())
            chksum += pl_sz
            payload = self.serial_port.read(pl_sz - 1)
            chksum += sum(payload)
            chksum = bytes([chksum % 256])
            _chksum = self.serial_port.read()

            if _chksum == chksum:
                f1, f2 = struct.unpack('2f', payload[:8])
                print(f"Received data: f1={f1}, f2={f2}")
                self.signals.progress.emit(f1, f2)
            else:
                print(f"Checksum mismatch. Expected: {chksum}, Received: {_chksum}")
        else:
            print("Invalid header")

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.serial_port = 'COM3'
        self.worker = Worker(self.serial_port)
        self.canvas = MplCanvas(parent=self.verticalLayoutWidget)
        # self.verticalLayout.addWidget(self.canvas)
        self.worker_thread = None

        self.pushButton.clicked.connect(self.toggle_serial_thread)
        self.pushButton_3.clicked.connect(self.clear_data)
        self.pushButton_2.clicked.connect(self.stop_serial_thread)
    def toggle_serial_thread(self):
        if not self.worker.is_running:
            self.start_serial_thread()
        else:
            self.stop_serial_thread()

    def start_serial_thread(self):
        self.worker_thread = QtCore.QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(self.worker.run, QtCore.Qt.QueuedConnection)
        self.worker.signals.progress.connect(self.canvas.update_plot_signal.emit)
        self.worker_thread.start()

    def stop_serial_thread(self):
        if self.worker_thread and self.worker_thread.isRunning():
            self.worker.stop()
            self.worker_thread.quit()
            self.worker_thread.wait()
            self.worker_thread = None

    def clear_data(self):
        self.canvas.clear_data()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
