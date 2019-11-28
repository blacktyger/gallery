
from images import *
from random import randint
from PyQt5.QtWidgets import QLabel, \
    QMainWindow, QApplication, \
    QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
import sys


img = link_list[randint(0,600)]
print(img)


def next():
    """Slot function."""
    if msg.text():
        msg.setText("")
    else:
        msg.setText("Hello World!")

class Menu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        lay = QVBoxLayout(self.central_widget)

        btn = QPushButton('Next')
        btn.clicked.connect(next)  # Connect clicked to greeting()

        label = QLabel(self)
        pixmap = QPixmap(img)
        pixmap = pixmap.scaledToHeight(966)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        lay.addWidget(btn)
        msg = QLabel('')
        lay.addWidget(msg)
        lay.addWidget(label)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())