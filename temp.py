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
    print(len(Matriz))
    nueva_lista = [Matriz[i:i+3] for i in range(0, len(Matriz), 3)]    
    print(nueva_lista)
    print(len(nueva_lista))
tablero(20)        
             
              

    



















































