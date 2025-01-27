import os
import xml.etree.ElementTree as ET

tree = ET.parse('diagramme-test.xml')
root = tree.getroot()

class Cells:
    Title = 0
    ID = 0
    def __init__(self):
        self.Target = []  # list member variable, unique to each instantiated class



liste_class = []


for child in root[0]:                   #positionement dans le fichié xml a la 3eme balise

        if 'name' in child.attrib : 
            print(child.attrib.get('name'), " | ", child.attrib.get("id"))      #lecture d'une valeur specifique

            Cell = Cells()
            Cell.Title = child.attrib.get('name')
            Cell.ID = child.attrib.get('id')
            liste_class.append(Cell)
        
        
            
        if 'sourceRef' in child.attrib:
            print("Source fleche : ", child.attrib.get('sourceRef'), "| Target Fleche: ", child.attrib.get('targetRef'))
            
            for i in range(len(liste_class)):
                if liste_class[i].ID == child.attrib.get('sourceRef'):
                    liste_class[i].Target.append(child.attrib.get('targetRef'))

            
            
        print(child.tag, child.attrib)        #lecture de toute la ligne