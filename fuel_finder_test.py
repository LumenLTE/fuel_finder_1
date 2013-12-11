from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #initialise stacked layout
        self.login_layout = QGridLayout()

        self.map_layout = QGridLayout()

        self.blank = QLabel("             ")

        self.register_layout = QGridLayout()

        self.initial_layout()

        self.select_login.clicked.connect(self.set_login_layout)

        


    def initial_layout(self):
        self.initial_layout = QHBoxLayout()

        self.select_login = QPushButton("\n\n LOGIN \n\n")
        self.select_register = QPushButton("\n\n REGISTER \n\n")
        

        self.initial_widget = QWidget()
        
        self.initial_layout.addWidget(self.blank)
        self.initial_layout.addWidget(self.select_login)
        self.initial_layout.addWidget(self.blank)
        self.initial_layout.addWidget(self.select_register)
        self.initial_layout.addWidget(self.blank)


        self.initial_widget.setLayout(self.initial_layout)

        self.setCentralWidget(self.initial_widget)

        self.setFixedSize(600, 480)

    def set_login_layout(self):
        self.submit_button = QPushButton("Login")
        
        self.username_label = QLabel("Username")
        self.username_line = QLineEdit()
        self.username_line.setMaxLength(10)
        self.username_line.setFixedWidth(120)

        self.password_label = QLabel("Password")
        self.password_line = QLineEdit()
        self.password_line.setMaxLength(10)
        self.password_line.setFixedWidth(120)

        self.login_layout.addWidget(self.blank, 0 ,0)
        self.login_layout.addWidget(self.blank, 1, 0)
        self.login_layout.addWidget(self.username_label, 1, 1)
        self.login_layout.addWidget(self.username_line, 1, 2)
        self.login_layout.addWidget(self.blank, 1, 3)

        self.login_layout.addWidget(self.password_label, 3, 1)
        self.login_layout.addWidget(self.password_line, 3, 2)
        self.login_layout.addWidget(self.blank, 4, 0)

        self.login_layout.addWidget(self.submit_button, 4, 1)
        self.login_layout.addWidget(self.blank, 4, 2)
        self.login_layout.addWidget(self.blank, 5, 0)

        self.login_widget = QWidget()
        self.login_widget.setLayout(self.login_layout)
        self.setCentralWidget(self.login_widget)

        self.setFixedSize(600, 480)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    app.exec_()
    
    
