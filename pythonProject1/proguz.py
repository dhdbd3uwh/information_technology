# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 20:58:45 2021

@author: Andry
"""
"""
РЕАЛИЗОВАНО ЗАДЕЙСТВОВАНИЕ БД
ТРИГГЕР НА УДАЛЕНИЕ ДАННЫХ ИЗ ТАБЛИЦЫ
(если удалется в одной, то удаляется и в другой)
"""
import shutil
from myfunc import BD_Cadet_Data
from funcGUI import Print_Window


#______________________________________________________________________________
def XL_START():  # старт окна печати
    #shutil.os.remove("InfTeh/uvol_zap_final.xlsx")
    shutil.copyfile("InfTeh/uvol_zap_initial.xlsx", "InfTeh/uvol_zap_final.xlsx")
    # запуск функции изъятия данных из БД
    BD_Cadet_Data()
    # запуск интерфейса
    Print_Window()




#______________________________________________________________________________

XL_START()



