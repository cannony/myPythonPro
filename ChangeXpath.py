# -*- coding: UTF-8 -*-

import CdaXpathUtils as cxu
import ExcelUtils as eu
import xlrd

sheet = eu.getSheet('excel/Opt_Record.xls')

colnum = eu.getColNum(sheet,'占位符')

count = 0
for placeholder in sheet.col_values(colnum):
    count = count+1
    # 第三行开始读
    if count <3:
        continue
    # print placeholder
    cdaXpath = cxu.getCdaXpath("sharedocs/Opt_Record.xml", placeholder)
    print cdaXpath

