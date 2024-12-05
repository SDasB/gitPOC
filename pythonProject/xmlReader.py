import xml.etree.ElementTree as ET

def read_xml(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Iterate over person elements
    for person_elem in root.findall('person'):
        # Extract information from each person
        name = person_elem.find('name').text
        age = int(person_elem.find('age').text)
        city = person_elem.find('city').text

        # Print information
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"City: {city}")
        print()

if __name__ == "__main__":
    xml_file_path = "data.xml"
    read_xml(xml_file_path)