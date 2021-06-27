from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import matplotlib.pyplot as plt
import numpy as np
#from PyQt5.uic import loadUiType
#MainUI,_ = loadUiType('schedular.ui')
from main_of_priority_non_preemptive import *
from osfcfssjf import *
from main_of_priority_preemptive import *
from TRIALRR import *

from main import Ui_MainWindow

class Main(QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("CPU Schedular")
        self.setGeometry(200,300,600,500)


        ############fcfs####################3##
        self.lineEditfcfs.textChanged.connect(self.newrowfcfs) #input noof process and adding rows
        self.tableWidgetfcfs.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #stretching table
        self.pushButton_10.clicked.connect(self.readtabledatafcfs) # read data from table
        #self.pushButton_10.clicked.connect(self.printfcfs) #print waiting time
        self.push_Buttonclear.clicked.connect(self.clearfcfs)


        #######sjf###############
        self.lineEditsjf.textChanged.connect(self.newrowsjf)  # input noof process and adding rows
        self.tableWidgetsjf.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # stretching table
        self.pushButton_4.clicked.connect(self.readtabledatasjf)  # read data from table
        #self.pushButton_4.clicked.connect(self.printsjf)  # print waiting time
        self.pushButton_4.clicked.connect(self.checksjf)
        self.push_Buttonclear1.clicked.connect(self.clearsjf)



######functions fcfs##############
    def printfcfs(self,t):
        self.lineEdit_2.setText(t)  # return waiting time

    def newrowfcfs(self, text):
        if (text is ""):
            self.lineEditfcfs.clear()
        else:
            noofrows = int(text)
            self.tableWidgetfcfs.setRowCount(noofrows)

    def readtabledatafcfs(self):
        not_valid=0
        rowCount = self.tableWidgetfcfs.rowCount()
        columnCount = self.tableWidgetfcfs.columnCount()
        x = 0
        for column in range(columnCount):
            columnData = ''
            x = x + 1
            for row in range(rowCount):
                widgetItem = self.tableWidgetfcfs.item(row, column)
                if (widgetItem and widgetItem.text):
                    columnData = columnData + ' ' + widgetItem.text()
                else:
                    columnData = columnData + ' ' + '-1'
            if (x == 1):
                arrival = columnData.split()
                if (('-1') in arrival):
                    QMessageBox.about(self, "ERROR", "There is an empty cell!")
                    not_valid=1
                else:
                    for i in range(0, len(arrival)):
                        arrival[i] = float(arrival[i])
                        if (arrival[i]<0):
                            QMessageBox.about(self, "ERROR", "Only positive numbers are allowed")
                            not_valid=1
                    print(arrival, 1, "\n")

            if (x == 2):
                burst = columnData.split()
                if (('-1') in burst):
                    QMessageBox.about(self, "ERROR", "There is an empty cell!")
                    not_valid=1
                else:
                    for j in range(0, len(burst)):
                        burst[j] = float(burst[j])
                        if (burst[j]<0):
                            QMessageBox.about(self, "ERROR", "Only positive numbers are allowed")
                            not_valid=1
                    print(burst, 2, "\n")

###############################################checking#########################################################
        if(not_valid==1):
            QMessageBox.about(self, "ERROR", "please,check your input!")
        else:
            wtimef = waiting_time_fcfs(joining(burst, arrival), fcfs(joining(burst, arrival)),fcfs_idl(joining(burst,arrival)))
            self.printfcfs(wtimef)

        #print(waitingtime)

    def clearfcfs(self):
        self.lineEditfcfs.clear()
        self.lineEdit_2.clear()
        self.tableWidgetfcfs.clearContents()
        self.tableWidgetfcfs.setRowCount(0)


#########functions sjf#################
    def clearsjf(self):
        self.lineEditsjf.clear()
        self.lineEdit_4.clear()
        #if(self.radioButton_2.isChecked()):
            #self.radioButton_2.checked==False
        #self.radioButton.setChecked(False)

        self.tableWidgetsjf.clearContents()
        self.tableWidgetsjf.setRowCount(0)

    def printsjf(self,t):
        if(self.radioButton.isChecked()): ##perimative
            self.lineEdit_4.setText(t)  ## return waiting time
        elif(self.radioButton_2.isChecked()): ##nonperimative
            self.lineEdit_4.setText(t)

        '''def printsjf(self, text):
        if (text is ""):
            self.lineEdit_4.clear()
        else:
            self.lineEdit_4.setText('23') # return waiting time'''

    def checksjf(self):
        if self.radioButton.isChecked():
            self.perimative()

        elif self.radioButton_2.isChecked():
            self.nonperimative()
        else:
            QMessageBox.about(self, "ERROR", "please choose perimative or non perimative")

    def newrowsjf(self, text):
        if (text is ""):
            self.lineEditsjf.clear()
        else:
            noofrows = int(text)
            self.tableWidgetsjf.setRowCount(noofrows)

    def readtabledatasjf(self):
        not_valid=0
        rowCount = self.tableWidgetsjf.rowCount()
        columnCount = self.tableWidgetsjf.columnCount()
        x = 0
        for column in range(columnCount):
            columnData = ''
            x = x + 1
            for row in range(rowCount):
                widgetItem = self.tableWidgetsjf.item(row, column)
                if (widgetItem and widgetItem.text):
                    columnData = columnData + ' ' + widgetItem.text()
                else:
                    columnData = columnData + ' ' + '-1'
            if (x == 1):
                arrival = columnData.split()
                if (('-1') in arrival):
                    QMessageBox.about(self, "ERROR", "There is an empty cell!")
                    not_valid=1
                else:
                    for i in range(0, len(arrival)):
                        arrival[i] = float(arrival[i])
                        if (arrival[i]<0):
                            QMessageBox.about(self, "ERROR", "Only positive numbers are allowed")
                            not_valid=1
                    print(arrival, 1, "\n")
            if (x == 2):
                burst = columnData.split()
                if (('-1') in burst):
                    QMessageBox.about(self, "ERROR", "There is an empty cell!")
                    not_valid=1
                else:
                    for j in range(0, len(burst)):
                        burst[j] = float(burst[j])
                        if (burst[j]<0):
                            QMessageBox.about(self, "ERROR", "Only positive numbers are allowed")
                            not_valid=1
                    print(burst, 2, "\n")
###################################checking#############################################################
        if(not_valid==1):
            QMessageBox.about(self, "ERROR", "please,check your input!")
        else:
            if (self.radioButton.isChecked()):
                twaitingp = waiting_time_psjf(joining(burst, arrival), preemptive_sjf(joining(burst, arrival)),preemptive_idl(joining(burst,arrival)))
                self.printsjf(twaitingp)

            elif (self.radioButton_2.isChecked()):
                twaitingnp = waiting_time_nonsjf(joining(burst, arrival), non_preemp_sjf(joining(burst, arrival)),sjf_idl(joining(burst,arrival)))
                self.printsjf(twaitingnp)


############## for sjf and periority############################
    def nonperimative(self): #general
        nonperimative=1
        perimative=0
        print("non")


    def perimative(self): #general
        perimative=1
        nonperimative=0
        print("p")



def main():
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

