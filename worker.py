# worker.py
from PyQt5 import QtCore
import serial
import struct

class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(float, float, float, float, float, float)

    def __init__(self, port_name):
        super().__init__()
        self.port_name = port_name
        self.is_running = False

    def stop(self):
        self.is_running = False

    def start_work(self):
        try:
            serial_port = serial.Serial(self.port_name, 115200, timeout=500)
            print("Connected to Arduino")
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
            return

        self.is_running = True
        while self.is_running:
            if serial_port.read() == b'\xff' and serial_port.read() == b'\xff':
                chksum = 255 + 255
                plSz = serial_port.read(1)[0]
                chksum += plSz
                payload = serial_port.read(plSz)
                chksum += sum(payload)
                chksum = bytes([chksum % 256])
                _chksum = serial_port.read()

                if _chksum == chksum:
                    f1, f2, f3, f4, cop_x, cop_y = struct.unpack('6f', payload[:24])
                    self.progress.emit(f1, f2, f3, f4, cop_x, cop_y)
                    print(f1,f2,f3,f4)
                else:
                    print(f"Checksum mismatch. Expected: {chksum}, Received: {_chksum}")
            else:
                print("Invalid header")

        serial_port.close()
        self.finished.emit()
