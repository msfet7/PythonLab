import json

class Person:
    def __init__(self, name, surname, age, addres, pesel, zipCode):
        self.name = name
        self.surname = surname
        self.age = age
        self.addres = addres
        self.pesel = pesel
        self.zipCode = zipCode
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
        with open("Zad2/test.json", "w") as out:
            out.write(jsonObject)


Zbychu = Person("Zbychu", "Marciniak", 45, "Ul. Kwiatowa", "61030595278", "31-104" )
Marcin = Person(None,None,None,None,None,None)
Zbychu.save()
with open('Zad2/file.json', 'r') as j:
    data = json.load(j)
Marcin.write(data)
print(Marcin.age)
print(Marcin.addres)