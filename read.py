import os
import xml.etree.ElementTree as ET

tree = ET.parse('diagramme-test.xml')
root = tree.getroot()

class Nom_Prenom:
    Nom_Prenom = 0
    ID = 0
    Target = []
    
liste_class = []


for child in root[0]:                   #positionement dans le fichié xml a la 3eme balise

        if 'name' in child.attrib : 
            print(child.attrib.get('name'), " | ", child.attrib.get("id"))      #lecture d'une valeur specifique
            
            if child.attrib.get('name') == 'Nom Prenom':
                NP = Nom_Prenom()
                NP.Nom_Prenom = child.attrib.get('name')
                NP.ID = child.attrib.get('id')
                liste_class.append(NP)
        
        
            
        if 'sourceRef' in child.attrib:
            print("Source fleche : ", child.attrib.get('sourceRef'), "| Target Fleche: ", child.attrib.get('targetRef'))
            
            for i in range(len(liste_class)):
                if liste_class[i].ID == child.attrib.get('sourceRef'):
                    liste_class[i].Target.append(child.attrib.get('targetRef'))
            
            
        print(child.tag, child.attrib)        #lecture de toute la ligne
        
print(liste_class)

        
        
        
        