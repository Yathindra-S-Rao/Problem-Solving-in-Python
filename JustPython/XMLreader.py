import xml.etree.ElementTree as ET

xml_string = '''<company>
    <employee id="001">
        <name>John</name>
        <role>Developer</role>
    </employee>
    <employee id="002">
        <name>Alice</name>
        <role>Tester</role>
    </employee>
</company>'''

data = ET.fromstring(xml_string)

for ele in data:
    print(ele.get("id"))
    print(ele.find("name").text)
