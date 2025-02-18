print("hola mundo")

nombre = "luis"
edad = 20
print("mi nombre es:", nombre)

#condicionales

if edad >= 2: # == >= <= != < > operadores de condicion
    print("mi nombre es luis")  
else:
        print("mi nombre no es luis")   

if edad >= 2 and edad <= 20:
    print("mi nombre es luis")


for i in range(5):
    print(i) 

# Array
    fruta = ["manzana", "pera", "uva", "sandia", "melon"]   

print(fruta[0])

for i in fruta:
    print(i)    

    fruta[0] = "platano"
    fruta.append("naranja")
    fruta.pop(1)


    
def algoritmo():
               #ejercicio
    arreglo_numero = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100]
    arreglo_final = []
    for i in arreglo_numero:
        if i > 20 and i < 80:
            arreglo_final.append(i)

            print("numeros del 20 al 30", arreglo_final)
            print("Suma de los numeros", sum(arreglo_final))



            #arreglos bidemencionales   
            matriz = [[1,3],[4,6],[7,9]]  

            for i in matriz:
                algoritmo(i[0])