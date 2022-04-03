#!/usr/bin/env python3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber, QCheckBox, QSlider
from PyQt5.QtCore import Qt, QSize, QTimer
from gpiozero import LEDBoard
from time import sleep
from threading import Thread

leds = LEDBoard(18, 23, 24, 25, pwm=True)

# Klasse für das Hauptfenster
class MyWindow(QMainWindow):
    def __init__(self): 

        super().__init__()
        self.setMinimumSize(QSize(250, 120)) 
        self.setWindowTitle('Dezimalumwandler Krajina Luka') 

        wid = QWidget(self)
        self.setCentralWidget(wid)


        hlayoutSlider = QHBoxLayout()

        self.binSlider = QSlider(Qt.Horizontal)
        self.binSlider.setGeometry(30, 40, 150, 50)
        self.binSlider.setRange(0, 15)
        self.binSlider.setPageStep(1) 
        self.binSlider.setTickPosition(2)
        hlayoutSlider.addWidget(self.binSlider)

        self.zahlanzeige = QLabel('0', self)
        hlayoutSlider.addWidget(self.zahlanzeige)

        hlayoutLabels = QHBoxLayout()
        #Funktioniert nicht
        #self.bitlabels = ['zahl8', 'zahl4', 'zahl2', 'zahl1']
        #for self.bitlabel in self.bitlabels:
        #    hlayoutLabels.addWidget(self.bitlabel)
        self.zahl8 = QLabel('8', self)
        self.zahl4 = QLabel('4', self)
        self.zahl2 = QLabel('2', self)
        self.zahl1 = QLabel('1', self)
        hlayoutLabels.addWidget(self.zahl8)
        hlayoutLabels.addWidget(self.zahl4)
        hlayoutLabels.addWidget(self.zahl2)
        hlayoutLabels.addWidget(self.zahl1)

        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayoutSlider)
        vlayout.addLayout(hlayoutLabels)
        wid.setLayout(vlayout)

        self.show()

        self.binSlider.valueChanged[int].connect(self.bin2dec) 
        self.binSlider.valueChanged[int].connect(self.checker)  


    def bin2dec(self):
        sliderValue = str(self.binSlider.value())
        self.zahlanzeige.setText(sliderValue)
    
    def checker(self):
        labelsValue = (self.binSlider.value())
        if(labelsValue >= 8):
            self.zahl8.setStyleSheet("background-color: rgb(180, 0, 0)")
            labelsValue = labelsValue - 8
            led8 = 1
        else:
            self.zahl8.setStyleSheet("background-color: rgb(0, 180, 0)")
            led8 = 0
        if(labelsValue >= 4):
            self.zahl4.setStyleSheet("background-color: rgb(180, 0, 0)")
            labelsValue = labelsValue - 4
            led4 = 1
        else:
            self.zahl4.setStyleSheet("background-color: rgb(0, 180, 0)")
            led4 = 0
        if(labelsValue >= 2):
            self.zahl2.setStyleSheet("background-color: rgb(180, 0, 0)")
            labelsValue = labelsValue - 2
            led2 = 1
        else:
            self.zahl2.setStyleSheet("background-color: rgb(0, 180, 0)")
            led2 = 0
        if(labelsValue >= 1):
            self.zahl1.setStyleSheet("background-color: rgb(180, 0, 0)")
            labelsValue = labelsValue - 1
            led1 = 1
        else:
            self.zahl1.setStyleSheet("background-color: rgb(0, 180, 0)")
            led1 = 0
        leds.value = (led8, led4, led2, led1)


app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()