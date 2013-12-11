from PyQt4.QtCore import *
from PyQt4.QtGui import *

class FuelFinderGraphicsScene(QGraphicsScene):
    def __init__(self):
        super().__init__()

        self.background_brush = QBrush()
        self.background_image = QPixmap("images/background.png")
        self.background_brush.setTexture(self.background_image)
        self.setBackgroundBrush(self.background_brush)
