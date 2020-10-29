special_character_set = (' ', ':', '/')
def Remove_Punc(user_input: str) -> str:
    output = ""
    for character in user_input:
        if character.isalpha() or character in special_character_set or character.isdigit():
            output += character
        elif character == '_':
            output += ' '
    return output

def Remove_Space(user_input: str) -> list:
    return [i.upper() for i in user_input.split(' ') if len(i) > 0]

def Remove_Words(user_input: list, key_words: list) -> int:
    for word in user_input:
        if word in key_words:
            return key_words.index(word)
    return -1

def Parse_Input(user_input: str, key_words: list) -> int:
    return Remove_Words(Remove_Space(Remove_Punc(user_input)), key_words)

if __name__ == "__main__":
    while True:
        a = input("> ")
        print(Parse_Input(a))
    