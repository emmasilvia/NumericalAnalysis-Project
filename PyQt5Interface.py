# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 20:11:13 2022

@author: Cris
"""

from functii2 import *
import PyQt5.QtWidgets as qtw
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDialog,
    QDoubleSpinBox,
    QFontComboBox,
    QGridLayout,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)
import PyQt5.QtGui as qtg
import sys
from PyQt5.QtCore import QRegExp
from PyQt5.QtCore import Qt
from scipy.optimize import fsolve
from sympy import *
from matplotlib import pyplot as plt
from time import time
import numpy as np
import math

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        #punem titlu
        self.setWindowTitle("Aproximarea solutiilor ecuatiilor neliniare")
        #layout vertical
        self.setLayout(QVBoxLayout())
        
#layout si design background
        self.left = 50
        self.top = 50
        self.width = 700
        self.height = 280

        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.gray)
        self.setPalette(p)
        
#labels pt a,b,f(x)
   
        label1 = QLabel("Adaugati valori:")
        self.layout().addWidget(label1)
        label1.setFont(qtg.QFont('Times', 10))
       
        
        label2 = QLabel("a=")
        self.layout().addWidget(label2)
        entry_a = QLineEdit()
        entry_a.setObjectName("Introduceti capatul a")
        self.layout().addWidget(entry_a)
        label2.setFont(qtg.QFont('Times', 10))
        
        label2_2 = QLabel("*obligatoriu si a<b")
        self.layout().addWidget(label2_2)
        
        #validator1 = validators.notEmpty()
        #entry_a.setValidator(validator1)
        reg_ex = QRegExp("[0-9]+.[0-9]{,5}")
        input_validator = qtg.QRegExpValidator(reg_ex, entry_a)
        entry_a.setValidator(input_validator)
        
        label3 = QLabel("b=")
        self.layout().addWidget(label3)
        entry_b = QLineEdit()
        entry_b.setObjectName("Introduceti capatul b")
        entry_b.setValidator(input_validator)
        self.layout().addWidget(entry_b)
        label3.setFont(qtg.QFont('Times', 10))
        
        label3_3 = QLabel("*obligatoriu si b>a")
        self.layout().addWidget(label3_3)
        
        label4 = qtw.QLabel("f(x)=")
        self.layout().addWidget(label4)
        entry_f = qtw.QLineEdit()
        entry_f.setObjectName("Introduceti f(x)")
        #entry_f.setText("")
        self.layout().addWidget(entry_f)
        label4.setFont(qtg.QFont('Times', 10))
        label4_4 = QLabel("*obligatoriu")
        self.layout().addWidget(label4_4)
        
# #criterii de stopare
        label6 = qtw.QLabel("Introduceti criteriile de stopare:")
        self.layout().addWidget(label6)
        label6.setFont(qtg.QFont('Times', 10))
        
        label6_6 = QLabel("*obligatoriu cel putin unul in functie de metoda aleasa")
        self.layout().addWidget(label6_6)
        

        
        label7 = qtw.QLabel("Numarul de iteratii: ")
        self.layout().addWidget(label7)
        entry_it = qtw.QLineEdit()
        entry_it.setObjectName("Introduceti nr de it: ")
        self.layout().addWidget(entry_it)
        entry_it.setValidator(input_validator)
        label7.setFont(qtg.QFont('Times', 10))
        
        label8 = qtw.QLabel("Valoare eroare: ")
        self.layout().addWidget(label8)
        entry_err = qtw.QLineEdit()
        entry_err.setObjectName("Introduceti err: ")
        self.layout().addWidget(entry_err)
        entry_it.setValidator(input_validator)
        label8.setFont(qtg.QFont('Times', 10))
        
        label5 = QLabel("Alegeti metoda:")
        self.layout().addWidget(label5)
        label5.setFont(qtg.QFont('Times', 10))
    
#butoane metode
        x = Symbol("x")
        fct = entry_f.text()
        
        button_bis_err = QPushButton("Bisectie eroare", clicked=lambda:bisectie_eroare())
        self.layout().addWidget(button_bis_err)
        button_bis_err.setStyleSheet("background-color : pink")
        button_bis_err.setFont(qtg.QFont('Times', 10))
     
        button_bis_it = QPushButton("Bisectie iteratii", clicked=lambda:bisectie_iteratii())
        self.layout().addWidget(button_bis_it)
        button_bis_it.setStyleSheet("background-color : pink")
        button_bis_it.setFont(qtg.QFont('Times', 10))
        
        button_tan_er = QPushButton("Tangenta eroare", clicked=lambda:tangenta_eroare())
        self.layout().addWidget(button_tan_er)
        button_tan_er.setStyleSheet("background-color : pink")
        button_tan_er.setFont(qtg.QFont('Times', 10))
        
        button_tan_it = QPushButton("Tangenta iteratii", clicked=lambda:tangenta_iteratii())
        self.layout().addWidget(button_tan_it)
        button_tan_it.setStyleSheet("background-color : pink")
        button_tan_it.setFont(qtg.QFont('Times', 10))
        
        button_coarda_er = QPushButton("Coarda eroare", clicked=lambda:coarda_eroare())
        self.layout().addWidget(button_coarda_er)
        button_coarda_er.setStyleSheet("background-color : pink")
        button_coarda_er.setFont(qtg.QFont('Times', 10))
        
        button_coarda_it = QPushButton("Coarda iteratii", clicked=lambda:coarda_iteratii())
        self.layout().addWidget(button_coarda_it)
        button_coarda_it.setStyleSheet("background-color : pink")
        button_coarda_it.setFont(qtg.QFont('Times', 10))
        
        button_contr_er = QPushButton("Contractii eroare", clicked=lambda:contractii_eroare())
        self.layout().addWidget(button_contr_er)
        button_contr_er.setStyleSheet("background-color : pink")
        button_contr_er.setFont(qtg.QFont('Times', 10))
        
        button_contr_it = QPushButton("Contractii iteratii", clicked=lambda:contractii_iteratii())
        self.layout().addWidget(button_contr_it)
        button_contr_it.setStyleSheet("background-color : pink")
        button_contr_it.setFont(qtg.QFont('Times', 10))
        
        lb = QLabel("",self)
        self.layout().addWidget(lb)
        lb.setFont(qtg.QFont('Times', 10))
        
        label9 = qtw.QLabel("Valoare x: ")
        self.layout().addWidget(label9)
        entry_x = qtw.QLineEdit()
        entry_x.setObjectName("x= ")
        #entry_err.setText("")
        self.layout().addWidget(entry_x)
        label9.setFont(qtg.QFont('Times', 10))
        
        
        label_valTimp = qtw.QLabel("Valoare timp: ")
        self.layout().addWidget(label_valTimp)
        entry_time = qtw.QLineEdit()
        entry_time.setObjectName("Durata= ")
        self.layout().addWidget(entry_time)
        label_valTimp.setFont(qtg.QFont('Times', 10))
     

        label_valErr = qtw.QLabel("Valoare eroare: ")
        self.layout().addWidget(label_valErr)
        entry_eroare = qtw.QLineEdit()
        entry_eroare.setObjectName("Eroare= ")
        self.layout().addWidget(entry_eroare)
        label_valErr.setFont(qtg.QFont('Times', 10))
        
        label_graph = qtw.QLabel("")
        self.layout().addWidget(label_graph)
        
        # self.x_val = np.linspace(entry_a.text(), entry_b.text(), 100)
        z = np.arange(0, 1, 100)
        # setting the corresponding y - coordinates
        y = entry_f.text()
  
        # plotting the points
        plt.plot(z, y)
  
        # function to show the plot
        plt.show()
        
        def bisectie_eroare():
            t0=time()
            x1 = bisectie_err(lambdify(x, entry_f.text()), float(entry_a.text()), float(entry_b.text()), float(entry_err.text()))
            t1=time()
            durata=t1-t0
            entry_x.setText(str(x1))
            
            entry_time.setText(str(durata))
            
            fs=entry_f.text()+'-x'
            fsl=lambdify(x, fs)
            x0 = np.random.rand() * (float(entry_b.text()) - float(entry_a.text())) + float(entry_a.text())
            err_abs1 = fsolve(fsl, x0)
            dif_err1 = x1-err_abs1
            
            entry_eroare.setText(str(dif_err1))
            
        def bisectie_iteratii():
            t0=time()
            x2 = bisectie_it(lambdify(x, entry_f.text()), float(entry_a.text()), float(entry_b.text()), int(entry_it.text()))
            t1=time()
            durata=t1-t0
            entry_x.setText(str(x2))
        
            entry_time.setText(str(durata))
            
            fs=entry_f.text()+'-x'
            fsl=lambdify(x, fs)
            x0 = np.random.rand() * (float(entry_b.text()) - float(entry_a.text())) + float(entry_a.text())
            err_abs2 = fsolve(fsl, x0)
            dif_err2 = x2-err_abs2
            
            entry_eroare.setText(str(dif_err2))
            
        def tangenta_eroare():
            t0=time()
            x3 = tangenta_err(entry_f.text(), float(entry_a.text()), float(entry_b.text()), float(entry_err.text()))
            t1=time()
            durata=t1-t0
            entry_x.setText(str(x3))
            
            entry_time.setText(str(durata))
            
            fs=entry_f.text()+'-x'
            fsl=lambdify(x, fs)
            x0 = np.random.rand() * (float(entry_b.text()) - float(entry_a.text())) + float(entry_a.text())
            err_abs3 = fsolve(fsl, x0)
            dif_err3 = x3-err_abs3
            
            entry_eroare.setText(str(dif_err3))
        
        def tangenta_iteratii():
            t0=time()
            x4 = tangenta_it(entry_f.text(), float(entry_a.text()), float(entry_b.text()), int(entry_it.text()))
            t1=time()
            durata=t1-t0
            entry_x.setText(str(x4))
            
            entry_time.setText(str(durata))
            
            fs=entry_f.text()+'-x'
            fsl=lambdify(x, fs)
            x0 = np.random.rand() * (float(entry_b.text()) - float(entry_a.text())) + float(entry_a.text())
            err_abs4 = fsolve(fsl, x0)
            dif_err4 = x4-err_abs4
            
            entry_eroare.setText(str(dif_err4))
            
        def coarda_eroare():
            t0=time()
            x5 = coarda_err(entry_f.text(), float(entry_a.text()), float(entry_b.text()), float(entry_err.text()))
            t1=time()
            durata=t1-t0
            entry_x.setText(str(x5))
            
            entry_time.setText(str(durata))
            
            fs=entry_f.text()+'-x'
            fsl=lambdify(x, fs)
            x0 = np.random.rand() * (float(entry_b.text()) - float(entry_a.text())) + float(entry_a.text())
            err_abs5 = fsolve(fsl, x0)
            dif_err5 = x5-err_abs5
            
            entry_eroare.setText(str(dif_err5))
        
        def coarda_iteratii():
            t0=time()
            x6 = coarda_it(entry_f.text(), float(entry_a.text()), float(entry_b.text()), int(entry_it.text()))
            t1=time()
            durata=t1-t0
            entry_x.setText(str(x6))
            
            entry_time.setText(str(durata))
            
            fs=entry_f.text()+'-x'
            fsl=lambdify(x, fs)
            x0 = np.random.rand() * (float(entry_b.text()) - float(entry_a.text())) + float(entry_a.text())
            err_abs6 = fsolve(fsl, x0)
            dif_err6 = x6-err_abs6
            
            entry_eroare.setText(str(dif_err6))
        
        def contractii_eroare():
            t0=time()
            x7 = contractii_err(entry_f.text(), float(entry_a.text()), float(entry_b.text()), float(entry_err.text()))
            t1=time()
            durata=t1-t0
            entry_x.setText(str(x7))
            
            entry_time.setText(str(durata))
            
            fs=entry_f.text()+'-x'
            fsl=lambdify(x, fs)
            x0 = np.random.rand() * (float(entry_b.text()) - float(entry_a.text())) + float(entry_a.text())
            err_abs7 = fsolve(fsl, x0)
            dif_err7 = x7-err_abs7
            
            entry_eroare.setText(str(dif_err7))
            
        def contractii_iteratii():
            t0=time()
            x8 = contractii_it(entry_f.text(), float(entry_a.text()), float(entry_b.text()), int(entry_it.text()))
            t1=time()
            durata=t1-t0
            entry_x.setText(str(x8))
            
            entry_time.setText(str(durata))
       
            fs=entry_f.text()+'-x'
            fsl=lambdify(x, fs)
            x0 = np.random.rand() * (float(entry_b.text()) - float(entry_a.text())) + float(entry_a.text())
            err_abs8 = fsolve(fsl, x0)
            dif_err8 = x8-err_abs8
            
            entry_eroare.setText(str(dif_err8))

#TO DO - afisare grafic                                        
        self.show()
        
app = QApplication([])
mw = MainWindow()

app.exec_()