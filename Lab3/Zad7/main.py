import json
from dataclasses import dataclass

@dataclass
class Person:
    
    name : str
    surname : str
    age : int
    addres : str
    pesel : str
    zipCode : str

    def write(self, jsonSave):
        self.name = jsonSave["name"]
        self.surname = jsonSave["surname"]
        self.age = jsonSave["age"]
        self.addres= jsonSave["addres"]
        self.pesel = jsonSave["pesel"]
        self.zipCode = jsonSave["zipCode"]

    def save(self):
        toSave = {
            "name" : self.name,
            "surname" : self.surname,
            "age" : self.age,
            "addres" : self.addres,
            "pesel" : self.pesel,
            "zipCode" : self.zipCode
        }
        jsonObject = json.dumps(toSave, indent = 6)
        with open("Zad7/test.json", "w") as out:
            out.write(jsonObject)


Zbychu = Person("Hubert", "Marciniak", 45, "Ul. Kwiatowa", "61030595278", "31-104" )
Marcin = Person(None,None,None,None,None,None)

Zbychu.save()
with open('Zad7/file.json', 'r') as j:
    data = json.load(j)
Marcin.write(data)

print(Marcin.name)
print(Marcin.addres)