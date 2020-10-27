import time
import sys
import random

from Characters import *
from Locations import *
from Normalise import Parse_Input
from Player import Current_Location
#from

def Execute_Talk():
    pass

def Execute_Investigate():
    pass

def Exit_Validation(Chosen_Exit, Possible_Exits):
    for Exit_Direction in Possible_Exits:
        if Chosen_Exit == Exit_Direction:
            return True
    return False

def Execute_Go(Direction):    
    if Exit_Validation(Direction, Current_Location["exits"]):
        Current_Location = Locations[Current_Location["exits"][Direction]]
    else:
        print("You cannot go that way!")

def Execute_Command(Command):

    #This function is getting bloated, is it worth putting in a module?
        
    if len(Command) == 0:
        return
    
    if Command[0] == "go":
        if len(Command) > 1:
            Execute_Go(Command[1])
        else:
            print("Specify direction.")
    elif Command[0] == "investigate":
        if len(Command) > 1:
            Execute_Investigate(Command[1])
            #are there multiple things to investigate in a room?
        else:
            print("Specify your investigation.")
    elif Command[0] == "deal":
        pass

    elif Command[0] == "else":
        pass
    

def Print_Location(Location):
    print("\n"+Location["name"].upper()+"\n"+"\n"+Location["description"]+"\n")

def Char_Print(String_Input):
    for ch in String_Input:
        sys.stdout.write(ch)
        sys.stdout.flush()
        number = random.randrange(25, 65) / 1000
        time.sleep(number)

def Dialogue():
    #Im not fully sure how to implement this
    #Dont know how to make it
    Char_Print("Testtttttttttttttt")
    pass

def Title_Screen():
    print()
    #Big Text showing the title

def Print_Menu(exits):
    print("You can:")
    for direction in exits:
        print("GO" , direction.upper(), "to", All_Locations[exits[direction]]["name"])
        #We need all of the locations set

def Menu(exits):
    Print_Menu(exits)
    #Need to print options for input other than exit
    user_input = input("> ")
    normalised_input = Parse_Input(user_input)
    return normalised_input

def Main():
    Title_Screen()
    
    while True:
        #The order may need to be changed \/
        Dialogue()
        Print_Location(Current_Location)
        Command = Menu(Current_Location["exits"])
        Execute_Command(Command)
        

if __name__ == "__main__":
    Main()
