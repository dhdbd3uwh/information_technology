from PyQt5 import QtWidgets, uic
from variables import CADET_DATA2, period_uval, vudacha
from myfunc import Rabota_nad_vsem_Failom, Print_File_Final

# Form, Window = uic.loadUiType("dialog.ui")

def Print_Window():
    app = QtWidgets.QApplication([])
    dlg = uic.loadUi("dialog.ui")
    # -----------------------------
    def Add_cadet_in_ListTable():  # Выводит в окно список
        dlg.listWidget.addItems(CADET_DATA2)

    def Process_Status(n):
        if n == 1:
            dlg.label_status.setText("Обработка данных...")
        elif n == 2:
            dlg.label_status.setText("Подключение к принтеру...")
        elif n == 3:
            dlg.label_status.setText("Файл отправлен на печать")


    def Print_send_list():  # Отправляет на печать
        if not dlg.lineEdit_start.text() == "" and not dlg.lineEdit_end.text() == "":
            vudacha = dlg.lineEdit_start.text()  # переменная с датой начала увольнения
            period_uval = dlg.lineEdit_end.text()  # переменная с датой конца увольнения
            print(vudacha, '-', period_uval)
        else:
            msb = QtWidgets.QMessageBox()
            msb.setWindowTitle("Ошибка")
            msb.setText("Введите даты !!!")
            msb.setIcon(QtWidgets.QMessageBox.Warning)
            msb.exec_()

        Process_Status(1)
        Rabota_nad_vsem_Failom(len(CADET_DATA2))  # начинаем работать с данными (после запуска интерфеса)
        Process_Status(2)
        Print_File_Final(len(CADET_DATA2))  # отправка файла на печать
        Process_Status(3)

    dlg.ButtonAdd.clicked.connect(Add_cadet_in_ListTable)
    dlg.ButtonPrint.clicked.connect(Print_send_list)
    # -----------------------------
    dlg.show()
    app.exec()







# class Ui(QtWidgets.QDialog, Form):
#     def __init__(self):
#         super(Ui, self).__init__()
#         self.setupUi(self)
#         self.ButtonConsole.clicked.connect(self.printButtonPresed)
#         self.ButtonList.clicked.connect(self.ListAdd)
#
#     def printButtonPresed(self):
#         print("print")
#
#     def ListAdd (self):
#         self.listWidget.addItem('test')
#
#
# def main():
#     import sys
#     app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
#     window = Ui()
#     window.show()
#     sys.exit(app.exec())  # и запускаем приложение
#
#
# if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
#     main()  # то запускаем функцию main()
