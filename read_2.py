import os
import shutil
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
            Cell.Content = cell_title[1]                                  # ajout du type et du contenue

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




def cell_fetch(id,list):               #algo de recherche de cellules avec une ID
    for i in range(len(list)):
        if id == list[i].ID :
            return list[i]             #renvoie la bonne cellule
    return 0


def traduction(data):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    group_freq = 0
    try:
        os.makedirs(dir_path+"/mydirectory")
    except FileExistsError:
        pass
    liste_titre= []
    shutil.copy('code.css', dir_path+"/mydirectory")
    shutil.copy('code.html', dir_path + "/mydirectory")
    shutil.copy('code.js', dir_path + "/mydirectory")
    for i in range(len(data)):
        if  data[i].Type == 'Titre' :
            liste_titre.append([])
            liste_titre[len(liste_titre)-1].append(data[i])
            for y in range(len(data[i].Target)):
                for x in range(len(data)):
                    if data[i].Target[y] == data[x].ID:
                        liste_titre[len(liste_titre)-1].append([data[x].Type,data[x].Content])

    print(liste_titre)
    edited_code = 'events = {'
    js_dict = {}
    date_properties: list[int | str] = [0, ""]  # [indice de la date, date]
    for element in liste_titre:
        # on trouve la date
        for attribut in element:
            if isinstance(attribut, Cells): continue
            if attribut[0] == 'date':
                date_properties[0] = element.index(attribut)
                date_properties[1] = attribut[1]
                js_dict[attribut[1]] = [{}]

        # on remplit la liste avec les informations restantes
        for index in range(len(element)):
            if index != 0 and index != date_properties[0]:
                date = date_properties[1]
                property_title = element[index][0]
                property_content = element[index][1]
                js_dict[date][0][property_title] = property_content


def freq_function(freq, edited_code, date, lieu, desc, group_freq):
    print(freq)
    freq = freq.split("-")  # split the data
    N = freq[0].strip()  # .split() delete the space at the start/end if the str
    j_s_m= freq[1].strip()

    date = date.split("-")  # split the data


    if j_s_m == 's':


        for i in range(int(N)):
            date[2] = int(date[2]) + 7
            if int(date[2]) > 31:
                date[1] = int(date[1]) + 1
                date[2] = int(date[2]) - 31
            if int(date[2]) < 10:
                date[2] = str("0") + str(date[2])
            if int(date[1]) <10:
                date[1] = str("0") + str(int(date[1]))


            edited_code = edited_code + "'" + str(date[0]) + "-" + str(date[1]) + "-"+ str(date[2]) + "'" + ":[{lieu:"
            edited_code = edited_code + "'" + lieu + "'" + ",activite:"
            edited_code = edited_code + "'" + desc + "'" + ",freq:"
            edited_code = edited_code + "'" + str(group_freq) + "'" + "}],"

    if j_s_m == 'm':

        for i in range(int(N)-1):
            date[1] = int(date[1]) + 1
            if int(date[1]) > 12:
                date[0] = int(date[0]) + 1
                date[1] = int(date[1]) - 11
            if int(date[1]) <10:
                date[1] = str("0") + str(int(date[1]))


            edited_code = edited_code + "'" + str(date[0]) + "-" + str(date[1]) + "-"+ str(date[2]) + "'" + ":[{lieu:"
            edited_code = edited_code + "'" + lieu + "'" + ",activite:"
            edited_code = edited_code + "'" + desc + "'" + ",freq:"
            edited_code = edited_code + "'" + str(group_freq) + "'" + "}],"




    return(edited_code)





data = readXML('test-format-3.xml')

traduction(data)

