# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(755, 750)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lb_atmImage = QLabel(self.centralwidget)
        self.lb_atmImage.setObjectName(u"lb_atmImage")
        self.lb_atmImage.setGeometry(QRect(0, 0, 761, 701))
        self.lb_atmImage.setPixmap(QPixmap(u"FIGURES/atm_front.jpg"))
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(160, 130, 431, 321))
        self.page_selectOperation = QWidget()
        self.page_selectOperation.setObjectName(u"page_selectOperation")
        self.verticalLayoutWidget = QWidget(self.page_selectOperation)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 431, 321))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_selectOperation = QLabel(self.verticalLayoutWidget)
        self.lb_selectOperation.setObjectName(u"lb_selectOperation")
        self.lb_selectOperation.setMaximumSize(QSize(16777215, 50))
        self.lb_selectOperation.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 24px;\n"
"padding: 10px; ")
        self.lb_selectOperation.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_selectOperation)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_withdraw = QPushButton(self.verticalLayoutWidget)
        self.pb_withdraw.setObjectName(u"pb_withdraw")
        self.pb_withdraw.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.pb_withdraw)

        self.pb_showbalance = QPushButton(self.verticalLayoutWidget)
        self.pb_showbalance.setObjectName(u"pb_showbalance")
        self.pb_showbalance.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.pb_showbalance)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.page_selectOperation)
        self.page_setAccount = QWidget()
        self.page_setAccount.setObjectName(u"page_setAccount")
        self.verticalLayoutWidget_2 = QWidget(self.page_setAccount)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 443, 321))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lb_setaccount = QLabel(self.verticalLayoutWidget_2)
        self.lb_setaccount.setObjectName(u"lb_setaccount")
        self.lb_setaccount.setMaximumSize(QSize(16777215, 50))
        self.lb_setaccount.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"padding: 10px; ")
        self.lb_setaccount.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_setaccount)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_cardid = QLabel(self.verticalLayoutWidget_2)
        self.lb_cardid.setObjectName(u"lb_cardid")
        self.lb_cardid.setMaximumSize(QSize(100, 16777215))
        self.lb_cardid.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"padding: 10px; ")

        self.horizontalLayout_3.addWidget(self.lb_cardid)

        self.lineEdit_cardid = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_cardid.setObjectName(u"lineEdit_cardid")
        self.lineEdit_cardid.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_cardid)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_pass = QLabel(self.verticalLayoutWidget_2)
        self.lb_pass.setObjectName(u"lb_pass")
        self.lb_pass.setMaximumSize(QSize(100, 16777215))
        self.lb_pass.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"padding: 10px; ")

        self.horizontalLayout_4.addWidget(self.lb_pass)

        self.lineEdit_password = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_4.addWidget(self.lineEdit_password)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pb_OK_setAccount = QPushButton(self.verticalLayoutWidget_2)
        self.pb_OK_setAccount.setObjectName(u"pb_OK_setAccount")
        self.pb_OK_setAccount.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.pb_OK_setAccount)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.stackedWidget.addWidget(self.page_setAccount)
        self.page_withdraw = QWidget()
        self.page_withdraw.setObjectName(u"page_withdraw")
        self.verticalLayoutWidget_3 = QWidget(self.page_withdraw)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 434, 321))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_withdraw = QLabel(self.verticalLayoutWidget_3)
        self.label_withdraw.setObjectName(u"label_withdraw")
        self.label_withdraw.setMaximumSize(QSize(16777215, 50))
        self.label_withdraw.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"padding: 10px; ")
        self.label_withdraw.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_withdraw)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_inf_pgwithdraw = QLabel(self.verticalLayoutWidget_3)
        self.lb_inf_pgwithdraw.setObjectName(u"lb_inf_pgwithdraw")
        self.lb_inf_pgwithdraw.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"padding: 10px; ")
        self.lb_inf_pgwithdraw.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lb_inf_pgwithdraw)

        self.lineEdit_inf_pgwithdraw = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_inf_pgwithdraw.setObjectName(u"lineEdit_inf_pgwithdraw")
        self.lineEdit_inf_pgwithdraw.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_6.addWidget(self.lineEdit_inf_pgwithdraw)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_amount_pgwithdraw = QLabel(self.verticalLayoutWidget_3)
        self.lb_amount_pgwithdraw.setObjectName(u"lb_amount_pgwithdraw")
        self.lb_amount_pgwithdraw.setMaximumSize(QSize(100, 16777215))
        self.lb_amount_pgwithdraw.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"padding: 10px; ")
        self.lb_amount_pgwithdraw.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lb_amount_pgwithdraw)

        self.lineEdit_amount_pgwithdraw = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_amount_pgwithdraw.setObjectName(u"lineEdit_amount_pgwithdraw")
        self.lineEdit_amount_pgwithdraw.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_5.addWidget(self.lineEdit_amount_pgwithdraw)

        self.pushButton = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.stackedWidget.addWidget(self.page_withdraw)
        self.page_showBalance = QWidget()
        self.page_showBalance.setObjectName(u"page_showBalance")
        self.verticalLayoutWidget_4 = QWidget(self.page_showBalance)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 0, 431, 321))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lb_show_balance = QLabel(self.verticalLayoutWidget_4)
        self.lb_show_balance.setObjectName(u"lb_show_balance")
        self.lb_show_balance.setMaximumSize(QSize(16777215, 50))
        self.lb_show_balance.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 24px;\n"
"padding: 10px; ")
        self.lb_show_balance.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lb_show_balance)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_balance_pgshowbalance = QLabel(self.verticalLayoutWidget_4)
        self.lb_balance_pgshowbalance.setObjectName(u"lb_balance_pgshowbalance")
        self.lb_balance_pgshowbalance.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"padding: 10px; ")
        self.lb_balance_pgshowbalance.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lb_balance_pgshowbalance)

        self.lineEdit_balance_pgshowbalance = QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_balance_pgshowbalance.setObjectName(u"lineEdit_balance_pgshowbalance")
        self.lineEdit_balance_pgshowbalance.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_7.addWidget(self.lineEdit_balance_pgshowbalance)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.stackedWidget.addWidget(self.page_showBalance)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 755, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_atmImage.setText("")
        self.lb_selectOperation.setText(QCoreApplication.translate("MainWindow", u"Select one action", None))
        self.pb_withdraw.setText(QCoreApplication.translate("MainWindow", u"Withdraw", None))
        self.pb_showbalance.setText(QCoreApplication.translate("MainWindow", u"Show Balance", None))
        self.lb_setaccount.setText(QCoreApplication.translate("MainWindow", u"Set yout account card_id and password, and press OK to continue", None))
        self.lb_cardid.setText(QCoreApplication.translate("MainWindow", u"Card_id", None))
        self.lineEdit_cardid.setText("")
        self.lb_pass.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pb_OK_setAccount.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_withdraw.setText(QCoreApplication.translate("MainWindow", u"Withdraw: Introduce the amount to be withdrawed and press OK", None))
        self.lb_inf_pgwithdraw.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.lb_amount_pgwithdraw.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.lb_show_balance.setText(QCoreApplication.translate("MainWindow", u"Show balance", None))
        self.lb_balance_pgshowbalance.setText(QCoreApplication.translate("MainWindow", u"Your balance is:", None))
    # retranslateUi

