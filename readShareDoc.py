# -*- coding: UTF-8 -*-

import  xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse('sharedocs/Opt_Record.xml')

#得到文档元素对象
root = dom.documentElement

bb = root.getElementsByTagName('title')
print bb[0].nodeValue