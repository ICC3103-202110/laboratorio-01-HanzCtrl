#Super Lab1 de POO
import numpy as np
import random
from copy import deepcopy


#Me di cuenta muy tarde que idealmente tenia que estar en ingles asi que las variables seran en español perdoooon!
def menu():
    print("-------------------------------------------------------------------------\n"
          "                     Welcome to the memory game! \n"    
          "                 Please indicate how many pairs you want!\n"
          "            Remember that this game only accept numbers as answers\n"
                           
          "-------------------------------------------------------------------------") 
    Cards = int(input("Number of pairs: "))
    
    return Cards

def tablero(Cards):
    if Cards <= 0:
        print("You need at least 1 pair to play! \n")
        tablero()
    else:
        Dimension = Cards * 2   
    global Pair1    
    Pair1 = list(range(1, Cards+1))

    Matrix = Pair1 + Pair1
    random.shuffle(Matrix)
                 
    if Dimension % 5 == 0:
        Matrix = [Matrix[i:i+5] for i in range(0, len(Matrix), 5)] #Aca separo la lista en pequeñas listas
    elif Dimension % 4 == 0:
        if Cards == 2:
            Matrix = [Matrix[i:i+2] for i in range(0, len(Matrix), 2)] #Esto es para que en caso de que sean 2 pares quede un bloue de 2x2
        else:
            Matrix = [Matrix[i:i+4] for i in range(0, len(Matrix), 4)]
    elif Dimension % 2 == 0:
        if Cards % 2 != 0:
            Matrix = [Matrix[i:i+4] for i in range(0, len(Matrix), 4)] 
        else:
            Matrix = [Matrix[i:i+2] for i in range(0, len(Matrix), 2)] 
        
    #Lo anterior lo hice para poder generar tableros relativamente bonitos y de manera "Automatica"
    #Para numeros como 7 y 9 se generara un tablero de tamaño predeterminado
    
    
    Symbols = deepcopy(Matrix)
    for i in range(len(Symbols)):
        for x in range (len(Symbols[i])):
            Symbols[i][x] = "*"
  
  
    
    return Matrix, Symbols

def Coords(Matrix, Symbols): #Verificar coordenadas
    temp = 0   
    loop1 = 1
    loop2 = 1
    while True:
        if Matrix == Symbols:
            print("\nThe whole board has been revealed! \n")
            return 0, temp, Symbols, Matrix
        
        while loop1:            
            Cord1 = input("\nPlease write the first coordinate x,y: \n").split(",")
            if int(Cord1[0]) > len(Symbols) or int(Cord1[0]) < 0:
                print("\nThe board is not that big!\n")
                continue
            
            if int(Cord1[1]) > len(Symbols[int(Cord1[0])]) or int(Cord1[1]) < 0:
                print("\nThe board is not that big!\n")
                continue    
            
            for i in range(len(Matrix)):
                for j in range(len(Matrix[i])): 
                    if i == int(Cord1[0]) and j == int(Cord1[1]) :
                        if Symbols[int(Cord1[0])][int(Cord1[1])] == "*":                            
                            Symbols[i][j] = Matrix[i][j] 
                            loop1 = 0
                        else:                            
                            print("\nThat number has already been revealed!!!\n")
                            Print(Symbols)
        Print(Symbols) #Agregar funcion de impresion bonita
        loop1 = 1
                
        while loop2:            
                        
                Cord2 = input("\nPlease write the second coordinate x,y: \n").split(",")
                if Cord2 == Cord1:                 
                    print("\nHey do not repeat coordinates!!\n")
                    Print(Symbols)
                    continue
                
                if int(Cord2[0]) > len(Symbols) or int(Cord2[0]) < 0:
                    print("\nThe board is not that big!\n")
                    continue
            
                if int(Cord2[1]) > len(Symbols[int(Cord2[0])]) or int(Cord2[1]) < 0:
                    print("\nThe board is not that big!\n")
                    continue  
                    
                                              
                for i in range(len(Matrix)):
                    for j in range(len(Matrix[i])):               
                        if i == int(Cord2[0]) and j == int(Cord2[1]):  
                            if Symbols[int(Cord2[0])][int(Cord2[1])] == "*":  
                                Symbols[i][j] = Matrix[i][j]   
                                loop2 = 0
                            else:                            
                                print("\nThat number has already been revealed!!!!!!\n")
                                Print(Symbols)
        Print(Symbols)
        
        loop2 = 1
        
        
        if Symbols[int(Cord1[0])][int(Cord1[1])] != Symbols[int(Cord2[0])][int(Cord2[1])]:
            print("\nNo match!\n")
            Symbols[int(Cord1[0])][int(Cord1[1])] = "*"
            Symbols[int(Cord2[0])][int(Cord2[1])] = "*"
            Print(Symbols)
            break
        else:
            print("\nYou got 1 point!\n"
                  "You get another turn!\n")
            temp += 1
    return 1, temp, Symbols, Matrix         

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


Cards = menu () #Al final esto no llego a anda pero aun lo para tener un menu bonito 
X , Y = tablero(Cards)

Print(Y)

Turn = False #False jugador 1 True jugador 2
while True:
    if Turn:
        print("\nPlayer 2 turn!\n")
    else:
        print("\nPlayer 1 turn!\n")
        
        
    Comp, puntos, Symbols, Matrix = Coords(X,Y)
    if Turn:
        Pt_2 += puntos
    else:
        Pt_1 += puntos
    if Comp == 0:
        if Pt_1 == Pt_2:
            print("There was a tie with", Pt_1, "points")
        elif Pt_1 > Pt_2:
            print("Player 1 won with", Pt_1, "Points!")
        else:
            print("Player 2 won with", Pt_2, "Points!")
        break
    
    Turn = not Turn
            
    





























































    