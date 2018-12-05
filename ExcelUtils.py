# -*- coding: UTF-8 -*-

import xlrd

def getColNum(sheet,colName):
    row = sheet.row(1)
    placehoderNum = -1
    for cell in row:
        placehoderNum = placehoderNum + 1
        if colName.decode("utf-8") == cell.value:
            break

    return placehoderNum

def getSheet(excelName):
    excel = xlrd.open_workbook(excelName)
    sheet = excel.sheet_by_index(0)
    return sheet