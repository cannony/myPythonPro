# -*- coding: UTF-8 -*-
fo = open("sharedocs/Opt_Record.xml", "r+")
str = fo.read()
print "读取的字符串是 : ", str
# 关闭打开的文件
fo.close()
