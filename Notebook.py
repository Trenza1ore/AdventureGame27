from os import system
from time import sleep
from Beautiful_Font import *

All_Notes = []

clue_book = [
    "Found this note on the bathroom mirror: \n Banana WAR U 3:40 5/3",
    "Figlio Inco's a short-tempered guy for sure. The questioning made him mad for some reason...",
    "Just talked to the consigliere, he's drunk and going on and on about how feelings make his work hard. Understandable.",
    "I was chased by a masked man through Manhattan. I believe he was the traitor who wanted to stop my investigation",
    "Angelina Lombardo is the daughter of the Lombardo family's boss." + ' \n ' +\
    "The Lombardo and Giovanni families are allied in their dispute against the Vittorio family." + ' \n ' +\
    "Rosolino was responsible for the recent alliance of the Lombardo and Giovanni families." + ' \n ' +\
    "Rosolino believes that the Lombardo family is the most beneficial to deal with."
]

clue_book.reverse()

def limit_line_length(list_or_words: list, max_line_length: int=60) -> int:
        lines_length = []
        output = [[list_or_words.pop(0)]]
        current_line_num = 0
        current_line_len = len(output[0][0])
        for word in list_or_words:
            word_length = len(word) + 1
            if '\n' in word:
                current_line_num += 1
                current_line_len = 0
                output.append([])
            elif (current_line_len + word_length) < max_line_length:
                output[current_line_num].append(word)
                current_line_len += word_length
            else:
                current_line_num += 1
                current_line_len = word_length - 1
                output.append([word])
        return [' '.join(line) for line in output]

def print_notes() -> None:
    clear_screen()
    print_title("notebook", 0.1)
    print('-' * 105)
    for i in range(len(All_Notes)):
        sleep(0.3)
        words_to_print = limit_line_length(All_Notes[i].split(' '), 100)
        print("%3d. "%(i+1))
        for line in words_to_print:
            print("     " + line)

def add_note() -> None:
    All_Notes.append(clue_book.pop())

# for testing only
if __name__ == "__main__":
    input()
    for _ in range(len(clue_book)):
        add_note()
    print_notes()
