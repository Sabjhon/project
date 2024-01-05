import pyqtgraph as pg
import numpy as np

class MplCanvas(pg.PlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.curve_f1 = self.plotItem.plot(pen='r', name="F1")
        self.curve_f2 = self.plotItem.plot(pen='g', name="F2")
        # self.curve_f3 = self.plotItem.plot(pen='b', name="F3")
        # self.curve_f4 = self.plotItem.plot(pen='c', name="F4")
        # self.curve_cop_x = self.plotItem.plot(pen='m', name="COP_X")
        # self.curve_cop_y = self.plotItem.plot(pen='y', name="COP_Y")

        self.x_data = np.linspace(0, 10, 100)
        self.data_f1 = [0] * 100
        self.data_f2 = [0] * 100
        # self.data_f3 = [0] * 100
        # self.data_f4 = [0] * 100
        # self.data_cop_x = [0] * 100
        # self.data_cop_y = [0] * 100

        self.curve_f1.setData(self.x_data, self.data_f1)
        self.curve_f2.setData(self.x_data, self.data_f2)
        # self.curve_f3.setData(self.x_data, self.data_f3)
        # self.curve_f4.setData(self.x_data, self.data_f4)
        # self.curve_cop_x.setData(self.x_data, self.data_cop_x)
        # self.curve_cop_y.setData(self.x_data, self.data_cop_y)

    def update_plot(self, f1, f2):
        self.data_f1 = self.data_f1[1:] + [f1]
        self.data_f2 = self.data_f2[1:] + [f2]
        # self.data_f3 = self.data_f3[1:] + [f3]
        # self.data_f4 = self.data_f4[1:] + [f4]
        # self.data_cop_x = self.data_cop_x[1:] + [cop_x]
        # self.data_cop_y = self.data_cop_y[1:] + [cop_y]

        self.curve_f1.setData(self.x_data, self.data_f1)
        self.curve_f2.setData(self.x_data, self.data_f2)
        # self.curve_f3.setData(self.x_data, self.data_f3)
        # self.curve_f4.setData(self.x_data, self.data_f4)
        # self.curve_cop_x.setData(self.x_data, self.data_cop_x)
        # self.curve_cop_y.setData(self.x_data, self.data_cop_y)