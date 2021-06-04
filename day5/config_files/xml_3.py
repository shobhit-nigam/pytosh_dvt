import xml.etree.ElementTree as ET

data_tree = ET.parse('sample.xml')
data_root = data_tree.getroot()

print(data_root[0].tag)
print(data_root[0].attrib)
