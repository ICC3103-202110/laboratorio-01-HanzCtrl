#Super Lab1 de POO
import numpy as np
import random
from copy import deepcopy

def menu():
    print("-------------------------------------------------------------------------\n"
          "Bienvenido al juego de memorice por favor indique la cantidad de pares \n"
          "-------------------------------------------------------------------------") 
    return

def tablero(Cartas):
    if Cartas <= 0:
        print("Se necesita al menos 1 par para poder jugar!\n")
        tablero()
    else:
        Dimension = Cartas * 2   
    global Par1    
    Par1 = list(range(1, Cartas+1))

    Matriz = Par1 + Par1
    random.shuffle(Matriz)
                 
    if Dimension % 5 == 0:
        Matriz = [Matriz[i:i+5] for i in range(0, len(Matriz), 5)] #Aca separo la lista en pequeñas listas
    elif Dimension % 4 == 0:
        if Cartas == 2:
            Matriz = [Matriz[i:i+2] for i in range(0, len(Matriz), 2)] #Esto es para que en caso de que sean 2 pares quede un bloue de 2x2
        else:
            Matriz = [Matriz[i:i+4] for i in range(0, len(Matriz), 4)]
    elif Dimension % 2 == 0:
        if Cartas % 2 != 0:
            Matriz = [Matriz[i:i+4] for i in range(0, len(Matriz), 4)] 
        else:
            Matriz = [Matriz[i:i+2] for i in range(0, len(Matriz), 2)] 
        
    #Lo anterior lo hice para poder generar tableros relativamente bonitos y de manera "Automatica"
    #Para numeros como 7 y 9 se generara un tablero de tamaño predeterminado
    
    print(Matriz)
    Simbolos = deepcopy(Matriz)
    for i in range(len(Simbolos)):
        for x in range (len(Simbolos[i])):
            Simbolos[i][x] = "*"
    print(Simbolos) #Crea la matriz de *
  
    
    return Matriz, Simbolos

def Coords(Matriz, Simbolos): #Verificar coordenadas
    temp = 0
    loop1 = 1
    loop2 = 1
    while True:
        while loop1:            
            Cord1 = input("Intoduzca la primera Coordenada (x,y): ").split(",")
            if int(Cord1[0]) > len(Simbolos) or int(Cord1[0]) < 0:
                print("El tablero no es tan grande!")
                continue
            
            if int(Cord1[1]) > len(Simbolos[int(Cord1[0])]) or int(Cord1[1]) < 0:
                print("El tablero no es tan grande!")
                continue    
            
            for i in range(len(Matriz)):
                for j in range(len(Matriz[i])): 
                    if i == int(Cord1[0]) and j == int(Cord1[1]) :
                        if Simbolos[int(Cord1[0])][int(Cord1[1])] == "*":                            
                            Simbolos[i][j] = Matriz[i][j] 
                            loop1 = 0
                        else:                            
                            print("Ya revelaste este numero!!!")
                            print(Simbolos)
        print(Simbolos) #Agregar funcion de impresion bonita
        loop1 = 1
                
        while loop2:            
                        
                Cord2 = input("Intoduzca la segunda Coordenada (x,y): ").split(",")
                if Cord2 == Cord1:                 
                    print("Ey no repitas coordenadas!!")
                    print(Simbolos)
                    continue
                
                if int(Cord2[0]) > len(Simbolos) or int(Cord2[0]) < 0:
                    print("El tablero no es tan grande!")
                    continue
            
                if int(Cord2[1]) > len(Simbolos[int(Cord2[0])]) or int(Cord2[1]) < 0:
                    print("El tablero no es tan grande!")
                    continue  
                    
                                              
                for i in range(len(Matriz)):
                    for j in range(len(Matriz[i])):               
                        if i == int(Cord2[0]) and j == int(Cord2[1]):  
                            if Simbolos[int(Cord2[0])][int(Cord2[1])] == "*":  
                                Simbolos[i][j] = Matriz[i][j]   
                                loop2 = 0
                            else:                            
                                print("Ya revelaste este numero!!!")
                                print(Simbolos)
        print(Simbolos)
        
        loop2 = 1
        
        
        if Simbolos[int(Cord1[0])][int(Cord1[1])] != Simbolos[int(Cord2[0])][int(Cord2[1])]:
            print("No hubo match!")
            Simbolos[int(Cord1[0])][int(Cord1[1])] = "*"
            Simbolos[int(Cord2[0])][int(Cord2[1])] = "*"
            print(Simbolos)
            break
        else:
            print("Obtuviste un 1 punto!")
            temp += 1
    return temp
            
        
        







x,y = tablero(10)

A = Coords(x,y)

print(A)



























































    