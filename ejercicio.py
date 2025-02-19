numero = 20
suma = 0
n = -1

for i in range(1, numero):
    if i % 2 == 0:
        suma +=i
        print("este es numero par",i * n)
        n = n * -1

print("la suma de los numeros pares es:", suma)