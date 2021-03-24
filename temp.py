#Super Lab1 de POO
import numpy as np
import random

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
        
    Par1 = list(range(1, Cartas+1))
    Par2 = Par1[:]
    Matriz = Par1 + Par2
    random.shuffle(Matriz)
    print(Matriz)
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
    
    a = ""

    for i in range(len(Matriz)):
            
        for x in range(len(Matriz[i])):
               
            print(Matriz[i][x])
            a += str(Matriz[i][x]) + '\t'
    print(a)
      
tablero(9)             
              

    



















































