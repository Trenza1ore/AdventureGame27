from Normalise import Parse_Input
from Notebook import limit_line_length
from Beautiful_Font import clear_screen
from time import sleep
from Beautiful_Font import *

script_tags = [
    "<title>",
    "<slide>",
    "<choice>",
    "<go back>"
]
script_tags = ["<%d>"%(i) for i in range(10)] + script_tags
script_tags_end = ["</" + tag[1:] for tag in script_tags]
screen = []
screen_row_length = 105
current_scene = "placeholder scene"
current_scene_num = -1

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

def parse_script(content: list, per_line_delay: float=0.5, debugging: bool=False) -> None:
    global current_scene, screen, current_scene_num
    clear_screen()
    current_line_num = 0
    script_length = len(content)
    is_tag = False
    tag_type = 100 # just a random initial value
    choice_num = 1 # number of choices when making a decision
    choice_index = -1 # which path did the player chose
    while current_line_num < script_length:
        #print("line", current_line_num)
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
        if is_tag:
            if tag_type == 10:
                current_scene_num += 1
                current_scene = current_line.title()
                print_title(current_scene)
                sleep(per_line_delay)
                print("Scene %d\nPress ENTER to continue..."%(current_scene_num))
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
                    screen.append("Type \"%s\" to %s"%(choice, choices[choice]))
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
                        #print("line num: %d\n%s"%(current_line_num, content[current_line_num]))
                        #input()
                        break
            elif -1 < tag_type < 10:
                if tag_type != choice_index:
                    current_line_num += 1
                    continue
                else:
                    screen += limit_line_length(current_line.split(' '))
                    display_screen()
                    sleep(per_line_delay)
                    current_line_num += 1
                    continue
            elif tag_type == 13:
                loop_info = [int(i) for i in current_line.split(',')]
                if choice_index != loop_info[0]:
                    current_line_num = loop_info[1] - 2
                    continue
                else:
                    current_line_num += 1
                    continue

        else:
            screen += limit_line_length(current_line.split(' '))
            display_screen()
            sleep(per_line_delay)
            current_line_num += 1
            continue






content = load_from_text()[:46]
parse_script(content)