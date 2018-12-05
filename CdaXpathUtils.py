# -*- coding: UTF-8 -*-

from lxml import etree

def getCdaXpath(filepath,placehodler):
    tree = etree.parse(filepath)

    root = tree.getroot()
    nsmap = root.nsmap
    NS_PREFIX = "default"
    nsmap[NS_PREFIX] = nsmap[None]
    nsmap.pop(None)

    cdaXpath = '{0}/@{1}'

    path1 = "//{0}:{1}".format(NS_PREFIX, "*[@*='["+placehodler+"]']")
    # path1 = "//text()"
    # print path1
    aa = tree.xpath(path1, namespaces=nsmap)
    # print(len(aa))  # 数组长度
    attname = ''
    if len(aa)>0:
        for name, value in sorted(aa[0].items()):
            if value == '[MaritalStatusCodeName]':
                attname = name

        cdaXpath = cdaXpath.format(tree.getpath(aa[0]), attname)
    else :
        print "未找到占位符:  ",placehodler
        cdaXpath = ''
    return cdaXpath