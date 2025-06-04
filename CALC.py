def add(n, m): 
    return n + m 

def sub(n, m): 
    return n - m 

def mul(n, m): 
    return n * m

def mod(n, m): 
    return n % m  

def div(n, m): 
    if m == 0:
        return 0 
    return n / m 

def leer_operacion(): 
    print("calc ", end="")
    return input().strip().lower()

def tomar_numeros(numeros_operacion, resultado): 
    lista = numeros_operacion.split(",")
    n = lista[0].strip()
    m = lista[1].strip()

    if n == 'r':
        n = resultado
    else:
        n = float(n)

    if m == 'r':
        m = resultado
    else:
        m = float(m)

    return n, m

def ejecutar_operacion(nombre_operacion, n, m):
    if nombre_operacion == 'add':
        return add(n, m)
    elif nombre_operacion == 'sub':
        return sub(n, m)
    elif nombre_operacion == 'mul':
        return mul(n, m)
    elif nombre_operacion == 'div':
        return div(n, m)
    elif nombre_operacion == 'mod':
        return mod(n, m)
    else:
        print("Operación no válida.")
        return 0

def calculadora():
    resultado = 0
    while True:
        operacion = leer_operacion()

        if operacion == 'exit':
            print('Goodbye')
            break

        if not ('(' in operacion and ')' in operacion):
            print("Formato inválido. Usa: op(n,m)")
            continue

        nombre = operacion[:3]
        argumentos = operacion[operacion.find("(")+1 : operacion.find(")")]
        
        try:
            n, m = tomar_numeros(argumentos, resultado)
            resultado = ejecutar_operacion(nombre, n, m)
            print("Resultado:", resultado)
        except Exception as e:
            print("Error en la operación:", e)

calculadora()
