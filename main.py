from Classes import Cards
from Classes import Board

def menu():
    print("-------------------------------------------------------------------------\n"
          "                     Welcome to the memory game! \n"    
          "                 Please indicate how many pairs you want!\n"
          "            Remember that this game only accept numbers as answers\n"
                           
          "-------------------------------------------------------------------------") 
    Cards = int(input("Number of pairs: "))
    
    return Cards

A = Cards(menu())
x,y = Cards.tablero(A)



Pt_1 = 0 #Jugadores
Pt_2 = 0
B = Board(x,y)

B.Print()

Turn = False #False jugador 1 True jugador 2
while True:
    if Turn:
        print("\nPlayer 2 turn!\n")
    else:
        print("\nPlayer 1 turn!\n")
        
        
    
    Comp, puntos, Symbols, Matrix = B.Coords()

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
