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
    print(f"Matriz Nro 1 {Matriz}")
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
    print(f"Matriz Nro 2 {Matriz}")
    Simbolos = Matriz[:]
    
    
    return Matriz, print_tab(Matriz)
    
    
    
    
def print_tab(Matriz):
    a = ""
    nums=[1,2,3,4,5,6,7,8,9]
    
    dic = {}

    for i in range(len(Matriz)):

        for x in range(len(Matriz[i])):
            key = f"{i},{x}"
            '''
            print(key,'----',choice)
            if key == choice:
                print("AAAAAAAAAAAA")
                item = dic[key]
                a+="f{item}\t"
            '''
            
            if Matriz[i][x] in nums:
                a+="*\t"
                dic[key] = Matriz[i][x]

        print(a)
        a = ""
    
    return dic
       

def reveal_coord(Matriz,dic,coord):
    print("-------")
    a = ""
    nums=[1,2,3,4,5,6,7,8,9]
    

    for i in range(len(Matriz)):

        for x in range(len(Matriz[i])):
            key = f"{i},{x}"
            if key == coord:
                item = dic[key]
                a+=str(item)+"\t"
            
            
            elif Matriz[i][x] in nums:
                a+="*\t"
             

        print(a)
        a = ""
    
    

matriz, dic = tablero(2)
coord = "1,1"

reveal_coord(matriz,dic,coord)

