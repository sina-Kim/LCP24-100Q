
import sys
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QSlider
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from LCP24_100Q import LCP24_100Q


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        # self.controller = LCP24_100Q('PORT0')

    def initUI(self):
        vbox = QVBoxLayout()
        hbox_in = QHBoxLayout()
        vbox_in = QVBoxLayout()
        self.setLayout(vbox)

        buttons = []
        for i in range(0, 3):
            button = QPushButton('MODE {:02}'.format(i+1), parent=self)
            button.setFixedHeight(50)
            buttons.append(button)
            hbox_in.addWidget(buttons[i])

        sliders = []
        for i in range(0, 4):
            slide = QSlider(Qt.Horizontal, parent=self)
            slide.setRange(0, 255)
            slide.setTickInterval(10)
            slide.setTickPosition(QSlider.TicksAbove)
            sliders.append(slide)
            vbox_in.addWidget(sliders[i])
        
        vbox.addLayout(hbox_in)
        vbox.addLayout(vbox_in)

        self.setWindowTitle('조명 제어')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
