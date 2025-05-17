LIMITE: int = 1000

suma: int = 0 
# numero: int = 1

#while numero < LIMITE:
#    if numero % 3 == 0 or numero % 5 == 0: 
#       suma += numero
#    numero += 1 

for numero in range(1, LIMITE): # [a..b)
    if numero % 3 == 0 or numero % 5 == 0: 
        suma += numero

print(suma) 