import xml.etree.ElementTree as ET 



file = r'C:\Users\malek\OneDrive\Documents\Projet_Pfe\Les fichiers xscade\Parsing\COND_RECOVERING_POS_TO_END_RECOVERING (1).xscade'

Tree = ET.parse(file) 
root = Tree.getroot()


# inputs = root.findall('.//{http://www.esterel-technologies.com/ns/scade/6}Variable') 
# # print(len(inputs))

# for element in inputs:
#     Variable_name = element.tag.replace('{http://www.esterel-technologies.com/ns/scade/6}' ,'') 
#     print(f"Donc mes {Variable_name} , sont {element.attrib['name']}") 
 
Type_reference = root.findall('.//{http://www.esterel-technologies.com/ns/scade/6}TypeRef') #xpath of 
for element in Type_reference:
    Variable_name = element.tag.replace('{http://www.esterel-technologies.com/ns/scade/6}' ,'') 
    print(f"Donc mes {Variable_name} , sont {element.attrib['name']}") 




# variables = inputs.findall('.//{http://www.esterel-technologies.com/ns/scade/6}Variable')

# print(len(variables))

# Variable_tag = inputs.tag.replace('{http://www.esterel-technologies.com/ns/scade/6}' , '')
# attribut= inputs.attrib['name']
    
# print(f"{Variable_tag} est {attribut}")
    
    
    
    
    

# Variables = inputs.findall('.//{http://www.esterel-technologies.com/ns/scade/6}Variable')

   