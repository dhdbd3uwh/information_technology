from PyQt5 import QtWidgets, uic, QtCore
from variables import CADET_DATA2, CADET_DATA1, period_uval, schet_name
from myfunc import Start_Filling_Process, BD_Cadet_Data, Insert_SQL_Table,Insert_SQL_Table1,Delete_Odnogo_SQL_Table, Delete_Odnogo_SQL_Table1, Clean_Table




def Print_Window():  # окно для печати
    app = QtWidgets.QApplication([])
    dlg = uic.loadUi("dialog.ui")


    # ----------------------------------
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
        print(len(x))
        if x is not None and not dlg.lineEdit_addcadet.text() == "" and x[0].isalpha() == True:
            if x.istitle() == True: # каждое слово с заглавной
                Insert_SQL_Table1(x)
                BD_Cadet_Data()
                dlg.listWidget1.clear()
                dlg.listWidget2.clear()
                dlg.listWidget1.addItems(CADET_DATA1)
                dlg.listWidget2.addItems(CADET_DATA2)
            else:
                msb = QtWidgets.QMessageBox()
                msb.setWindowTitle("Ошибка")
                msb.setText("Имя и фамилия должны начинаться с заглавной буквы !!!")
                msb.setIcon(QtWidgets.QMessageBox.Warning)
                msb.exec_()

        else:
            msb = QtWidgets.QMessageBox()
            msb.setWindowTitle("Ошибка")
            msb.setText("Введите имя !!!")
            msb.setIcon(QtWidgets.QMessageBox.Warning)
            msb.exec_()


    #------------------------------------

    def Print_send_list():  # Отправляет на печать
        global period_uval
        if not dlg.lineEdit_start.text() == "" and not dlg.lineEdit_end.text() == "":
            period_uval.clear()
            period_uval.append(dlg.lineEdit_start.text())  # переменная с датой начала увольнения
            period_uval.append(dlg.lineEdit_end.text())  # переменная с датой конца увольнения

            Start_Filling_Process(len(CADET_DATA2))

            msb = QtWidgets.QMessageBox()
            msb.setWindowTitle("Оповещение")
            msb.setText("Файл отправлен на печать")
            msb.setIcon(QtWidgets.QMessageBox.Information)
            msb.exec_()
            #sys.exit(0) # после отправки на печать прога закрывается
        else:
            msb = QtWidgets.QMessageBox()
            msb.setWindowTitle("Ошибка")
            msb.setText("Введите даты !!!")
            msb.setIcon(QtWidgets.QMessageBox.Warning)
            msb.exec_()

    def Label_blabla():
        print('ds')

    def Print_send_list_start():
        Label_blabla()
        Print_send_list()


    def Tyds ():
        Clean_Table()
        BD_Cadet_Data()
        dlg.listWidget1.clear()
        dlg.listWidget2.clear()
        dlg.listWidget1.addItems(CADET_DATA1)
        dlg.listWidget2.addItems(CADET_DATA2)


#------------------------------------------------------------------------
    dlg.ButtonPrint.clicked.connect(Print_send_list_start)
    dlg.add_cadetprint_button.clicked.connect(Tranz_cadet)
    dlg.del_cadetprint_button.clicked.connect(Del_cadet)
    dlg.del_cadet_button.clicked.connect(Delete_cadet)
    dlg.add_cadet_button.clicked.connect(Add_cadet)
    dlg.clean_BD_button.clicked.connect(Tyds)

    dlg.listWidget1.addItems(CADET_DATA1)
    dlg.listWidget2.addItems(CADET_DATA2)
    # -----------------------------
    dlg.show()
    app.exec()

