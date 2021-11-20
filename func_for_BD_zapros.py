# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pymysql, openpyxl

global con
con = pymysql.connect(host='localhost',
        user='root',
        password='h8!vv933M',
        db='test') #имя БД


def Create_SQL_Table ():
    '''
    Функция создает таблицу с нуля 
    '''
    with con:
        cur = con.cursor()
        sql = "CREATE TABLE cadet_print(id int AUTO_INCREMENT, name VARCHAR(30), PRIMARY KEY(id))"
        cur.execute(sql)
        con.commit()  
        print('table created')
        
def Delete_SQL_Table ():
    '''
    Функция удаляет всю таблицу полностью 
    '''
    with con:
        cur = con.cursor()
        sql = "DROP TABLE cadet_print"
        cur.execute(sql)
        con.commit()  
        print('table deleted')

def Insert_SQL_Table (x):
    '''
    Функция добаляет в таблицу имя Х
    '''
    #with con:
    cur = con.cursor()
    sql = f"INSERT INTO cadet_print(name) VALUES ('{x}')"
    cur.execute(sql)
    con.commit()

def Zapolnenye_SQL_Table ():
    '''
    Функция заполняет таблицу из exel
    '''
    excel_file = openpyxl.load_workbook('name_list.xlsx') #открывает файл
    excel_list = excel_file['Sheet1']                   #выбирает лист файла
    for i in range(excel_list.max_row):  #заполнение списка
        cell_obj = excel_list.cell(row=i+1, column=1)                 
        x = cell_obj.value
        Insert_SQL_Table(x)
    print('table inserted')
        
        
def Delete_Odnogo_SQL_Table (aidi):
    '''
    Функция удаляет челоека по id
    '''
    with con:
        cur = con.cursor()
        sql = f"DELETE FROM cadet WHERE id='{aidi}'"
        cur.execute(sql)
        con.commit()
        print('delited - ',aidi)
    
    

def Seach_Cadet (seach):
    '''
    Функция выполняет поиск по полю id для чисел и по name для букв
    '''
    print(type(seach))
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM cadet WHERE id=%s", seach)
        rows = cur.fetchall()
        for row in rows:
            print("{0} {1}".format(row[0], row[1]))
    
    
def Sort_Cadet ():
    '''
    Функция выполняет сортировку в запросе по имени
    '''
    cur = con.cursor()
    sql = "SELECT id, name FROM cadet_print ORDER BY name"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print("{0} {1}".format(row[0], row[1]))









# print ('Создать таблтцу - 1\nУдалить таблицу - 2\nЗаполнить таблицу - 3\nУдалить человека - 4')
# vvod = input("Выберите один вариант: ")
# if vvod == '1':
#     Create_SQL_Table()
# elif vvod == '2':
#     Delete_SQL_Table()
# elif vvod == '3':
#     Zapolnenye_SQL_Table()
# elif vvod == '4':
#     aidi = input("Выберите id человека, которого надо удалить: ")
#     Delete_Odnogo_SQL_Table(aidi)
    
