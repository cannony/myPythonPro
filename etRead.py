# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET

tree = ET.parse('sharedocs/Opt_Record.xml')
root = tree.getroot()

# aa = root.findall("//[@extension='[PHRID]']")
aa = tree.findall(".")
print(aa)