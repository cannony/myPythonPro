# -*- coding: UTF-8 -*-

from lxml import etree

tree = etree.parse("sharedocs/Opt_Record.xml")

root = tree.getroot()
nsmap = root.nsmap
NS_PREFIX = "default"
nsmap[NS_PREFIX] = nsmap[None]
nsmap.pop(None)

cdaXpath = '{0}/@{1}'

path1 = "//{0}:{1}".format(NS_PREFIX, "*[@*='[MaritalStatusCodeName]']")
# path1 = "//text()"
print path1
aa = tree.xpath(path1, namespaces=nsmap)
print(len(aa)) #数组长度
attname = ''
for name, value in sorted(aa[0].items()):
    if value == '[MaritalStatusCodeName]':
        attname = name

cdaXpath = cdaXpath.format(tree.getpath(aa[0]),attname)
print cdaXpath
# print '标签',aa[0].tag #标签名
# print tree.getpath(aa[0]) #获取xpath路径
# bb = tree.xpath("//0".format(aa[0].tag), namespaces=nsmap)
# print( bb )