# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 16:30:11 2021

@author: Andry
"""
import pymysql

file_initial = 'InfTeh/uvol_zap_initial.xlsx' #имя файла
file_final = 'InfTeh/uvol_zap_final.xlsx'
file_spisok_kadet = 'InfTeh/name_list.xlsx'
list_number = ['1','2','3','4','5','6','7','8','9','10']
CADET_DATA2 = []
schet_name = 0

period_uval = "T"
vudacha = "T"


con = pymysql.connect(host='localhost',
        user='root',
        password='h8!vv933M',
        db='test') #имя БД