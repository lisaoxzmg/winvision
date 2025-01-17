import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class WinVision(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('WinVision - Display Readability Enhancer')
        self.setGeometry(100, 100, 400, 300)

        layout = QtWidgets.QVBoxLayout()

        # Brightness control
        self.brightness_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.brightness_slider.setRange(0, 100)
        self.brightness_slider.setValue(50)
        self.brightness_slider.valueChanged.connect(self.adjust_brightness)
        layout.addWidget(QtWidgets.QLabel('Brightness'))
        layout.addWidget(self.brightness_slider)

        # Contrast control
        self.contrast_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.contrast_slider.setRange(0, 100)
        self.contrast_slider.setValue(50)
        self.contrast_slider.valueChanged.connect(self.adjust_contrast)
        layout.addWidget(QtWidgets.QLabel('Contrast'))
        layout.addWidget(self.contrast_slider)

        # Color filter dropdown
        self.filter_dropdown = QtWidgets.QComboBox(self)
        self.filter_dropdown.addItem("Normal")
        self.filter_dropdown.addItem("Grayscale")
        self.filter_dropdown.addItem("Inverted")
        self.filter_dropdown.addItem("High Contrast")
        self.filter_dropdown.currentIndexChanged.connect(self.apply_filter)
        layout.addWidget(QtWidgets.QLabel('Color Filter'))
        layout.addWidget(self.filter_dropdown)

        self.setLayout(layout)

    def adjust_brightness(self):
        value = self.brightness_slider.value()
        print(f"Adjusting brightness to {value}")

    def adjust_contrast(self):
        value = self.contrast_slider.value()
        print(f"Adjusting contrast to {value}")

    def apply_filter(self):
        filter_name = self.filter_dropdown.currentText()
        print(f"Applying filter: {filter_name}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    winVision = WinVision()
    winVision.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()