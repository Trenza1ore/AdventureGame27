from os import system
from time import sleep
from Beautiful_Font import *

All_Notes = []

clue_book = {
    "friend"    : "My loyal friend who has helped me a lot." * 10,
    "boss"      : "My boss Mariano Giovanni." * 10,
    "suspect_1" : "Suspect 1: Manuele Mariano." * 10,
    "suspect_2" : "Suspect 2: Roberto Orazio." * 10,
    "suspect_3" : "Suspect 3: Figlio Incompetente." * 10,
    "suspect_4" : "Suspect 4: Angelo Rosolino." * 10
}

def limit_line_length(list_or_words: list, max_line_length: int=60) -> int:
        lines_length = []
        current_line_num = 0
        current_line_len = 0
        output = [[list_or_words.pop(0)]]
        for word in list_or_words:
            word_length = len(word) + 1
            if (current_line_len + word_length) > max_line_length:
                current_line_num += 1
                current_line_len = word_length - 1
                output.append([word])
            else:
                output[current_line_num].append(word)
                current_line_len += word_length
        return [' '.join(line) for line in output]

def print_notes() -> None:
    clear_screen()
    print_title("notebook", 0.1)
    print('-' * 100)
    for i in range(len(All_Notes)):
        sleep(0.3)
        words_to_print = limit_line_length(All_Notes[i].split(' '), 100)
        print("%3d. "%(i+1))
        for line in words_to_print:
            print("     " + line)

if __name__ == "__main__":
    input()
    for i in clue_book:
        All_Notes.append(clue_book[i])
    print_notes()