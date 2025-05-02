# Cree un bucle For de Python.
for ejercicio_1 in range(1, 13):
    print(ejercicio_1)

# Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
def suma(a,b,c):
    return a + b + c

ejercicio_2 = suma(200, 210, 10)
print(ejercicio_2)

# Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
suma_con_lambda = lambda a, b, c: a + b + c
ejercicio_3 = suma_con_lambda(20, 9, 40)
print(ejercicio_3)

# -Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.
nombre = 'Enrique'
lista_nombre ='Jessica', 'Paul', 'George', 'Henry', 'Adán'

if nombre in lista_nombre:
    print(f"{nombre} SI está aquí.")
else:
    print(f"{nombre} NO está aqui.")