import xml.etree.ElementTree as ET

data_tree = ET.parse('sample.xml')
data_root = data_tree.getroot()

for outer in data_root:
    print(outer.tag)

"""    
for val in data_root[0]:
    print(val.tag, end=' = ')
    print(val.text)
"""
