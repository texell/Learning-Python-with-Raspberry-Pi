import turtle
import sys
from PySide.QtCore import *
from PySide.QtGui import *

class TurtleControl(QWidget):
    def __init__(self, turtle):
        super(TurtleControl, self).__init__()
        self.turtle = turtle

        self.left_btn = QPushButton("Left", self)
        self.right_btn = QPushButton("Right", self)
        self.move_btn = QPushButton("Move", self)
        self.distance_spin = QSpinBox()
        self.red_spin = QSpinBox()
        self.red_label = QLabel("Red", self)
        self.green_spin = QSpinBox()
        self.green_label = QLabel("Green", self)
        self.blue_spin = QSpinBox()
        self.blue_label = QLabel("Blue", self)
        self.dcolor_btn = QPushButton("Color", self)
        #self.color_btn = QPushButton("Color", self)
        #uncomment the comments to add a button to start color
        #and recomment the dcolor lines

        self.controlsLayout = QGridLayout()
        self.controlsLayout.addWidget(self.left_btn, 0, 0)
        self.controlsLayout.addWidget(self.right_btn, 0, 1)
        self.controlsLayout.addWidget(self.distance_spin, 1, 0)
        self.controlsLayout.addWidget(self.move_btn, 1, 1)
        self.controlsLayout.addWidget(self.red_label, 2, 0)
        self.controlsLayout.addWidget(self.green_label, 2, 1)
        self.controlsLayout.addWidget(self.blue_label, 2, 2)
        self.controlsLayout.addWidget(self.red_spin, 3, 0)
        self.controlsLayout.addWidget(self.green_spin, 3, 1)
        self.controlsLayout.addWidget(self.blue_spin, 3, 2)
        self.controlsLayout.addWidget(self.dcolor_btn, 4, 0)
        #self.controlsLayout.addWidget(self.color_btn, 4, 0)
        
        self.setLayout(self.controlsLayout)

        self.distance_spin.setRange(0, 100)
        self.distance_spin.setSingleStep(5)
        self.distance_spin.setValue(20)

        self.red_spin.setRange(0, 255)
        self.red_spin.setSingleStep(5)
        self.red_spin.setValue(0)

        self.green_spin.setRange(0, 255)
        self.green_spin.setSingleStep(5)
        self.green_spin.setValue(0)

        self.blue_spin.setRange(0, 255)
        self.blue_spin.setSingleStep(5)
        self.blue_spin.setValue(0)
        
        self.move_btn.clicked.connect(self.move_turtle)
        self.right_btn.clicked.connect(self.turn_turtle_right)
        self.left_btn.clicked.connect(self.turn_turtle_left)
        self.dcolor_btn.clicked.connect(self.dcolor_turtle)
        #self.color_btn.clicked.connect(self.color_turtle)

    def turn_turtle_left(self):
        self.turtle.left(45)

    def turn_turtle_right(self):
        self.turtle.right(45)

    def move_turtle(self):
        self.turtle.forward(self.distance_spin.value())
        #self.turtle.color(self.red_spin.value(),#
        #             self.green_spin.value(),#
        #             self.blue_spin.value())#
        #if uncommenting, recomment the above 3 lines

    #def color_turtle(self):
        #turtle.color(self.red_spin.value(),
                     #self.green_spin.value(),
                     #self.blue_spin.value())

    def dcolor_turtle(self):
        self.color = QColorDialog.getColor()
        self.turtle.color(self.color.getRgb()[:3])
        self.red_spin.setValue(self.color.getRgb()[0])
        self.green_spin.setValue(self.color.getRgb()[1])
        self.blue_spin.setValue(self.color.getRgb()[2])

#setup turtle
window = turtle.Screen()
babbage = turtle.Turtle()
window.colormode(255)

#Creat QT application
app = QApplication(sys.argv)
control_window = TurtleControl(babbage)
control_window.show()

#Enter QT application main loop
app.exec_()
sys.exit()
