# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 20:58:45 2021

@author: Andry
"""
"""
РЕАЛИЗОВАНО ЗАДЕЙСТВОВАНИЕ БД
"""
import openpyxl, shutil, sys
#from progress.bar import IncrementalBar
from myfunc import Rabota_nad_vsem_Failom, Print_File_Final, BD_Cadet_Data
from variables import file_spisok_kadet, period_uval,vudacha, CADET_DATA2


#______________________________________________________________________________
def XL_START ():
    shutil.copyfile("InfTeh/uvol_zap_initial.xlsx", "InfTeh/uvol_zap_final.xlsx")
    
    #запуск функции изъятия данных из БД
    BD_Cadet_Data()
    
    # запуск главной функции и функции печати
    Rabota_nad_vsem_Failom(len(CADET_DATA2))
    print('Подключение к принтеру...')
    Print_File_Final(len(CADET_DATA2))

    print('________ \nCOMPLITE')
    sys.exit(0)
#______________________________________________________________________________


XL_START ()








