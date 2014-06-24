import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Potato_class import *
from Wheat_class import *

from RadioButtonWidget_class import * #provides radio buton widget

class CropWindow(QMainWindow):
    """This class creates a window to observe the growth of crop simulation"""

    #constructor
    def __init__(self):
        super().__init__() # call super class constructor
        self.setWindowTitle('Crop Simulator') # set window title
        self.create_select_crop_layout()

    def create_select_crop_layout(self):
        self.crop_radio_buttons = RadioButtonWidget('Crop Simulation','Select a crop',('Wheat','Potato'))
        self.instantiate_button = QPushButton('Create Crop')

        #create layoutto hold the widgets
        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.crop_radio_buttons)
        self.initial_layout.addWidget(self.instantiate_button)

        self.select_crop_widget = QWidget()
        self.select_crop_widget.setLayout(self.initial_layout)

        self.setCentralWidget(self.select_crop_widget)

        #connections
        self.instantiate_button.clicked.connect(self.instantiate_crop)

    def instantiate_crop(self):
        croy_type = self.crop_radio_buttons.selected_button()
        if crop_type == 1:
            self.simulated_crop = Wheat()
        elif crop_type == 2:
            self.simulated_crop = Potato()
        print(self.simulated_crop)
        

def main():
    crop_simulation = QApplication(sys.argv) #create new application
    crop_window = CropWindow() #create new instance of main window
    crop_window.show() #make instance visible
    crop_window.raise_() #raise to top window stack
    crop_simulation.exec_() #monitor application for events

if __name__ == "__main__":
    main()
