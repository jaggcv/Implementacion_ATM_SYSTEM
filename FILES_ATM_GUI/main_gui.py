import PySide2.QtGui
from GUI_mainwindow import Ui_MainWindow
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from time import sleep

from Receive_Command import Recieve_command
from Check_Password import Check_password
from Withdraw import Withdraw
from Show_Balance import Show_balance

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Process receive command
        self.sel = None
        self.ui.pb_withdraw.clicked.connect(self.withdraw)
        self.ui.pb_showbalance.clicked.connect(self.show_balance)
        

        #Process check password
        self.card_id = 0
        self.passw = 0
        self.account1:dict = {}
        self.account2:dict = {}
        
        self.ui.pb_OK_setAccount.clicked.connect(self.check_password)


        #Process withdraw
        self.amount = 0
        self.ui.pushButton.clicked.connect(self.withdraw_operation)


        #timer
        self.timeofwait = 4000
        self.temporizador = QTimer()
        self.temporizador.timeout.connect(self.timer_function)
        self.temporizador.setSingleShot(True)  # Establece el temporizador para ejecutarse solo una vez
        


    def withdraw(self):
        self.sel = Recieve_command(2) # Process 1
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_setAccount)
        print(self.sel)
        pass
    
    def show_balance(self):
        self.sel = Recieve_command(1) # Process 1
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_setAccount)
        print(self.sel)
        pass
 
    
    def check_password(self):
        self.card_id = int(self.ui.lineEdit_cardid.text())
        self.passw = int(self.ui.lineEdit_password.text())
        
        result = Check_password(self.card_id, self.sel, self.passw) #process 2
        print(result)

        if(result[0]!=None and result[1]==None and result[2]==None):
            self.account1 = result[0]
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_withdraw)
        elif(result[0]==None and result[1]!=None and result[2]==None):
            self.account2 = result[1]
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_showBalance)
            self.show_balance_operation()
        else:
            self.ui.lb_setaccount.setText(result[2])

    def withdraw_operation(self):
        self.amount = int(self.ui.lineEdit_amount_pgwithdraw.text())
        result = Withdraw(self.amount, self.account1) # Process 3
        if(result[0]!= None and result[1]==None):
            self.ui.lineEdit_inf_pgwithdraw.setText("Succesfull, get the amount")
            self.temporizador.start(self.timeofwait)

        elif(result[0]== None and result[1]!=None):
            self.ui.lineEdit_inf_pgwithdraw.setText(result[1])
            self.ui.lineEdit_amount_pgwithdraw.setText('')
            self.temporizador.start(self.timeofwait)

    def show_balance_operation(self):
        result = Show_balance(self.account2)
        self.ui.lb_show_balance.setText("The balance of account:"+str(result[0]))
        self.ui.lineEdit_balance_pgshowbalance.setText(str(result[1]))
        self.temporizador.start(self.timeofwait)
          
    def timer_function(self):
        self.ui.lineEdit_cardid.setText('')
        self.ui.lineEdit_password.setText('')
        self.ui.lineEdit_inf_pgwithdraw.setText('')
        self.ui.lineEdit_amount_pgwithdraw.setText('')

        self.ui.lb_show_balance.setText('Balance')
        self.ui.lineEdit_balance_pgshowbalance.setText('')

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_selectOperation)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()