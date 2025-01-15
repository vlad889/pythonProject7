import sys
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.nagad)
        # Обратите внимание: имя элемента такое же как в QTDesigner
        self.diameter = random.randint(50, (434 - 20))
        self.x = (434 - self.diameter)
        self.y = (631 - self.diameter)#не списано!!! это на случай переделки!
        self.nach = False

    
    def nagad(self):
        self.nach = True
        self.pushButton.setVisible(False)
        self.repaint()


    def paintEvent(self, event):
        if not self.nach:
            return
        painter = QPainter(self)
        painter.setBrush(QColor('yellow'))
        painter.drawEllipse(100, 100, self.x, self.x)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
