import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle('hello world')
        self.create_layout()

    def create_layout(self):
        #create widgets
        self.text_box = QLineEdit()
        self.button = QPushButton('Submit')
        self.label = QLabel('Enter your name')
        #create layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        #set central widget
        self.Widget = QWidget()
        self.Widget.setLayout(self.layout)
        self.setCentralWidget(self.Widget)
        #connections
        self.button.clicked.connect(self.display_name)
        
    def display_name(self):        
        name = self.text_box.text()
        self.label.setText('Hello {0}'.format(name))
        
if __name__ == "__main__":
    application =QApplication(sys.argv) #creates new app
    window = MainWindow()               #creates instance of main window
    window.show()                       #make instance visable
    window.raise_()                     #raise instance to top window stack
    application.exec()                  #monitor app for events
    
