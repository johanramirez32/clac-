def add(n , m): 
    return n + m 


def sub(n, m):
    return n - m 


def mul(n, m):
    return n * m


def mod(n, m):
    return n % m  


def div(n, m):
    if m == 0:
        division = 0 
    else:
        division = n / m 
    return division 


def leer_operacion():
    print("calc ", end="")
    operacion: str = input()
    return operacion 



def tomar_numeros(numeros_operacion):
    lista_numeros = numeros_operacion.split(",")
    n = float(lista_numeros[0])
    m = float(lista_numeros[-1])
    return (n, m)


operacion: str = leer_operacion()
nombre_operacion: str = operacion[0:3]
n: float m: float = tomar_numeros(operacion[4:-1])

if nombre_operacion == "add":
    resultado: float  = add(n, m)
elif nombre_operacion == "dub":
    resultado: float = sub(n, m)
elif nombre_operacion == "mul":
    resultado: float = mul(n, m)
elif nombre_operacion == "div":
    resultado: float = div(n, m)
elif nombre_operacion == "mod":
    resultado: float = mod(n, m)
else:
    resultado = "chao pezcao"

print(resultado)
