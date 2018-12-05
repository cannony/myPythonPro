# -*- coding: UTF-8 -*-

from lxml import etree

tree = etree.parse("sharedocs/Opt_Record.xml")

# aa = tree.xpath('//typeId')
root = tree.getroot()
nsmap = root.nsmap
# ns = "{%s}" % nsmap
# item = root.find(ns+"typeId")

NS_PREFIX = "default"
nsmap[NS_PREFIX] = nsmap[None]
nsmap.pop(None)

aa = tree.xpath("//{0}:{1}".format(NS_PREFIX, "*[@displayName='[MaritalStatusCodeName]']"), namespaces=nsmap)
print aa[0].tag