class Persona:

    def __init__(self, nombre, edad, email):#Constructor
        self.nombre = nombre
        self.edad = edad
        self.email = email

    def __str__(self):#Metodo
       print("mi nombre es:", self.nombre, "y tengo", self.edad,"años")

Persona01 = Persona("pedro",12,"correo1")
Persona02 = Persona("pedro01",12,"correo2")
Persona03 = Persona("pedro01",132,"correo3")

print(Persona01.nombre)
print(Persona02.nombre)
print(Persona03.nombre)


