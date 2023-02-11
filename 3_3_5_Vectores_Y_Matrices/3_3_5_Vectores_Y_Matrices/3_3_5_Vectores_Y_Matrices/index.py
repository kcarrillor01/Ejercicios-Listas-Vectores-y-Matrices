"""
Servicio Nacional de Aprendizaje SENA
Kevin Felipe Carrillo Romero
Ficha 2617818
Fundamentos de Programacion
trabajo 3.3.5: Vectores y Arreglos
"""


#Importamos todas las funciones que cree para este trabajo
import funciones


"""EJERCICIO 1.Llenar dos vectores A y B de 45 elementos cada uno, sumar el elemento uno del vector A con el elemento uno del vector B y así sucesivamente hasta 45, almacenar el resultado en un vector C, e imprimir los vectores originales y el resultante. """

#Cabe aclarar que entendi que solo se suman A[0]+B[0], A[1]+B[1], A[2]+B[2], etc, es decir solo cuando sus indices son iguales hasta A[45]+B[45]

#Creamos A y B con un mismo tamaño n=45, decido que se llene aleatoriamente con numeros entre -10 y 10 usando la funcion lista_random que cree.
n=45
r=10
A=funciones.lista_random(n,r)
B=funciones.lista_random(n,r)
#Creamos un vector C que seria la diagonal de la matriz A+B (y llamamos la funcion que lo calcula )
C=funciones.suma_diagonal_pricipal(A,B)
#Imprimimos todo lo que pide el ejercicio
print("Ejercicio 1 \n \n")
print(f"A = {A}\n\nB ={B}\n\nC = A+B = {C}")



"""EJERCICIO 2. Almacenar 300 números en un vector, imprimir cuantos son ceros, cuantos son negativos, cuantos positivos. Imprimir además la suma de los negativos y la suma de los positivos."""

#Funcion que crea una lista numeros con 300 valores aleatorios en un rango de -10 a 10
numeros=funciones.lista_random(300, 10)
#Usamos la funcion que permiten clasificar los numeros de un vector en positivos, neutros y negativos. Y tambien la que permite sumar todos los positivos y a aparte todos los negativos (la suma de todos los neutros da 0), Esa informacion la guardo en clasificacion y sumatoria para aligerar el print 
clasificacion=funciones.enteros_clasificaion(numeros)
sumatoria=funciones.suma_segun_clasificacion(numeros)
#Imprimimos todo lo que el ejercicio pide
print("\n \n Ejercicio 2 \n \n")
print(f"Vector = {numeros}\n\nEn este vector de {len(numeros)} números, {clasificacion[0]} son positivos, {clasificacion[1]} son neutros, y {clasificacion[2]} son negativos.\n\nLa suma de todos los positivos da: {sumatoria[0]}, mientras que al sumar todos los negativos da: {sumatoria[1]}")



"""EJERCICIO 3. Almacenar 150 números en un vector, almacenarlos en otro vector en orden inverso al vector original e imprimir el vector resultante"""

#Creamos un vector aleatorio con 150 numeros n y un rango aleatorio de -10 a 10
original= funciones.lista_random(150,10)
#Llamamos la funcino que cree que invierte el orden de cualquier lista
inverso= funciones.lista_invertida(original)
#Imprimimos lo que pide el ejercicio
print("\n\nEjercicio 3 \n\n")
print(f"El vector original\n{original}\nEl vector invertido\n{inverso}")



"""EJERCICIO 4.  Almacenar 500 números en un vector, elevar al cuadrado cada valor almacenado en el vector, almacenar el resultado en otro vector. Imprimir el vector original y el vector resultante"""

#Creamos el vector de tamaño 500 y rango (-100,10)
vector=funciones.lista_random(500,10)
#Creamos el vector cuadrado que gaurdara el resultado de cada valor de vector elevado al cuadrado
cuadrado=[]
for i in range(len(vector)):
    cuadrado.append(vector[i]*vector[i])
#Imprimimos lo que pide el ejercicio
print("\n\n Ejercicio 4\n\n")
print(f"El Vector original es: \n{vector} \nEl vector de los cuadrados es: \n{cuadrado}")



"""Ejercicio 5. Hacer un algoritmo que almacene números en una matriz de 5 * 6. Imprimir la suma de los números almacenados en la matriz."""

#Usamos una funcion que crea matrices aleatorias de tamaño 5x6 con valores aleatorios entre 0 y 10
matriz=funciones.matriz_random(5,6,0,10)
suma=0
#Para cada iteracion, i es un vector dentro de la matriz, por eso vamos a usar la funcion que suma todos los numeros de un vector para cada i, los guardamos en sumaAux y los vamos sumando entre ellos en la variable suma
for i in matriz:
    sumaAux=funciones.suma_en_lista(i)
    suma=suma+sumaAux
#imprimimos lo que pide el ejercicio
print("\n\nEjercicio 5\n\n")
print("La matriz aleatoria es: ")
for i in matriz:
    print(i)
print(f"y la suma de todos los numeros almacenados en ella da: {suma}")



"""EJERCICIO 6. Hacer un algoritmo que llene una matriz de 5 * 5 y que almacene la diagonal principal en un vector. Imprimir el vector resultante."""

#Creamos la matriz 5x5 con valores aleatorios desde 0 hasta 10
matriz=funciones.matriz_random(5,5,0,10)
#Usamos una funcioon que regresa la diagonal principal del vector
diagonal=funciones.diagonal_principal(matriz)
#Imprimimos lo que pide el ejercicio
print("\n\nEjercicio 6\n\n")
print("La matriz es:")
for i in matriz:
    print(i)
print(f"Entonces la diagonal principal es el vector: \n{diagonal}")



"""EJERCICIO 7. Hacer un algoritmo que llene una matriz de 10 * 10 y que almacene en la diagonal principal unos y en las demás posiciones ceros"""

#Creamos una matriz "Aleatoria" de tamaño 10x10 pero de rango que vaya de 0 a 0 (asi es una matriz de solo ceros)
matriz=funciones.matriz_random(10,10,0,0)
#Usamos una funcin que llene la diagonal de una matriz nxn con un parametro dado
matriz=funciones.valor_en_diagonal_principal(matriz,1)
#Imprimimos lo que pude el ejercicio
print("\n\nEjercicio 7\n\n")
for i in matriz:
    print(i)



"""EJERCICIO 8. Hacer un algoritmo que llene una matriz de 5 * 6 y que imprima cuantos de los números almacenados son ceros, cuantos son positivos y cuantos son negativos"""


#Creamos la matriz aleatoria 5x6 con valores aleatorios de -10 a 10
matriz=funciones.matriz_random(5,6,-10,10)
#Vamos a reciclar tambien la funcion que cuenta los positivos, los neutros y los negativos, vamos a llamarla para cada vector dentro de la matriz

#Para no perder la informacion de dicha funcion vamos a crear globalmente las variables positivo, negativo y neutro
positivo=0
neutro=0
negativo=0
for i in range(len(matriz)):
    clasificacion=funciones.enteros_clasificaion(matriz[i])
    #Recordemos que enteros_clasificacion(vector) retorna un vector [positivos, neutros, negativos]
    positivo=positivo+clasificacion[0]
    neutro=neutro+clasificacion[1]
    negativo=negativo+clasificacion[2]
#Imprimir lo que pide el ejercicio
print("\n\n Ejercicio 8\n\n")
print("La matriz aleatoria es: \n")
for i in matriz:
    print(i)
print(f"\nEntonces hay {positivo} numeros positivos, {neutro} numeros neutros y {negativo} numeros negativos")