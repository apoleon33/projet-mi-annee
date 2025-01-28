import os
import xml.etree.ElementTree as ET



class Cells:
    Type = 0
    Content = 0
    ID = 0
    def __init__(self):
        self.Target = []  # list member variable, unique to each instantiated class




def readXML(data):
    tree = ET.parse(data)
    root = tree.getroot()
    liste_class = []


    for child in root[0]:                   #positionement dans le fichié xml a la bonne balise

        if 'name' in child.attrib : 
            #print(child.attrib.get('name'), " | ", child.attrib.get("id"))      #lecture d'une valeur specifique

            Cell = Cells()       #creation des cellules

            cell_title = read_title(child.attrib.get('name'))            #call func read_title to split the variables
            Cell.Type = cell_title[0]
            Cell.Content = cell_title[1]

            Cell.ID = child.attrib.get('id')                              #ajout ID
            liste_class.append(Cell)
        
        
            
        if 'sourceRef' in child.attrib:
            #print("Source fleche : ", child.attrib.get('sourceRef'), "| Target Fleche: ", child.attrib.get('targetRef'))
            
            for i in range(len(liste_class)):                              #boucle de comparaison pour trié les fleche
                if liste_class[i].ID == child.attrib.get('sourceRef'):
                    liste_class[i].Target.append(child.attrib.get('targetRef'))

            
            
        #print(child.tag, child.attrib)        #lecture de toute la ligne
    return(liste_class)


def read_title(data):          #read Cells datas
    data = data.split(":")     #split the data
    type = data[0].strip()     #.split() delete the space at the start/end if the str
    content = data[1].strip()

    return([type,content])

data = readXML('test-format-2.xml')