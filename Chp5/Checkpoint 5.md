## ¿Qué es un condicional?

Para entender como funciona Python en general se necesita saber lo que es una condicional.

Las condicionales son un elemento usado para crear una aplicación de python que sea dinamica, es decir: crea un **ramificado en base a las condiciones**. Esto tiene muchos usos como por ejemplo poder bloquear y desbloquear partes de la aplicación dependiendo del tipo del usuario, dar preferencia a ciertos procesos ...

```
dieta = "vegetariana" 

if dieta = "vegetariana", "vegana":
   print("No comes carne")
else:
   print("Comes carne")
```
Ejemplo basico de una condicional cuyo valor es un hilo. En este caso dependiendo del valor de dieta el codigo hara print de una de los dos resultados dependiendo del valor de `dieta`. Tambien se puede usar para comparaciones de valores numericos.

```
comensales = 23

if comensales <= 8:
   print("Comereis en la sala pequeña")
if comensales >= 8:
   print("Hay que reservar mesa")
if comensales >= 15:
   print("Comereis en la sala grande")
```

## ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

En python hay dos tipos principales de bucles, estos son procesos que se usan para repetir ciertas tareas de codigo automaticamente y sin tener que re-escribir la tarea una y otra vez.

**Bucles `for-in`**:  Son un tipo de bucles finito, es decir; cuenta con la capacidad de poder fijarse en ella el numero de veces que se repetira el codigo en question sin depender del resultado de la tarea. 

```
frutas = ["kiwi", "mispero", "manzana"]

for fruta in frutas:
    print(fruta)
```


**Bucles `while`**: Son un tipo de bucle infinito. Lo cual implica que el codigo se repetira infinitas veces. Esto tiene la negativa de que puede soprecargar un sistema debido a no poner una condicion que cause el final de bucle.

```
cuenta = 1

while cuenta <= 5:
    print(cuenta)
    cuenta += 1  

```
(con el incremento de 1 se evita que el bucle entre en infinito)
## ¿Qué es una lista por comprensión en Python?

Es una metodo para crear y definir listas a partir de elementos como otras listas o hilos, tambien aplicando modificaciones o filtros a cada elemento. La syntaxis es más breve y más simple de comprender que un bucle `for-in`.

Unos ejemplos:
##### Combinar dos listas por pares
```
colores = ["rojo", "verde"]
gemas = ["ruby", "esmeralda"]
combinados = [f"{color} {gema}" for color in colores for gema in gemas]
```

##### Extraer las primeras palabras de una lista
```
trabajadores = ["Yonta", "Cavalero", "Quinn"]
iniciales = [trabajador[0] for trabajador in trabajadores]
```


##### Transformacion con condiciones
```
clasificación = ["Aprobado" if nota >= 5 else "Suspendido" for nota in [4, 6, 3, 8]]
```

## ¿Qué es un argumento en Python?

Un **argumento** es un valor concreto que pasa por una **función** cuando se le nombra. Esto permite customizar el comportamiento de la función, ya que se le han proporcionado instrucciones sobre como llevar adelante el proceso en cuestion. 

```
def saludo(nombre, mensaje):
    print(f"{mensaje}, {nombre}!")

saludo("Carlos", "Buenas tardes")
```
En este caso, esto es un argumento posicional asique el valor de cada argumento se define por posición. Si en cambio este fuera de palabra clave (keyword) tendriamos algo tal que así:

```
saludar(mensaje="Hola", nombre="Carlos")  
```

Tener en cuenta que si no se fija un valor este contara con un valor predeterminado. En el caso de `huevo frito` al no fijar la `compa`, el predeterminado es `patatas`, asique python leera el `print` e rellenara el vacio de `compa` con el predeterminado.

```
def comida(tipo, compa="patatas"):
    print(f"comida: {tipo} con {compa}")

comida("huevo frito")               
comida("filete", topping="pimientos")
```

## ¿Qué es una función Lambda en Python?

Es una función anónima  (es decir, sin nombre) y rápida que se define usando una sola linea de code en operaciones sencillas que no requieren una función tradicional  con `def`, contienen una sola expresion y que son de uso puntual.

```
reversa = lambda s: s[::-1]
print(reversa("python"))
```
## ¿Qué es un paquete pip?

Conjunto de archivos en formato `.py` empaquetados para distribuir funcionalidades  tales como `numpy`, `requests`... mediante `pip` que es la herramienta en sistema de comandos de manejo  de paquetes oficial de Python. Se usa para instalar, actualizar y desinstalar bibliotecas/librerías de paquetes hechos por terceros desde el **[Python Package Index (PyPI)](https://pypi.org/)** y otros repositorios. 



