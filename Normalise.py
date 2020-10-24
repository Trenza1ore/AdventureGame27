from Locations import *

key_words = ["go", "notebook"]

def Remove_Punc(user_input: str) -> str:
    output = ""
    for character in user_input:
        if character.isalpha() or character == ' ':
            output += character
        elif character == '_':
            output += ' '
    return output

def Remove_Space(user_input: str) -> list:
    return [i.lower() for i in user_input.split(' ') if len(i) > 0]

def Remove_Words(user_input: list) -> dict:
    command = {
    "operand": "",
    "operator": ""
    }
    for word in user_input:
        if word in key_words:
            command["operator"] = word
        elif word in All_Locations:
            command["operand"] = word
    return command

def Parse_Input(user_input: str) -> dict:
    return Remove_Words(Remove_Space(Remove_Punc(user_input)))

if __name__ == "__main__":
    while True:
        a = input("> ")
        print(Parse_Input(a))
    