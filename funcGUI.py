from PyQt5 import QtWidgets, uic
from variables import CADET_DATA2, CADET_DATA1, period_uval
from myfunc import Rabota_nad_vsem_Failom, Print_File_Final, BD_Cadet_Data, Insert_SQL_Table,Insert_SQL_Table1,Delete_Odnogo_SQL_Table, Delete_Odnogo_SQL_Table1
import sys


def Print_Window():  # окно для печати
    app = QtWidgets.QApplication([])
    dlg = uic.loadUi("dialog.ui")

    # -----------------------------
    def Add_cadet_in_ListTable():  # Выводит в окно список (выполняет сортировку по имени)
        dlg.listWidget.addItems(CADET_DATA2)
        # listWidget.selectedItems() - то, что выделили \ takeItem(row) - удаление

    def Tranz_cadet():  # переместить из табл в табл
        indexcur = dlg.listWidget1.currentRow()
        item = dlg.listWidget1.item(indexcur)
        x = item.text()
        if x is not None:
            Insert_SQL_Table(x)
            BD_Cadet_Data()
            dlg.listWidget2.clear()
            dlg.listWidget2.addItems(CADET_DATA2)

    def Del_cadet():
        indexcur = dlg.listWidget2.currentRow()
        item = dlg.listWidget2.item(indexcur)
        x = item.text()
        if x is not None:
            Delete_Odnogo_SQL_Table(x)
            BD_Cadet_Data()
            dlg.listWidget2.clear()
            dlg.listWidget2.addItems(CADET_DATA2)

    def Delete_cadet():
        indexcur = dlg.listWidget1.currentRow()
        item = dlg.listWidget1.item(indexcur)
        x = item.text()
        if x is not None:
            Delete_Odnogo_SQL_Table1(x)
            BD_Cadet_Data()
            dlg.listWidget1.clear()
            dlg.listWidget2.clear()
            dlg.listWidget1.addItems(CADET_DATA1)
            dlg.listWidget2.addItems(CADET_DATA2)

    def Add_cadet():
        x = dlg.lineEdit_addcadet.text()
        if x is not None:
            Insert_SQL_Table1(x)
            BD_Cadet_Data()
            dlg.listWidget1.clear()
            dlg.listWidget2.clear()
            dlg.listWidget1.addItems(CADET_DATA1)
            dlg.listWidget2.addItems(CADET_DATA2)


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

    dlg.ButtonPrint.clicked.connect(Print_send_list)
    dlg.add_cadetprint_button.clicked.connect(Tranz_cadet)
    dlg.del_cadetprint_button.clicked.connect(Del_cadet)
    dlg.del_cadet_button.clicked.connect(Delete_cadet)
    dlg.add_cadet_button.clicked.connect(Add_cadet)

    dlg.listWidget1.addItems(CADET_DATA1)
    dlg.listWidget2.addItems(CADET_DATA2)
    # -----------------------------
    dlg.show()
    app.exec()

