import numpy as np
import random
from copy import deepcopy
class Cards(): #This part just creates the two matrixes that im going to use
    def __init__(self, Card):
        self.Card = Card

    def tablero(self):
        if self.Card <= 0:
            print("You need at least 1 pair to play! \n")
            tablero()
        else:
            Dimension = self.Card * 2   

        global Pair1    
        Pair1 = list(range(1, self.Card+1))

        Matrix = Pair1 + Pair1
        random.shuffle(Matrix)
                 
        if Dimension % 5 == 0:
            Matrix = [Matrix[i:i+5] for i in range(0, len(Matrix), 5)] #Aca separo la lista en pequeñas listas
        elif Dimension % 4 == 0:
            if self.Card == 2:
                Matrix = [Matrix[i:i+2] for i in range(0, len(Matrix), 2)] #Esto es para que en caso de que sean 2 pares quede un bloue de 2x2
            else:
                Matrix = [Matrix[i:i+4] for i in range(0, len(Matrix), 4)]
        elif Dimension % 2 == 0:
            if self.Card % 2 != 0:
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

   
class Board():
    def __init__(self, Matrix, Symbols):
        self.Matrix = Matrix
        self.Symbols = Symbols

    def Print(self):
        print("\nHere is your board!\n")
        for index in range(len(self.Symbols[0])):  #The first list will always dictate how long the lines will be      
            print("\t", index, end=" ")
        print("\n")
        cont = 0
    
        for fila in self.Symbols:
            print(cont, end=" ")
            for valor in fila:
                print("\t", valor, end=" ")
            cont += 1
            print()

    def Coords(self): #Verificar coordenadas
        temp = 0   
        loop1 = 1
        loop2 = 1
        while True:
            if self.Matrix == self.Symbols:
                print("\nThe whole board has been revealed! \n")
                return 0, temp, self.Symbols, self.Matrix
        
            while loop1:            
                Cord1 = input("\nPlease write the first coordinate x,y: \n").split(",")
                if int(Cord1[0]) > len(self.Symbols) or int(Cord1[0]) < 0:
                    print("\nThe board is not that big!\n")
                    continue
            
                if int(Cord1[1]) > len(self.Symbols[int(Cord1[0])]) or int(Cord1[1]) < 0:
                    print("\nThe board is not that big!\n")
                    continue    
            
                for i in range(len(self.Matrix)):
                    for j in range(len(self.Matrix[i])): 
                        if i == int(Cord1[0]) and j == int(Cord1[1]) :
                            if self.Symbols[int(Cord1[0])][int(Cord1[1])] == "*":                            
                                self.Symbols[i][j] = self.Matrix[i][j] 
                                loop1 = 0
                            else:                            
                                print("\nThat number has already been revealed!!!\n")
                                self.Print()
            self.Print() #Agregar funcion de impresion bonita
            loop1 = 1
                
            while loop2:            
                        
                    Cord2 = input("\nPlease write the second coordinate x,y: \n").split(",")
                    if Cord2 == Cord1:                 
                        print("\nHey do not repeat coordinates!!\n")
                        self.Print()
                        continue
                
                    if int(Cord2[0]) > len(self.Symbols) or int(Cord2[0]) < 0:
                        print("\nThe board is not that big!\n")
                        continue
            
                    if int(Cord2[1]) > len(self.Symbols[int(Cord2[0])]) or int(Cord2[1]) < 0:
                        print("\nThe board is not that big!\n")
                        continue  
                    
                                              
                    for i in range(len(self.Matrix)):
                        for j in range(len(self.Matrix[i])):               
                            if i == int(Cord2[0]) and j == int(Cord2[1]):  
                                if self.Symbols[int(Cord2[0])][int(Cord2[1])] == "*":  
                                    self.Symbols[i][j] = self.Matrix[i][j]   
                                    loop2 = 0
                                else:                            
                                    print("\nThat number has already been revealed!!!!!!\n")
                                    self.Print()
            self.Print()
        
            loop2 = 1
        
        
            if self.Symbols[int(Cord1[0])][int(Cord1[1])] != self.Symbols[int(Cord2[0])][int(Cord2[1])]:
                print("\nNo match!\n")
                self.Symbols[int(Cord1[0])][int(Cord1[1])] = "*"
                self.Symbols[int(Cord2[0])][int(Cord2[1])] = "*"
                self.Print()
                break
            else:
                print("\nYou got 1 point!\n"
                "You get another turn!\n")
                temp += 1
        return 1, temp, self.Symbols, self.Matrix

  

