from Characters import *
from Locations import *
from Normalise import Parse_Input
from Player import Current_Location
#from



def Print_Location(Location):
    print("\n"+Location["name"].upper()+"\n"+"\n"+Location["description"]+"\n")

def Dialogue():
    #Im not fully sure how to implement  this
    pass

def Title_Screen():
    print()
    #Big Text showing the title

def Print_Menu(exits)
    for direction in exits:
        print("GO " + direction.upper() + " to " + Location[exits[direction]]["name"] + ".")
        #We need all of the locations set

def Menu(exits, clues):
    Print_Menu(exits)
    
    input()
    pass

def Main():
    Title_Screen()
    
    while True:
        Dialogue()
        Print_Location(Current_Location)
        Command = Menu(Current_room["exits"], Current_room["clues"])

if __name__ == "__main__":
    Main()
