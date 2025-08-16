#!/usr/bin/python3

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = value

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: child.text for child in root}



def main():
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)

if __name__ == "__main__":
    main()