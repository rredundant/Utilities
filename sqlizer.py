## sqlizer

import openpyxl

def sqlize(file_in, sheet_name):
    wb = openpyxl.load_workbook(file_in)
    sheet = wb[sheet_name]
    list1 = list(sheet.columns)[0]
    list2 = []
    for cellObj in list1:
        list2.append('\'' + cellObj.value + '\'')
    string1 = '(' + ', '.join(list2) + ')'
    print(string1)
