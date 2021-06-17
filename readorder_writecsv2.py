import xml.etree.ElementTree as ET

filename = 'text_files/sampleOrder.xml'

parsed_file = ET.parse(filename)
for line in parsed_file:
    print(line)