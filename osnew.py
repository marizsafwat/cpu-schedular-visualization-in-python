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




        ###roundrobin#########
        self.lineEditrr.textChanged.connect(self.newrowrr)  # input noof process and adding rows
        self.tableWidgetrr.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # stretching table
        self.pushButton_5.clicked.connect(self.readtabledatarr)  # read data from table
        #self.pushButton_5.clicked.connect(self.printrr)# print waiting time
        self.pushButton_5.clicked.connect(self.checkrr) # checking if Quantum is empty
        self.push_Buttonclear2.clicked.connect(self.clearround)
        self.lineEdit_7.textChanged.connect(self.Quantum)




        ####periority############
        self.lineEditper.textChanged.connect(self.newrowper)  # input noof process and adding rows
        self.tableWidgetper.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # stretching table
        self.pushButton_7.clicked.connect(self.readtabledataper)  # read data from table
        #self.pushButton_7.clicked.connect(self.printper)  # print waiting time
        self.pushButton_7.clicked.connect(self.checkper)
        self.push_Buttonclear3.clicked.connect(self.clearper)





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

######functions roundrobin##############
    def printrr(self,t):
        self.lineEdit_6.setText(t)  # return waiting time

    def Quantum(self):
        Qtext=self.lineEdit_7.text()
        if (Qtext is ""):
            self.lineEdit_7.clear()
            return 0
        else:
            Q = int(Qtext)
            print(Q)
            return Q

    '''def Quantum(self,text1): #input quantum
        if (text1 is ""):
            self.lineEdit_7.clear()
        else:
            Q = int(text1)
            print(Q,"Main")'''

    def checkrr(self):
        if self.lineEdit_7.text() == "":
            QMessageBox.about(self, "ERROR", "please enter the Quatum number")

    def newrowrr(self, text):
        if (text is ""):
            self.lineEditrr.clear()
        else:
            noofrows = int(text)
            self.tableWidgetrr.setRowCount(noofrows)

    def readtabledatarr(self):
        not_valid=0
        rowCount = self.tableWidgetrr.rowCount()
        columnCount = self.tableWidgetrr.columnCount()
        x = 0
        for column in range(columnCount):
            columnData = ''
            x = x + 1
            for row in range(rowCount):
                widgetItem = self.tableWidgetrr.item(row, column)
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

############################################checking####################################################
        if(not_valid==1):
            QMessageBox.about(self, "ERROR", "please,check your input!")
        else:
            if(self.Quantum() !=0):
                waitingr = main_roundRobin(rowCount, self.Quantum(), arrival, burst)
                self.printrr(waitingr)



    def clearround(self):
        self.lineEditrr.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.tableWidgetrr.clearContents()
        self.tableWidgetrr.setRowCount(0)


######functions periority#############
    def clearper(self):
        self.lineEditper.clear()
        self.lineEdit_9.clear()
        #self.radioButton.setChecked(False)
        #self.radioButton_2.setChecked(False)
        self.tableWidgetper.clearContents()
        self.tableWidgetper.setRowCount(0)


    def printper(self,t):###########################################3
        if (self.radioButton_3.isChecked()):  ##perimative
            self.lineEdit_9.setText(t)  ## return waiting time
        elif (self.radioButton_4.isChecked()):  ##nonperimative
            self.lineEdit_9.setText(t)



    def checkper(self):
        if self.radioButton_3.isChecked():
            self.perimative()

        elif self.radioButton_4.isChecked():
            self.nonperimative()
        else:
            QMessageBox.about(self, "ERROR", "please choose perimative or non perimative")


    def newrowper(self, text):
        if (text is ""):
            self.lineEditper.clear()
        else:
            noofrowsp = int(text)
            self.tableWidgetper.setRowCount(noofrowsp)

    def readtabledataper(self):
        not_valid=0
        rowCount = self.tableWidgetper.rowCount()
        columnCount = self.tableWidgetper.columnCount()
        x = 0
        for column in range(columnCount):
            columnData = ''
            x = x + 1
            for row in range(rowCount):
                widgetItem = self.tableWidgetper.item(row, column)
                if (widgetItem and widgetItem.text):
                    columnData = columnData + ' ' + widgetItem.text()
                else:
                    columnData = columnData + ' ' + '-1'
            if (x == 1):
                arrivalper = columnData.split()
                if (('-1') in arrivalper):
                    QMessageBox.about(self, "ERROR", "There is an empty cell!")
                    not_valid=1
                else:
                    for i in range(0, len(arrivalper)):
                        arrivalper[i] = float(arrivalper[i])
                        if (arrivalper[i]<0):
                            QMessageBox.about(self, "ERROR", "Only positive numbers are allowed")
                            not_valid=1
                    print(arrivalper, 1, "\n")
            if (x == 2):
                burstper = columnData.split()
                if (('-1') in burstper):
                    QMessageBox.about(self, "ERROR", "There is an empty cell!")
                    not_valid=1
                else:
                    for j in range(0, len(burstper)):
                        burstper[j] = float(burstper[j])
                        if (burstper[j]<0):
                            QMessageBox.about(self, "ERROR", "Only positive numbers are allowed")
                            not_valid=1
                    print(burstper, 2, "\n")

            if (x == 3):
                periority = columnData.split()
                if (('-1') in periority):
                    QMessageBox.about(self, "ERROR", "There is an empty cell!")
                    not_valid=1
                else:
                    for k in range(0, len(periority)):
                        periority[k] = float(periority[k])
                        if (periority[k]<0):
                            QMessageBox.about(self, "ERROR", "Only positive numbers are allowed")
                            not_valid=1
                    print(periority, 3, "\n")

###########################################checking########################################################33
        if(not_valid==1):
            QMessageBox.about(self, "ERROR", "please,check your input!")
        else:
            if (self.radioButton_3.isChecked()):
                twaitingp = main_priority_preemptive(rowCount, arrivalper, burstper, periority)
                self.printper(twaitingp)

            elif (self.radioButton_4.isChecked()):
                twaitingnp = main_priority_NON(rowCount, arrivalper, burstper, periority)
                self.printper(twaitingnp)


def main():
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

