#importo randint porque me interesa llenar vectores de numeros aleatorios en lugar de exigirle al ususario que digite 300+ numeros diferentes
from random import randint

#Esta funcion pide una lista, un tamaño para la lista n y un rango r, devuelve una lista de tamaño n llena de numeros enteros aleatorios entre -r y r.
def lista_random (n, r):
    lista=[]
    for i in range (n):
        valor= randint(-r,r)
        lista.append(valor)
    return lista

#Esta funcion pide una lista y devuelve cuantos de numeros de la lista son positivos, cuantos son 0 (neutros) y cuantos negativos
def enteros_clasificaion(lista):
    positivos=0
    negativos=0
    neutros=0
    for i in lista:
        if i > 0:
            positivos=positivos+1
        elif i == 0:
            neutros= neutros+1
        else:
            negativos= negativos+1
    return [positivos, neutros, negativos]

#Esta funcion suma todos los numeros positivos y ceros, y luego suma todos los numeros negativos, devuleve un vector con estos 2 valores
def suma_segun_clasificacion(lista):
    positivos=0
    negativos=0
    for i in lista:
        if i >= 0:
            positivos=positivos+i
        else:
            negativos= negativos+i
    return[positivos, negativos]

#Esta funcion coge la matriz Vector1+Vector2 y regresa el vector de la diagonal principal como un vector3
def suma_diagonal_pricipal (vector1, vector2):
    vector3=[]
    if len(vector1)==len(vector2):
        for i in range(len(vector1)):
            for j in range(len(vector2)): 
                if i==j:
                    vector3.append(vector1[i]+vector2[j])
        return vector3
    else:
        print("Esta funcion necesita que el vector 1 y el vector 2 sean del mismo tamaño")
        return 0

#_Una funcion que le de vuelta al orden de un vector
def lista_invertida(lista):
    listaInvertida=[]
    for i in lista:
        listaInvertida.insert(0,i)
    return listaInvertida

#Una Funcion que crea una matriz aleatoria de tamaño nxm, con numeros que vienen desde r hasta R
def matriz_random(n,m,r,R):
    matriz=[]
    for i in range(n):
        lista=[]
        for j in range(m):
            lista.append(randint(r,R))
        matriz.append(lista)
    return matriz

#Una funcion que suma todos los numeros de un vector
def suma_en_lista(lista):
    suma=0
    for i in lista:
        suma= suma+i
    return suma

#Una funcion que dada una matriz nxn regresa la diagonal principal
def diagonal_principal(matriz):
    diagonal=[]
    for i in range(len(matriz)):
        lista=matriz[i] #(asi vamos viendo cada lista dentro de matriz indivualmente)
        for j in range(len(matriz)):
            #Con este if nos aseguramos que solo obtenga los valores de la matriz en las posiciones 
            #(0,0),(1,1),(2,2),...,(n,n) 
            if i==j:
                diagonal.append(lista[j])
    return diagonal

#Una funcion que cambia la diagonal principal con un parametro "valor"
def valor_en_diagonal_principal(matriz, valor):
    for i in range(len(matriz)):
        lista=matriz[i] #(asi vamos viendo cada lista dentro de matriz indivualmente)
        for j in range(len(matriz)):
            #Con este if nos aseguramos que solo cambia los valores de la matriz en las posiciones 
            #(0,0),(1,1),(2,2),...,(n,n) 
            if i==j:
                lista[j]=1
        #Insertamos el vector modificado antes de que se pierda
        matriz[i]=lista
    return matriz
