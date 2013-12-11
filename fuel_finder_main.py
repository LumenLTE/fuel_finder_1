import sys
import os


from PyQt4.QtCore import *
from PyQt4.QtGui import *

from fuel_graphics_scene import *

#MOST COMMENTED OUT FOR DISPLAY PURPOSES

class MainDisplayWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fuel Price Finder")
        self.setInitialLayout()


    def setInitialLayout(self):
        #create some widgets for a left side test
        self.left_label = QLabel("LEFT WIDGET")
        self.button_1_left = QPushButton("+")
        self.button_2_left = QPushButton("-")
        self.left_button = QPushButton("<")
        self.up_button = QPushButton("^")
        self.right_button = QPushButton(">")
        self.down_button = QPushButton("v")
##        self.button_3_left = QPushButton("BUTTON3")
##        self.button_4_left = QPushButton("BUTTON4")

##        #create some widgets for a right side test
##        self.right_label = QLabel("RIGHT WIDGET")
##        self.button_1_right = QPushButton("BUTTON1")
##        self.button_2_right = QPushButton("BUTTON2")
##        self.button_3_right = QPushButton("BUTTON3")
##        self.button_4_right = QPushButton("BUTTON4")

        #add graphics scene
        self.middle_graphics = QGraphicsView()
        self.graphics_scene = FuelFinderGraphicsScene()
        self.middle_graphics.setScene(self.graphics_scene)
        self.middle_graphics.setFixedHeight(300)
        self.middle_graphics.setFixedWidth(400)
        self.middle_graphics.setSceneRect(0,0, 300, 400)
        self.middle_graphics.setVerticalScrollBarPolicy(1)
        
        #create layout
        self.main_layout = QHBoxLayout()
        self.left_layout = QGridLayout()
        self.middle_layout = QGridLayout()
        self.right_layout = QGridLayout()

        #add left test widgets to layout
        self.left_layout.addWidget(self.button_1_left, 0, 0)
        self.left_layout.addWidget(self.button_2_left, 1, 0)
        
##        self.left_layout.addWidget(self.button_3_left, 1, 0)
##        self.left_layout.addWidget(self.button_4_left, 1, 1)

        #add right test widgets to layout
##        self.right_layout.addWidget(self.button_1_right, 0, 0)
##        self.right_layout.addWidget(self.button_2_right, 0, 1)
##        self.right_layout.addWidget(self.button_3_right, 1, 0)
##        self.right_layout.addWidget(self.button_4_right, 1, 1)

        #add graphics to mid
        self.middle_layout.addWidget(self.middle_graphics)

        #create widgets containing each layout
        self.left_widget = QWidget()
        self.middle_widget = QWidget()
        self.right_widget = QWidget()

        #add widgets to corresponding layout
        self.left_widget.setLayout(self.left_layout)
        self.middle_widget.setLayout(self.middle_layout)
        #self.right_widget.setLayout(self.right_layout)

        #add widgets to main layout
        self.main_layout.addWidget(self.left_widget)
        self.main_layout.addWidget(self.middle_widget)
        #self.main_layout.addWidget(self.right_widget)

        #create main widget and set it as central
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)



def main():
    fuel_finder_app = QApplication(sys.argv)

    fuel_finder_window = MainDisplayWindow()

    fuel_finder_window.show()
    fuel_finder_window.raise_()

    fuel_finder_app.exec_()


if __name__ == "__main__":
    main()
