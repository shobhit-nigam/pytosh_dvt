import xml.etree.ElementTree as ET

data_tree = ET.parse('sample.xml')
data_root = data_tree.getroot()

titles = []

fa = open("books.txt", "w")

for outer in data_root:
    for val in outer:
        if val.tag == 'title':
            titles.append(val.text)
            fa.write(val.text)
            fa.write("\n")
