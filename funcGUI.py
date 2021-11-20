from PyQt5 import QtWidgets, uic
from variables import CADET_DATA2, period_uval
from myfunc import Rabota_nad_vsem_Failom, Print_File_Final
import sys


def Print_Window():
    app = QtWidgets.QApplication([])
    dlg = uic.loadUi("dialog.ui")

    # -----------------------------
    def Add_cadet_in_ListTable():  # Выводит в окно список (выполняет сортировку по имени)
        dlg.listWidget.addItems(CADET_DATA2)
        # listWidget.selectedItems() - то, что выделили \ takeItem(row) - удаление


    def Print_send_list():  # Отправляет на печать
        global period_uval
        if not dlg.lineEdit_start.text() == "" and not dlg.lineEdit_end.text() == "":
            period_uval.clear()
            period_uval.append(dlg.lineEdit_start.text())  # переменная с датой начала увольнения
            period_uval.append(dlg.lineEdit_end.text())  # переменная с датой конца увольнения

            Rabota_nad_vsem_Failom(len(CADET_DATA2))  # начинаем работать с данными (после запуска интерфеса)
            Print_File_Final(len(CADET_DATA2))  # отправка файла на печать
            msb = QtWidgets.QMessageBox()
            msb.setWindowTitle("Оповещение")
            msb.setText("Файл отправлен на печать")
            msb.setIcon(QtWidgets.QMessageBox.Information)
            msb.exec_()
            sys.exit(0)
        else:
            msb = QtWidgets.QMessageBox()
            msb.setWindowTitle("Ошибка")
            msb.setText("Введите даты !!!")
            msb.setIcon(QtWidgets.QMessageBox.Warning)
            msb.exec_()

    dlg.ButtonAdd.clicked.connect(Add_cadet_in_ListTable)
    dlg.ButtonPrint.clicked.connect(Print_send_list)
    # -----------------------------
    dlg.show()
    app.exec()

# Form, Window = uic.loadUiType("dialog.ui")
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
