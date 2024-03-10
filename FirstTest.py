#first exercice is to extract the inputs and the outputs and the locals.
# if i instanciate an object from this class and i call 3 methodes on of them is for the inputs , the other for outputs and the other for locals 
import xml.etree.ElementTree as ET 
file =r'C:\Users\malek\OneDrive\Documents\Projet_Pfe\Les fichiers xscade\Parsing\COND_RECOVERING_POS_TO_END_RECOVERING (1).xscade'
root = ET.parse(file).getroot()

# first i want to extarct only the outputs 
namespace = {'ns': 'http://www.esterel-technologies.com/ns/scade/6'} 




inputs = root.findall('./ns:inputs/ns:Variable', namespace)
index= 1
for inp in inputs:
    name = inp.tag.split('}')[-1]
    type_ref = inp.find('./ns:type/ns:NamedType/ns:type/ns:TypeRef',namespace).attrib['name']
    print(f"{name} input numero {index}  :  {inp.attrib['name']} et leur type de donnée est :  {type_ref}")
    index+=1  
    pragmas = inp.findall('./ns:pragmas/*', namespace)
    for prg in pragmas:
        print(prg.attrib['oid'])

   




# outputs = root.findall('./ns:outputs/ns:Variable' , namespace)
# index1=1
# for output in outputs:
#     name_output=output.tag.split('}')[-1]
#     type_ref = output.find('./ns:type/ns:NamedType/ns:type/ns:TypeRef' , namespace).attrib['name']
#     print(f"{name_output} de la sortie numero {index1}  : {output.attrib['name']} et leur type de donnée est : {type_ref}")
#     pragmas_output=output.findall('./ns:pragmas/*' , namespace)
#     for prgms in pragmas_output:
#         print(f"et son pragams est{prgms.attrib['oid']}")
#     index1+=1 







# #C'est la recherche d abord du variables locals
# locals_variables = root.findall('./ns:locals/ns:Variable', namespace) #localiser les variables locale
# N=1
# for lcl in locals_variables: #parcourir les variables locales
#     local = lcl.tag.split('}')[-1]  #eliminer les le namespace en faisant eliminer le lien qui se termine par } et renvoyant l index final de la liste puisque findall renvoye une liste des ittems 
#     Data_type = lcl.find('./ns:type/ns:NamedType/ns:type/ns:TypeRef' , namespace).attrib['name'] #se referant avec le xpath du type de donner 
#     print(f"{local} local numero {N} est  , {lcl.attrib['name']} est de type {Data_type}") 
#     N+=1    
#     pragmas_locals = lcl.findall('./ns:pragmas/*' , namespace) #localiser les pragmas 
#     for pr in pragmas_locals:
#         print(f"et son pragams est {pr.attrib['oid']}") #extraire les pragmas 




# data_system = root.findall('./ns:data/ns:Equation' , namespace) 
# Number = 1 
# for element in data_system: 
#     left_equations = element.findall('./ns:lefts/ns:VariableRef' , namespace)
#     for lft in left_equations:
#         print(f"les variables lefts de l equation sont {lft.tag.replace('{http://www.esterel-technologies.com/ns/scade/6}' , '')[:]} {Number} , {lft.attrib['name']}")
#         Number+=1    
#     right_equations = element.findall('./ns:rights/')




