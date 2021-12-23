from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from funcGUI import Print_Window
import sys, os
import hashlib

def zapusk():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = uic.loadUi("dialogPass.ui")
    

    def check(login,paswrld): #проверка логина и пароля, также в функции реализованы входы в другие формы
        try:
            f = open('config.txt', 'r')
        except IOError:
            msg = QMessageBox()
            msg.setWindowTitle("Предупреждение")
            msg.setText("Создан файл данных")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            f = open('config.txt', 'w')
            f.close()
            f=open('config.txt', 'r')
        k=f.readlines()
        print("kop=",k)
        print("k=",len(k))
        if(len(k)>1):
            Ologin = k[0]
            Ologin = Ologin[:-1]
            Opassworld=k[1]
        else:
            Ologin=""
            Opassworld=""
        f.close()
        print("Ologin=", len(Ologin), "Opassworld=", len(Opassworld))
        print("log=", len(login), "pas=", len(paswrld))
        if(len(Ologin)<2 and len(Opassworld)<2):
            f = open('config.txt', 'w')
            Ologin=login
            Opassworld=paswrld
            print("сработало")
            print("log=",Ologin,"pas=",Opassworld)
            f.write(Ologin)
            f.write("\n")
            f.write(Opassworld)
            f.close()
            print("Новые данные запомнены!")
            print("Olog=", Ologin)
            print("Opassworld=", Opassworld)
            msg = QMessageBox()
            msg.setWindowTitle("Предупреждение")
            msg.setText("Новый логин и пароль запомнены")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            
        elif(login==Ologin and paswrld==Opassworld):
            
            MainWindow.close()
            

        else:
            print("Неверно введенные данные, попробуйте еще раз")
            msg = QMessageBox()
            msg.setWindowTitle("Предупреждение")
            msg.setText("Неверно введенные данные, попробуйте еще раз")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            sys.exit()

    def hash_dan(dan): #функция хэширования
        return hashlib.sha256(dan.encode()).hexdigest()
    def Vhodu(): # функция кнопки входа
        log1=MainWindow.lineEdit.text()
        pas1=MainWindow.lineEdit_2.text()
        login=hash_dan(log1)
        paswrld=hash_dan(pas1)
        check(login,paswrld)

    MainWindow.pushButton.clicked.connect(Vhodu)

    MainWindow.show()
    app.exec()
