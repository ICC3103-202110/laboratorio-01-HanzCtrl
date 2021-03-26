#Super Lab1 de POO
import numpy as np
import random
from copy import deepcopy

def menu():
    print("-------------------------------------------------------------------------\n"
          "Bienvenido al juego de memorice por favor indique la cantidad de pares \n"          "-------------------------------------------------------------------------") 
    Cartas = int(input(" "))
    
    return Cartas

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
    
    
    Simbolos = deepcopy(Matriz)
    for i in range(len(Simbolos)):
        for x in range (len(Simbolos[i])):
            Simbolos[i][x] = "*"
  
  
    
    return Matriz, Simbolos

def Coords(Matriz, Simbolos): #Verificar coordenadas
    temp = 0   
    loop1 = 1
    loop2 = 1
    while True:
        if Matriz == Simbolos:
            print("\nEl tablero se revelo entero!\n")
            return 0, temp, Simbolos, Matriz
        
        while loop1:            
            Cord1 = input("\nIntoduzca la primera Coordenada (x,y): \n").split(",")
            if int(Cord1[0]) > len(Simbolos) or int(Cord1[0]) < 0:
                print("\nEl tablero no es tan grande!\n")
                continue
            
            if int(Cord1[1]) > len(Simbolos[int(Cord1[0])]) or int(Cord1[1]) < 0:
                print("\nEl tablero no es tan grande!\n")
                continue    
            
            for i in range(len(Matriz)):
                for j in range(len(Matriz[i])): 
                    if i == int(Cord1[0]) and j == int(Cord1[1]) :
                        if Simbolos[int(Cord1[0])][int(Cord1[1])] == "*":                            
                            Simbolos[i][j] = Matriz[i][j] 
                            loop1 = 0
                        else:                            
                            print("\nEl numero ya esta revelado!!!\n")
                            Print(Simbolos)
        Print(Simbolos) #Agregar funcion de impresion bonita
        loop1 = 1
                
        while loop2:            
                        
                Cord2 = input("\nIntoduzca la segunda Coordenada (x,y): \n").split(",")
                if Cord2 == Cord1:                 
                    print("\nEy no repitas coordenadas!!\n")
                    Print(Simbolos)
                    continue
                
                if int(Cord2[0]) > len(Simbolos) or int(Cord2[0]) < 0:
                    print("\nEl tablero no es tan grande!\n")
                    continue
            
                if int(Cord2[1]) > len(Simbolos[int(Cord2[0])]) or int(Cord2[1]) < 0:
                    print("\nEl tablero no es tan grande!\n")
                    continue  
                    
                                              
                for i in range(len(Matriz)):
                    for j in range(len(Matriz[i])):               
                        if i == int(Cord2[0]) and j == int(Cord2[1]):  
                            if Simbolos[int(Cord2[0])][int(Cord2[1])] == "*":  
                                Simbolos[i][j] = Matriz[i][j]   
                                loop2 = 0
                            else:                            
                                print("\nEl numero ya esta revelado!!!!!!\n")
                                Print(Simbolos)
        Print(Simbolos)
        
        loop2 = 1
        
        
        if Simbolos[int(Cord1[0])][int(Cord1[1])] != Simbolos[int(Cord2[0])][int(Cord2[1])]:
            print("\nNo hubo match!\n")
            Simbolos[int(Cord1[0])][int(Cord1[1])] = "*"
            Simbolos[int(Cord2[0])][int(Cord2[1])] = "*"
            Print(Simbolos)
            break
        else:
            print("\nObtuviste un 1 punto!\n")
            temp += 1
    return 1, temp, Simbolos, Matriz         

def Print(Matrix):
    print("\nHere is your board!\n")
    for index in range(len(Matrix[0])):  #The first list will always dictate how long the lines will be      
        print("\t", index, end=" ")
    print("\n")
    cont = 0
    
    for fila in Matrix:
        print(cont, end=" ")
        for valor in fila:
            print("\t", valor, end=" ")
        cont += 1
        print()


Pt_1 = 0 #Jugadores
Pt_2 = 0


Cartas = menu () #Al final esto no llego a anda pero aun lo para tener un menu bonito 
X , Y = tablero(Cartas)

Print(Y)

Turn = False #False jugador 1 True jugador 2
while True:
    if Turn:
        print("\nTurno del jugador 2!\n")
    else:
        print("\nTurno del jugador 1!\n")
        
        
    Comp, puntos, Simbolos, Matriz = Coords(X,Y)
    if Turn:
        Pt_2 += puntos
    else:
        Pt_1 += puntos
    if Comp == 0:
        if Pt_1 == Pt_2:
            print("Empataron! con", Pt_1, "puntos")
        elif Pt_1 > Pt_2:
            print("Gano el jugdor 1 con ", Pt_1, "Puntos!")
        else:
            print("Gano el jugador 2 con ", Pt_2, "Puntos!")
        break
    
    Turn = not Turn
            
    





























































    