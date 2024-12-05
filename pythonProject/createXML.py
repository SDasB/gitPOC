import xml.etree.ElementTree as ET

def create_xml(file_path):
    # Create the root element
    root = ET.Element("root")

    # Create person elements
    person1 = ET.SubElement(root, "person")
    name1 = ET.SubElement(person1, "name")
    name1.text = "John Doe"
    age1 = ET.SubElement(person1, "age")
    age1.text = "30"
    city1 = ET.SubElement(person1, "city")
    city1.text = "New York"

    person2 = ET.SubElement(root, "person")
    name2 = ET.SubElement(person2, "name")
    name2.text = "Jane Doe"
    age2 = ET.SubElement(person2, "age")
    age2.text = "25"
    city2 = ET.SubElement(person2, "city")
    city2.text = "San Francisco"

    # Create an ElementTree object
    tree = ET.ElementTree(root)

    # Write to the XML file
    tree.write(file_path)

if __name__ == "__main__":
    xml_file_path = "created_data.xml"
    create_xml(xml_file_path)