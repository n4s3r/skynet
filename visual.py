from colorama import Fore, init, Style
from os import system, get_terminal_size
init()


def rainbow(color_ratio, string):
    for color, character in zip(range(color_ratio[0], color_ratio[1]), string):
        print(f"\x1b[38;5;{color}m{character}\x1b[0m", end='')
    return ''


def rainbow2(color_ratio, character, letter_color, _type, number=5, increment=1):
    # Reminder: sum 1 to the number
    if number >= 5:
        for color in range(color_ratio[0], color_ratio[1], increment):
            print(f"\x1b[{_type};5;{color};{letter_color}m{character}\x1b[0m", end='')
        rainbow2((color_ratio[1], color_ratio[0]), character, letter_color, _type,
                 number-(max(color_ratio)-min(color_ratio))//abs(increment), increment*-1)
    else:
        for color in range(color_ratio[0], color_ratio[1]-number*increment, increment):
            print(f"\x1b[{_type};5;{color};{letter_color}m{character}\x1b[0m", end='')
    return ''


class F0re:
    def BLINK(string):
        system(f"echo -n '\e[5m{string}\e[25m'")
        return ''

    def Reset_BLINK():
        system("echo -n '\e[25m'")
        return ''

    def UNDERLINED(string=""):
        system(f"echo -n '\e[4m{string}'")
        return ''

    def Reset_UNDERLINED():
        system("echo -n '\e[24m'")
        return ''

    def Reset_all():
        system("echo -n '\e[0m'")
        return ''


def skynet():
    print(Style.BRIGHT, end='')
    rainbow2((16, 21), "#", "32", "48", get_terminal_size()[0]-5)
    print(f'''
{Fore.YELLOW}             ┏━┛┃ ┃┃ ┃┏━ ┏━┛━┏┛      {Fore.RESET}               ``...........-...``                    
{Fore.YELLOW}             ━━┃┏┛ ━┏┛┃ ┃┏━┛ ┃     {Fore.RESET}           ```-::-/-........-:://++/.``                
{Fore.YELLOW}             ━━┛┛ ┛ ┛ ┛ ┛━━┛ ┛     {Fore.RESET}          `-/y/:::--..``.`.-:////+syd/.`{''}                  
             ..:^^^~~^^^:..                 --yyo::-.......`://:/++yyhs/--`              
         .:^!7?JJJJYYJJJJ?7!^:.             `:+sds/:-........-:::/osyyso/:-.              
       :~7?JYY55555Y555555YYJ?7~:           .:/ohs:--........-:::/oyyss+::..              
     :!?JYY55PPPPPP{Fore.RED}!{Fore.RESET}7GPPPPP55YYJ?!:         .--oso:---.......--::/oo+++:--..              
   .~?JY55PPGGGGGGJ{Fore.RED}^~{Fore.RESET}YBGGGGGPP55YJ?~.       `../ys:---.........-::+::++/:...              
  :!JYY5PPP5JJJJJJ{Fore.RED}~~~~{Fore.RESET}JJJJJYPGPP5YYJ!:      `--/dh-..-.```........-::+s++...              
 :~JYY5PPGGGPJ{Fore.RED}!~^^~~~~^^~{Fore.RESET}7YPGGGPP5YYJ~:     /--//....```..........-/+/:-.:`              
.^?JY5PPGGGGGBGP{Fore.RED}!~~~~~~{Fore.RESET}7GGBGGGGGPP5JJ?^.    /::` :.:{Fore.RED}-```{Fore.RESET}````````{Fore.RED}.::-.{Fore.RESET}` --:`              
:~JJ~75GGGGGGGBY{Fore.RED}~^~77~^~{Fore.RESET}PBGGGGGGPY!^JJ~:    .os:```.{Fore.RED}`  `{Fore.RESET}.-:-:..''', end='')
    F0re.BLINK(F"{Fore.RED}``...``")
    print(f'''{Fore.RESET}/+::              
:!JY7~~!JPGBGGP{Fore.RED}!7{Fore.RESET}YPGGPY{Fore.RED}7!{Fore.RESET}GGBBG5?~::7YJ!:     `//--.````..:s/:/:-:.....-:--.              
:~JY5Y7~^~!JPGPPBBGGGGBBPGG5?~:::!Y5YJ~:     --...````..::-.:.---...--.-.`              
.^?JY5P5J7~^^!JPPYGGGGYPP?^:::~J5P5YJ?^.     `-...```.:/`` `.::--`.:...                
 :~JYY5PGGPJ??~~~?PGGP!:::77?PGGP5YYJ~:      -. `...:--.` `--:--.. `.`                
  :!JYY5PPGGGP?J7~~7!^:!?7PGGGPP5YYJ!:       ..` ..:yo:-..:+o+/...``.`                
   .~?JY55PPPPGGJ\x1b[37m^^^^^~Y\x1b[39mGGPPPP55YJ?~.         `--. `-:--....-.----.``..                  
     :!?JYY55J\x1b[37m!^:^!JJ7\x1b[37m~^~?\x1b[39mY55YYJ?!:           ...:-`.--......-.---..--.                  
       :~7?JYJ\x1b[37m!^?\x1b[39m55PP5Y?!7YYJ?7~:             ...``/-..`````..--....-.`.`                
         .:^!7??JJJJJJJJ??7!^:.               `..``   ..` ``.```..``..````.`                
             ..:^^^~~^^^:..                   ````````.```  ` ` ``.-:..`.---`` ``` `...` `          
                              .......```````     `` ``  `.....-`  `````  `.....```````''')
    rainbow2((16, 46), "#", "40", "38", get_terminal_size()[0]-5, 6)
    print(Style.RESET_ALL)
    print(f"{Fore.GREEN}By {Fore.RED+Style.BRIGHT}polblanco@insestatut.cat{Style.RESET_ALL}{Fore.LIGHTCYAN_EX} v0.1")
