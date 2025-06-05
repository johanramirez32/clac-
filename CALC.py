def add(n , m): 
    return n+m 


def sub(n, m):  
    return n-m 


def mul(n, m): 
    return n * m


def mod(n, m): 
    return n % m  


def add(n , m): 
    return n+m 


def sub(n, m):  
    return n-m 


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
    return operacion.lower()


def tomar_numeros(numeros_operacion, resultado): 
    lista_numeros = numeros_operacion.split(",")
    n = lista_numeros[0] 
    m = lista_numeros[-1] 
    return n,m

def ejecutar_numeros(nombre_operacion,n,m,resultado):

    if n.lower().strip() == 'r':
                n= resultado
    n,m=float(n),float(m)
    if nombre_operacion == "add":
                resultado = add(n, m)
    elif nombre_operacion == "sub":
                resultado = sub(n, m)
    elif nombre_operacion == 'mul':
                resultado = mul(n, m)
    elif nombre_operacion == 'div':
                resultado = div(n, m)
    elif nombre_operacion == 'mod':
                resultado = mod(n, m)
    else:
            resultado = 0

    return resultado 


def calculadora():
    resultado = 0
    while True:
        operacion: str = leer_operacion()

        if operacion == 'exit':
            print('Goodbye')
            break


        nombre_operacion: str = operacion[0:3] 
        n , m = tomar_numeros(operacion[4:-1],resultado)
        resultado = ejecutar_numeros(nombre_operacion, n, m,resultado)

        print(resultado)
calculadora()
