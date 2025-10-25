import xml.etree.ElementTree as ET
import os  

def xml_verifier(file_name, element):
        try: 
            if not os.path.exists(file_name):
                root = ET.Element(element)
                tree = ET.ElementTree(root)
                tree.write(file_name, encoding='utf-8', xml_declaration=True)
                return root, tree
            else: 
                tree = ET.parse(file_name) 
                root = tree.getroot()
                return root, tree
        except ET.ParseError: 
            return None 

xml_verifier ("library.xml", "books")

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child (self, child_node):
        self.children.append(child_node)

root = Node

child1 = Node("Child 1 Value")
child2 = Node("Child 2 Value")
child3 = Node("Child 3 Value")

root.add_child(child1)
root.add_child(child2)
root.add_child(child3)

print(f"Root Value") 
