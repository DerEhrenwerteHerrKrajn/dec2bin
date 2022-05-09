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
        self.zahlen = [QLabel('8', self), QLabel('4', self), QLabel('2', self), QLabel('1', self)]
        for x in self.zahlen:
            hlayoutLabels.addWidget(x)

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
        print("Start: " + str(labelsValue))
        on = "background-color: rgb(0, 180, 0)"
        off = "background-color: rgb(180, 0, 0)"
        for i in range(4):
            div = 2 ** (3 - i)
            self.zahlen[i].setStyleSheet(off)
            if labelsValue >= div:
                    self.zahlen[i].setStyleSheet(on)
                    leds[i].on()
                    labelsValue -= div
        print("________")


app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()