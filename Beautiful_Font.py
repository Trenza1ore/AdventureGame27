from os import system
from time import sleep

def clear_screen() -> None:
    system("cls")

# The website I used to generate these fonts:
# http://www.patorjk.com/software/taag/#p=display&f=Big&t=K
title_fonts = {

'A' : '''
           
     /\    
    /  \   
   / /\ \  
  / ____ \ 
 /_/    \_\\
'''.splitlines(),

'B' : '''
  ____  
 |  _ \ 
 | |_) |
 |  _ < 
 | |_) |
 |____/ 
 '''.splitlines(),

'C' : '''
   _____ 
  / ____|
 | |     
 | |     
 | |____ 
  \_____|
 '''.splitlines(),

'D' : '''
  _____  
 |  __ \ 
 | |  | |
 | |  | |
 | |__| |
 |_____/ 
 '''.splitlines(),

'E' : '''
  ______ 
 |  ____|
 | |__   
 |  __|  
 | |____ 
 |______|
'''.splitlines(),

'F' : '''
  ______ 
 |  ____|
 | |__   
 |  __|  
 | |     
 |_|     
'''.splitlines(),

'G' : '''
   _____ 
  / ____|
 | |  __ 
 | | |_ |
 | |__| |
  \_____|
'''.splitlines(),

'H' : '''
  _    _ 
 | |  | |
 | |__| |
 |  __  |
 | |  | |
 |_|  |_|
'''.splitlines(),

'I' : '''
  _____ 
 |_   _|
   | |  
   | |  
  _| |_ 
 |_____|
'''.splitlines(),

'J' : '''
       _ 
      | |
      | |
  _   | |
 | |__| |
  \____/ 
 '''.splitlines(),

'K' : '''
  _  __
 | |/ /
 | ' / 
 |  <  
 | . \ 
 |_|\_\\
 '''.splitlines(),

'L' : '''
  _      
 | |     
 | |     
 | |     
 | |____ 
 |______|
'''.splitlines(),

'M' : '''
  __  __ 
 |  \/  |
 | \  / |
 | |\/| |
 | |  | |
 |_|  |_|
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

'P' : '''
  _____  
 |  __ \ 
 | |__) |
 |  ___/ 
 | |     
 |_|     
 '''.splitlines(),

'Q' : '''
   ____  
  / __ \ 
 | |  | |
 | |  | |
 | |__| |
  \___\_\\
 '''.splitlines(),

'R' : '''
  _____  
 |  __ \ 
 | |__) |
 |  _  / 
 | | \ \ 
 |_|  \_\\
 '''.splitlines(),

'S' : '''
   _____ 
  / ____|
 | (___  
  \___ \ 
  ____) |
 |_____/ 
 '''.splitlines(),

'T' : '''
  _______ 
 |__   __|
    | |   
    | |   
    | |   
    |_|   
'''.splitlines(),

'U' : '''
  _    _ 
 | |  | |
 | |  | |
 | |  | |
 | |__| |
  \____/ 
'''.splitlines(),

'V' : '''
 __      __
 \ \    / /
  \ \  / / 
   \ \/ /  
    \  /   
     \/    
'''.splitlines(),

'W' : '''
 __          __
 \ \        / /
  \ \  /\  / / 
   \ \/  \/ /  
    \  /\  /   
     \/  \/    
'''.splitlines(),

'X' : '''
 __   __
 \ \ / /
  \ V / 
   > <  
  / . \ 
 /_/ \_\\
'''.splitlines(),

'Y' : '''
 __     __
 \ \   / /
  \ \_/ / 
   \   /  
    | |   
    |_|   
'''.splitlines(),

'Z' : '''
  ______
 |___  /
    / / 
   / /  
  / /__ 
 /_____|
'''.splitlines(),

'0' : '''
   ___  
  / _ \ 
 | | | |
 | | | |
 | |_| |
  \___/ 
'''.splitlines(),

'1' : '''
  __ 
 /_ |
  | |
  | |
  | |
  |_|
'''.splitlines(),

'2' : '''
  ___  
 |__ \ 
    ) |
   / / 
  / /_ 
 |____|
'''.splitlines(),

'3' : '''
  ____  
 |___ \ 
   __) |
  |__ < 
  ___) |
 |____/ 
'''.splitlines(),

'4' : '''
  _  _   
 | || |  
 | || |_ 
 |__   _|
    | |  
    |_|  
'''.splitlines(),

'5' : '''
  _____ 
 | ____|
 | |__  
 |___ \ 
  ___) |
 |____/ 
'''.splitlines(),

'6' : '''
    __  
   / /  
  / /_  
 | '_ \ 
 | (_) |
  \___/ 
'''.splitlines(),

'7' : '''
  ______ 
 |____  |
     / / 
    / /  
   / /   
  /_/    
'''.splitlines(),

'8' : '''
   ___  
  / _ \ 
 | (_) |
  > _ < 
 | (_) |
  \___/ 
'''.splitlines(),

'9' : '''
   ___  
  / _ \ 
 | (_) |
  \__, |
    / / 
   /_/  
'''.splitlines(),

'.' : '''
      
      
      
      
  _   
 (_)  
'''.splitlines(),
}

def print_title_line(letters: list, line_num: int) -> None:
    for i in letters:
        print(i[line_num], end=' ')
    print()

def print_title(print_list: str="TITLE", wait_time: float=0.1) -> None:
    print_list = list(print_list.upper())
    current_print_list = []
    #input()
    for i in print_list:
        clear_screen()
        current_print_list.append(title_fonts[i])
        for j in range(7):
            print_title_line(current_print_list, j)
        sleep(wait_time)
    print('-' * 105)