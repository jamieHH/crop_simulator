import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello world')        
        
        self.stacked_layout = QStackedLayout()
        self.create_initial_layout()
        self.create_hello_layout()
        self.stacked_layout.setCurrentIndex(0)
        
        self.initial_widget = QWidget()
        self.initial_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.initial_widget)        


    def create_initial_layout(self):
        #create widgets
        self.label = QLabel('Enter your name')
        self.text_box = QLineEdit()
        self.button = QPushButton('Submit')
        #create layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.button)
        #set central widget
        self.initial_widget = QWidget()
        self.initial_widget.setLayout(self.layout)
        #add to stacked_layout
        self.stacked_layout.addWidget(self.initial_widget)        
        #connections
        self.button.clicked.connect(self.switch_layout)


    def create_hello_layout(self):
        self.hello_label = QLabel()
        self.back_button = QPushButton('Back')
        #
        self.hello_layout = QVBoxLayout()
        #
        self.hello_layout.addWidget(self.hello_label)
        self.hello_layout.addWidget(self.back_button)
        #
        self.hello_widget = QWidget()
        self.hello_widget.setLayout(self.hello_layout)
        #
        self.stacked_layout.addWidget(self.hello_widget)
        #conections
        self.back_button.clicked.connect(self.switch_back)


    def switch_layout(self):
        self.stacked_layout.setCurrentIndex(1)
        name = self.text_box.text()
        self.hello_label.setText('Hello {0}'.format(name))
        


    def switch_back(self):
        self.stacked_layout.setCurrentIndex(0)
        self.text_box.setText(str(''))
        
        
if __name__ == "__main__":
    application = QApplication(sys.argv)#creates new app
    window = MainWindow()               #creates instance of main window
    window.show()                       #make instance visable
    window.raise_()                     #raise instance to top window stack
    application.exec()                  #monitor app for events
    
