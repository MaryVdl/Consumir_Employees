'''
Created on 5 jul. 2022

@author: marisol.vidal
'''        
from pip._vendor.urllib3.util import response, url
import requests

def readFile(file):
    try:
        with open(file, "r+", encoding='utf-8') as f:
            return f.readlines();
    except FileNotFoundError:
        print("Archivo no encontrado")
        
def crearLista():
    lista = []
    name_archivo = "Clientes.txt"
    res = readFile(name_archivo)
    for line in res:
        if line != "":
            lista.append(line.rstrip("\n"))
    print(lista)
    return lista

def datas(lista):
    try:
        for i in lista:
            if (i != ""):
                pos = i.split(",")
                #Employee(0 firstname, 1 surname), Country(2 nameCountry), Language(3 namelanguage), Airport(4 nameairport),
                firstname = pos[0]
                surname =  pos [1]
                name_country = pos[2]
                name_language = pos[3]
                name_airport = pos[4]
                
                data_airport = add_airport(name_airport)
                id_airport = data_airport["id"]  
                
                nameLan = name_language[:5]
                data_language =  add_language("LAN" + nameLan, name_language) 
                id_language = data_language["id"]         
                
                nameCoun = name_country[:5]
                data_country = add_country("COU" + nameCoun, name_country, id_airport)
                id_country = data_country["id"]
                
                create_employee(surname, firstname, id_country, id_language)                
    except:
        print("ERROR en datas")

def add_country(code, name, id_airport):
    try:
        url = "http://localhost:8080/country/countryadd"
        requests.post(url)
        todo = {"code": code, "name": name, "id_airport": id_airport}
        response = requests.post(url, json=todo)
        res = response.json()
        print("add_country\n" + str(res))
        return res
    except:
        print("Error en add_Country")

def add_airport(name):
    try:
        url = "http://localhost:8080/airports/airportadd"
        requests.post(url)
        todo = {"name": name}
        response = requests.post(url, json=todo)
        res = response.json()
        print("add_airport\n" + str(res))
        return res
    except:
        print("ERROR en add_airport")
    
def add_language(code, name):
    try:
        url = "http://localhost:8080/languages/languagesadd"
        requests.post(url)
        todo = {"code": code, "name": name}
        response = requests.post(url, json=todo)
        res = response.json()
        print("add_language\n" + str(res))
        return res
    except:
        print("ERROR en add_language")
        
    

def create_employee(surname, firstname, name_country, name_language):
    try:
        url = "http://localhost:8080/apiv1/employees/add"
        requests.post(url)
        todo = {"surname" : surname, "firstname": firstname, "name_country": name_country, "name_language": name_language}
        response = requests.post(url, json=todo)
        res = response.json()
        print("Se agregaron los datos a la tabla employees\n" + str(res))
    except:
        print("Error, no se pudieron guardar los datos")
        
            
#crearLista()