# PyQt5 Tutorials: https://www.tutorialspoint.com/pyqt5/index.htm
# Part-1: Hello World

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class window(QWidget):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        self.resize(500, 200)  # Set the size for the GUI window
        self.setWindowTitle("PyQt5")  # Set the title of the GUI window
        self.label = QLabel(self)  # ?
        self.label.setText("Hello World")  # Set the words to show in the GUI window
        font = QFont()  # The QFont class specifies a query for a font used for drawing text
        font.setFamily(
            "Arial")  # Sets the family name of the font. The name is case-insensitive and may include a foundry name.
        font.setPointSize(32)  # Sets the point size to pointSize. The point size must be greater than zero.
        self.label.setFont(font)  # apply the font setting to the "self.label.setText("Hello World")"
        self.label.move(50, 20)  # move the "setText("Hello World")" within the GUI window


def Qt_1():
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    Qt_1()
