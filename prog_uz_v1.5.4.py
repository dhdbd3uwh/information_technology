# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 20:58:45 2021

@author: Andry
"""
"""
РЕАЛИЗОВАНО ЗАДЕЙСТВОВАНИЕ БД
"""
import shutil, sys
from myfunc import BD_Cadet_Data
from funcGUI import Print_Window


#______________________________________________________________________________
def XL_START ():
    shutil.copyfile("InfTeh/uvol_zap_initial.xlsx", "InfTeh/uvol_zap_final.xlsx")
    # запуск функции изъятия данных из БД
    BD_Cadet_Data()
    # запуск интерфейса
    Print_Window()
    sys.exit(0)

#______________________________________________________________________________


XL_START()








