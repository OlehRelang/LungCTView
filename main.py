import sys
import numpy as np
import SimpleITK as sitk
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *

from ui_mainwindow import Ui_MainWindow

plt.style.use('dark_background')


class Canvas(FigureCanvas):
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots(figsize=(parent.width()/100, parent.height()/100))
        super().__init__(self.fig)
        self.setParent(parent)


class LungCTViewApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.graphs = [Canvas(self.ui.Graph_widget_1), Canvas(self.ui.Graph_widget_2)]
        self.sliders = [self.ui.horizontalSlider_1, self.ui.horizontalSlider_2]
        self.filenames = [self.ui.label_file_1, self.ui.label_file_2]
        self.ids = [self.ui.label_id_1, self.ui.label_id_2]
        self.spinBoxes = [self.ui.spinBox_1, self.ui.spinBox_2]

        self.img = [np.zeros(1), np.zeros(1)]

        self.ui.pushButton_load_1.clicked.connect(lambda: self.load_ct_series(0))
        self.ui.pushButton_load_2.clicked.connect(lambda: self.load_ct_series(1))

        self.ui.horizontalSlider_1.valueChanged.connect(lambda: self.slide(0))
        self.ui.horizontalSlider_2.valueChanged.connect(lambda: self.slide(1))

        self.ui.horizontalSlider_1.sliderReleased.connect(lambda: self.slider_released(0, self.ui.horizontalSlider_1.value()))
        self.ui.horizontalSlider_2.sliderReleased.connect(lambda: self.slider_released(1, self.ui.horizontalSlider_2.value()))

        self.ui.spinBox_1.valueChanged.connect(lambda: self.spin_change(0, self.ui.spinBox_1.value()))
        self.ui.spinBox_2.valueChanged.connect(lambda: self.spin_change(1, self.ui.spinBox_2.value()))

        self.show()

    def load_ct_series(self, button_id: int):
        dialog = QFileDialog()
        dialog.exec()
        files = dialog.selectedFiles()

        if button_id:
            self.img[button_id] = np.flip(np.rot90(sitk.GetArrayFromImage(sitk.ReadImage(files[0])), axes=(1, 2)), 2)[::-1]
        else:
            self.img[button_id] = np.flip(sitk.GetArrayFromImage(sitk.ReadImage(files[0])), 2)

        self.sliders[button_id].setMaximum(self.img[button_id].shape[0] - 1)
        self.spinBoxes[button_id].setMaximum(self.img[button_id].shape[0] - 1)
        self.filenames[button_id].setText(files[0].split('/')[-1])
        self.ids[button_id].setText("ID: 0")

        self.draw_image(self.img[button_id][0], button_id)

    def slide(self, slider_id: int):
        id = self.sliders[slider_id].value()
        self.ids[slider_id].setText(f"ID: {id}")

    def slider_released(self, slider_id: int, value: int):
        self.ids[slider_id].setText(f"ID: ")
        self.spinBoxes[slider_id].setValue(value)

    def spin_change(self, spin_id: int, value: int):
        self.sliders[spin_id].setValue(value)
        self.ids[spin_id].setText("ID: ")
        self.draw_image(self.img[spin_id][value], spin_id)

    def draw_image(self, img: np.array, widget_id: int):
        self.graphs[widget_id].ax.imshow(img, cmap='grey')
        self.graphs[widget_id].ax.axis('off')
        self.graphs[widget_id].draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LungCTViewApp()
    sys.exit(app.exec())
