from Normalise import Parse_Input
from Notebook import limit_line_length, print_notes, All_Notes, clue_book
from time import sleep
from Beautiful_Font import *
from os import remove

try:
    remove("player_notes")
    remove("save")
except:
    pass
script_tags = [
    "<title>",
    "<slide>",
    "<choice>",
    "<go back>",
    "<pause>",
    "<loop choice>",
    "<change word>",
    "<Unknown>",
    "<Unknown>",
    "<Unknown>"
]
special_tags = [
    "<lose 1 hp>",
    "<add clue>",
    "<notebook>",
    "<save final choice>"
    ]
script_tags = ["<%d>"%(i) for i in range(10)] + script_tags + ["<loop %d>"%(i) for i in range(10)]
input()
script_tags_end = ["</" + tag[1:] for tag in script_tags]
screen = []
screen_row_length = 105
current_scene = "placeholder scene"
current_scene_num = -1
full_hp = 5

try:
    player_notes = []
    savefile = open("player_notes", 'r', encoding="utf-8")
    note_num = int(savefile.read())
    savefile.close()
    for i in range(note_num):
        player_notes.append(clue_book.pop())
    remaining_notes = clue_book.copy()
except:
    player_notes = []
    remaining_notes = clue_book.copy()

class Choice:
    def __init__(self, first_line: str, second_line: str) -> None:
        first_line = first_line.split(',')
        second_line = second_line.split(',')
        self.choices = {first_line[i]:second_line[i] for i in range(len(first_line))}
    def set_choices(self, line_of_text: str) -> None:
        self.question = line_of_text

def display_screen() -> None:
    global screen
    clear_screen()
    for line in screen:
        print(line)

def display_sliding(sliding_line: str, animation_delay: float=0) -> None:
    global screen, screen_row_length
    line_length = len(sliding_line)
    for i in range(1, screen_row_length + 1):
        j = max(i, line_length)
        clear_screen()
        for line in screen:
            print(line)
        print(" " * (screen_row_length - i) + sliding_line[:j])
        sleep(animation_delay)
    screen.append(sliding_line)

def load_from_text(file_name: str="script/game_script_final_lets_get_this_bread.txt", file_encoding: str="utf-8") -> list:
    file = open(file_name, 'r', encoding=file_encoding)
    file.readline()
    content = [line[:-1] for line in file.readlines()]
    file.close()
    return content

def parse_script(content: list, per_line_delay: float=0.5, current_hp: int=5, debugging: bool=False, start_line: int=0) -> None:
    global current_scene, screen, current_scene_num, full_hp, player_notes, remaining_notes
    clear_screen()
    current_line_num = start_line
    script_length = len(content)
    is_tag = False
    loop_choice = [False, False, False]
    loop_choice_index = -1
    loop_start_line_num = -1
    final_choice = False
    tag_type = 100 # just a random initial value
    choice_num = 1 # number of choices when making a decision
    choice_index = -1 # which path did the player chose
    choice_start_line_num = -1
    while current_line_num < script_length:
        if debugging:
            print("line", current_line_num)
            input()
        if current_hp < 1:
            input("\nYou died.\nPress ENTER key to continue...\n")
            print_title("game over")
            input("\n%s\nPress ENTER key to return to the start of this chapter...\n%s\n"%('-' * 105, '-' * 105))
            savefile = open("save", 'r', encoding="utf-8")
            current_line_num, current_scene_num = (int(i) for i in savefile.readline().split(','))
            savefile.close()
            current_hp = full_hp
            screen = []
            continue
        current_line = content[current_line_num]
        if current_line in script_tags:
            is_tag = True
            if debugging:
                print(current_line_num, current_line)
                input()
            tag_type = script_tags.index(current_line)
            current_line_num += 1
            continue
        elif current_line in script_tags_end:
            is_tag = False
            if debugging:
                print(current_line_num, current_line)
                input()
            current_line_num += 1
            continue
        elif current_line in special_tags:
            special_tag_type = special_tags.index(current_line)
            if special_tag_type == 0:
                current_hp -= 1
                current_line_num += 1
                for _ in range(3):
                    clear_screen()
                    display_screen()
                screen.append("You have lost 1HP, current HP: " + '◉ ' * current_hp + '◎ ' * (full_hp - current_hp))
                display_screen()
                continue
            elif special_tag_type == 1:
                current_line_num += 1
                player_notes.append(remaining_notes.pop())
                savefile = open("player_notes", 'w', encoding="utf-8")
                savefile.write(str(len(player_notes)))
                savefile.close()
                screen.append("<A new clue has been added to your notebook!>")
                display_screen()
                continue
            elif special_tag_type == 2:
                if choice_index != 0:
                    current_line_num += 1
                    continue
                current_line_num += 1
                print_notes(player_notes)
                input("\n%s\nPress ENTER key to exit notebook...\n%s\n"%('-' * 105, '-' * 105))
                current_line_num = choice_start_line_num
                continue
            elif special_tag_type == 3:
                final_choice = True if choice_index == 1 else False
                current_line_num += 1
                continue
        
        if is_tag:
            if debugging:
                print("is tag %d"%(tag_type))
                input()
            if tag_type == 10:
                current_scene_num += 1
                current_scene = current_line.title()
                print_title(current_scene)
                sleep(per_line_delay)
                if current_line != "End sequence":
                    savefile = open("save", 'w', encoding="utf-8")
                    savefile.write("%d,%d"%(current_line_num - 1, current_scene_num))
                    savefile.close()
                current_hp = full_hp
                print("Scene %d | Player HP restored: %s\nPress ENTER to continue..."%(current_scene_num, '◉ ' * current_hp))
                input()
                current_line_num += 1
                print("over")
                continue
            elif tag_type == 11:
                display_sliding(current_line)
                sleep(per_line_delay)
                current_line_num += 1
                continue
            elif tag_type == 12:
                choice_start_line_num = current_line_num - 1
                first_line = current_line.split(',')
                choice_num = len(first_line)
                current_line_num += 1
                second_line = content[current_line_num].split(',')
                choices = {first_line[i]:second_line[i] for i in range(choice_num)}
                current_line_num += 2
                screen.append('')
                screen += limit_line_length(content[current_line_num].split(' '))
                display_screen()
                current_line_num += 1
                sleep(per_line_delay)
                for choice in choices:
                    screen.append("Type \"%s\" -> %s"%(choice, choices[choice]))
                display_screen()
                while True:
                    user_input = input("> ")
                    choice = Parse_Input(user_input, first_line)
                    if choice == -1:
                        clear_screen()
                        display_screen()
                        print("A voice in your head just said \"%s\"\nWhat's that? You wondered..."%(user_input))
                        continue
                    else:
                        choice_index = choice
                        screen.append("> " + first_line[choice_index])
                        screen.append('')
                        if debugging:
                            print(choice)
                            input()
                        #print("line num: %d\n%s"%(current_line_num, content[current_line_num]))
                        #input()
                        break
            elif -1 < tag_type < 10:
                if tag_type != choice_index:
                    while content[current_line_num] not in script_tags_end:
                        current_line_num += 1
                    continue
                else:
                    screen += limit_line_length(current_line.split(' '))
                    display_screen()
                    if current_line != '' and "|" not in current_line and "_" not in current_line and ":" not in current_line:
                        input()
                    sleep(per_line_delay)
                    current_line_num += 1
                    continue
            elif 19 < tag_type < 23:
                tag_type -= 20
                if tag_type != loop_choice_index:
                    while content[current_line_num] not in script_tags_end:
                        current_line_num += 1
                    continue
                else:
                    while content[current_line_num + 1] not in script_tags_end:
                        screen += limit_line_length(content[current_line_num].split(' '))
                        display_screen()
                        sleep(per_line_delay)
                        current_line_num += 1
                    loop_choice[loop_choice_index] = True
                    if loop_choice == [True, True, True]:
                        loop_choice = [False, False, False]
                        current_line_num += 1
                    else:
                        current_line_num = loop_start_line_num
                    continue
            elif tag_type == 13:
                loop_info = [int(i) for i in current_line.split(',')]
                if choice_index != loop_info[0]:
                    current_line_num = loop_info[1] - 2
                    continue
                else:
                    current_line_num += 1
                    continue
            elif tag_type == 14:
                input("\n%s\nPress ENTER key to continue to the next chapter...\n%s\n"%('-' * 105, '-' * 105))
                current_line_num += 1
                screen = []
                continue
            elif tag_type == 15:
                loop_start_line_num = current_line_num - 1
                second_line = content[current_line_num].split(',')
                choices = [second_line[i] for i in range(3)]
                current_line_num += 2
                screen.append('')
                screen += limit_line_length(content[current_line_num].split(' '))
                display_screen()
                current_line_num += 1
                sleep(per_line_delay)
                for i in range(3):
                    if loop_choice[i] == True:
                        continue
                    screen.append("Type %d -> %s"%(i, choices[i]))
                display_screen()
                while True:
                    user_input = input("> ")
                    choice = Parse_Input(user_input, ['0', '1', '2'])
                    if choice == -1:
                        clear_screen()
                        display_screen()
                        print("A voice in your head just said \"%s\"\nWhat's that? You wondered..."%(user_input))
                        continue
                    else:
                        loop_choice_index = choice
                        screen.append("> %d"%(choice))
                        screen.append('')
                        #print("line num: %d\n%s"%(current_line_num, content[current_line_num]))
                        #input()
                        break
            elif tag_type == 16:
                old_text, new_text = current_line.split('/')
                old_pos = screen.index(old_text)
                screen[old_pos] = new_text
                display_screen()
                current_line_num += 1
                continue

        else:
            thisline = limit_line_length(current_line.split(' '))
            screen += thisline
            display_screen()
            print()
            if thisline != [''] and "|" not in current_line and "_" not in current_line and ":" not in current_line:
                input()
            sleep(per_line_delay)
            current_line_num += 1
            continue

content = load_from_text()#[:925]
parse_script(content, 0, start_line=1384-2, debugging=False)
# start_line is starting from which line in the script, remember to calibrate using -2