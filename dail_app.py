from PyQt5.QtWidgets import QDialog, QDial, QHBoxLayout, QApplication, QSpinBox
import sys
from qt_material import *

class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        apply_stylesheet(app, theme='dark_amber.xml')
        self.setWindowTitle("the dail app")
        self.setGeometry(40, 40, 450, 300)
        self.intUi()

    def intUi(self):
        dail = QDial()
        dail.setNotchesVisible(True)
        spin = QSpinBox()
        hbox = QHBoxLayout()
        hbox.addWidget(dail)
        hbox.addWidget(spin)
        self.setLayout(hbox)
        dail.valueChanged.connect(spin.setValue)
        spin.valueChanged.connect(dail.setValue)

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()