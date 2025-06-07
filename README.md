# Proyecto Calculadora 2.0 

### descripcion:
Es una calculadora capas de hacer las siguientes operaciones: suma, resta, multiplicasion y division y módulo. Está dirigida a personas que necesitan una herramienta funcional desde la terminal, para resolver ecuaciones matemáticas. Su objetivo principal es facilitar el cálculo de manera rápida, practica y utilizando el resultado final para otra operacion.

### Caracteristicas Principales
Calculadora escrita 100% en Python
Para las siguientes operaciones:
1. `add`: suma
2. `sub`: resta
3. `mul`: multiplicación
4. `div`: división (teniendo en cunta que no puede dividir por cero)
5. `mod`: módulo (es el resultado de una division)
6. tambien nos permite reutiloizar el resultado con la letra `r`.
7. con exit lo que hace es salir de la calculadora si ya no desea seguir `exit`

### Estructura Del Proyecto

* `CALC.py` El codigo principal que contiene la calculadora
* `README.md` Documentación del proyecto escrito en Markdown

### Como Ejecutar El Proyecto
Tener instalado Python en el sistema 

1. Descargar o clonar el proyecto
Se clona el repositorio si está en GitHub o simplemente guardar el archivo calculadora.py en una carpeta.

* `git clone https://github.com/tuusuario/calculadora.git`
cd calculadora
2. Ejecutar el programa
Desde la terminal o línea de comandos ejecuta el archivo con: python `calculadora.py`

3. Interactuar con la calculadora
Una vez iniciada escribe comandos de la siguiente manera:

calc operación:`número1,número2`
Ejemplos:
* `calc (add:5,3)`         Resultado: 8
* `calc (div:10,2)`        Resultado: 5.0
* `calc (mul:r,4)`         Usa el resultado anterior (r) y lo multiplica por 4

4. Salir del programa
Para cerrar la calculadora escribir `exit`

### Como probarlo 
Al iniciar el programa, se pedira ingresar una operación de la siguiente manera:
* `número1,número2`
* Por ejemplo: `calc add(5,3)`
* Para reutilizar un resultado usar la `r`:
* Si desea salir escribir: `exit`

### Modulo 
* Estas son las funciones de las operaciones: 
* add(n, m): return n + m
* sub(n, m): return n - m
* mul(n, m): return n * m
* mod(n, m): return n % m
* div(n, m): return 0 if m == 0 else n / m
* Estas funciones realizan las operaciones. El módulo div( especifica que no puede dividir por cero)

Como lee el comando 
* con una definicion `leer_operacion()`
Esta solicita al usuario un primer numero

Con otra definicion tomar_numeros(numeros_operacion, resultado)
toma todos los numeros y si desea reutilizar el resultado pone la `r`.

Ejecución de operacioUna definicion ejecutar_operacion(nombre_operacion, n, m)
Llama a la función correspondiente según sea: `(add, sub, etc)` y retorna el resultado.

Función principal
* definir la:  `calculadora()`
* Es el bucle principal que mantiene la calculadora funcionando hasta que se ingrese `exit` 
### Autores
* Colaborador desarrollo: Sebastian Martinez 
* Autor desarrollo: Johan Ramirez 
* Autor documentacion: Johan Ramirez
