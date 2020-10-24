from os import system
from time import sleep

def clear_screen() -> None:
    system("cls")



# The website I used to generate these fonts:
# http://www.patorjk.com/software/taag/#p=display&f=Big&t=K
title_fonts = {
'T' : '''
  _______ 
 |__   __|
    | |   
    | |   
    | |   
    |_|   
'''.splitlines(),
'I' : '''
  _____ 
 |_   _|
   | |  
   | |  
  _| |_ 
 |_____|
'''.splitlines(),
'L' : '''
  _      
 | |     
 | |     
 | |     
 | |____ 
 |______|
'''.splitlines(),
'E' : '''
  ______ 
 |  ____|
 | |__   
 |  __|  
 | |____ 
 |______|
'''.splitlines(),

'N' : '''
  _   _ 
 | \ | |
 |  \| |
 | . ` |
 | |\  |
 |_| \_|
 '''.splitlines(),

'O' : '''
   ____  
  / __ \ 
 | |  | |
 | |  | |
 | |__| |
  \____/ 
 '''.splitlines(),

'B' : '''
  ____  
 |  _ \ 
 | |_) |
 |  _ < 
 | |_) |
 |____/ 
 '''.splitlines(),

'K' : '''
  _  __
 | |/ /
 | ' / 
 |  <  
 | . \ 
 |_|\_\\
 '''.splitlines()
}

def print_title_line(letters: list, line_num: int) -> None:
    for i in letters:
        print(i[line_num], end=' ')
    print()

def print_title(print_list: str="TITLE", wait_time: float=0.3) -> None:
    print_list = list(print_list.upper())
    current_print_list = []
    #input()
    for i in print_list:
        clear_screen()
        current_print_list.append(title_fonts[i])
        for j in range(7):
            print_title_line(current_print_list, j)
        sleep(wait_time)