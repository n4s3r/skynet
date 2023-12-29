#from functions import F0re, rainbow, rainbow2
import functions
#from os import system
#import multiprocessing as mp
import threading
from time import sleep
from visual import *
from colorama import Fore, init, Style, Back
try:
    from pynput import keyboard as kb
except:
    print()
    print("Error starting keyboard module, please reboot the machine.")
    exit()
init()


class Menu:
    def __init__(self, name, supermenu, options, route):
        self.name = name
        self.supermenu = supermenu
        self.options = options
        self.route = route


class Option:
    def __init__(self, name, used, route):
        self.name = name
        self.used = used
        self.route = route


options = []


def print_menu(_menu):
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + F0re.UNDERLINED() + _menu.name + Style.RESET_ALL)

    for _option in _menu.options.values():
        if type(_option[0]) is Menu:
            print(f"\t{Fore.LIGHTMAGENTA_EX}{_option[1]}-{_option[0].name}\t"
            f"{Style.RESET_ALL}")
        else:
            print(f"\t{Fore.GREEN if _option[0].used else Fore.RED}"
                  f"{_option[1]}-{_option[0].name}\t{Style.RESET_ALL}")


teclas = ''


def pulsa(tecla):
    global teclas
    teclas += str(tecla)[1] if len(str(tecla)) == 3 else str(tecla)


def go_to(_option, sound, parameter=''):
    global actual_menu, teclas, signal
    # TODO: sleep better
    while all(functions.all_process[1]) != False:
        pass
    functions.signal = None
    if _option.isnumeric():
        for opt in actual_menu.options.values():
            if opt[1] == int(_option):
                if type(actual_menu.options[opt[0].name][0]) is Menu:
                    if sound:
                        functions.mixer.music.load('.enter.wav')
                        functions.mixer.music.play()
                    actual_menu = actual_menu.options[opt[0].name][0]
                else:
                    if sound:
                        # Buscar sonido
                        functions.mixer.music.load('.enter.wav')
                        functions.mixer.music.play()
                    s = threading.Thread(target=eval(f"{actual_menu.options[opt[0].name][0].route}"), args=(parameter,))
                    s.daemon = True
                    s.start()
                    teclas = ''
                    with kb.Listener(pulsa):
                        while 'stopKey.enter' not in teclas and s.is_alive():
                            pass
                    if s.is_alive():
                        functions.signal = 'stop'
                    teclas = ''
                    actual_menu.options[opt[0].name][0].used = True
    elif _option == 'back' or _option == "-1":
        if sound:
            functions.mixer.music.load('.exit.wav')
            functions.mixer.music.play()
        actual_menu = actual_menu.supermenu
    elif _option.lower() == 'ip':
        if sound:
            # buscar nuevo sonido
            functions.mixer.music.load('.enter.wav')
            functions.mixer.music.play()
        functions.Change_IPversion()
    elif 'functions' in _option:
        if sound:
            functions.mixer.music.load('.enter.wav')
            functions.mixer.music.play()
        s = threading.Thread(target=eval(_option), args=(parameter,))
        s.daemon = True
        s.start()
        teclas = ''
        with kb.Listener(pulsa):
            while 'stopKey.enter' not in teclas and s.is_alive():
                pass
        if s.is_alive():
            print('Stopping...')
            functions.signal = 'stop'
        teclas = ''

        def check_option(_option, menu = global_menu):
            for option in menu.options:
                if menu.options[option][0].route + '()' == _option:
                    menu.options[option][0].used = True
                    return
                elif type(menu.options[option][0]) is Menu:
                    check_option(_option, menu.options[option][0])

        check_option(_option)
    else:
        try:
            if type(actual_menu.options[_option][0]) is Menu:
                actual_menu = actual_menu.options[_option][0]
            else:
                s = threading.Thread(target=eval(f"{actual_menu.options[_option][0].route}"), args=(parameter,))
                s.daemon = True
                s.start()
                teclas = ''
                with kb.Listener(pulsa):
                    while 'stopKey.enter' not in teclas and s.is_alive():
                        pass
                if s.is_alive():
                    print('Stopping...')
                    signal = 'stop'
                teclas = ''
                # exec(f"{actual_menu.options[_option][0].route}()")
                actual_menu.options[_option][0].used = True
        except KeyError:
            input(f"{Fore.RED}You can't call a function that not exists.")

global_menu = Menu("Main menu", None, {}, "functions")
global_menu.supermenu = global_menu
actual_menu = global_menu

ismenu = False


def check(route):
    global ismenu
    for obj in route:
        if obj[0].isupper():
            ismenu = True
            return
    ismenu = False


def gen_tree(_menu, options):
    global ismenu
    for _option, num in zip(options, range(len(options))):
        if _option[0].isupper():
            if type(_menu) is Menu:
                exec(F'''check(dir({_menu.route + f".{_option}"}))''')
                if ismenu:
                    _menu.options[_option] = (Menu(_option, _menu, {}, f"{_menu.route}.{_option}"), num)
                    exec(f"gen_tree(_menu.options[_option][0], dir"
                         f"({_menu.options[_option][0].route}))")
                else:
                    _menu.options[_option] = (Option(_option, False, f"{_menu.route}.{_option}"), num)


gen_tree(global_menu, dir(functions))


def main_menu(args):
    functions.init_skynet(args.no_get_ip, args.sound, args.sniff_output)
    if args.ipv6:
        functions.Change_IPversion(True)
    while True:
        system('clear')
        if not args.no_draw:
            skynet()
        print_menu(actual_menu)
        print(Fore.LIGHTYELLOW_EX + Back.BLACK, end='')
        F0re.BLINK(f'\e[93mLaunch action[/{actual_menu.route.replace(".", "/")}/]>>>')
        print(Fore.GREEN + Back.RESET, end='')
        for op in dir(args):
            if '__' not in op and eval(f'args.{op}') not in [False, None]:
                parameter = eval(f'args.{op}')
                parameter = str(parameter)
                if op == 'leave_a_message':
                    exec(f'args.{op} = False')
                    go_to(f'functions.Miscelanelous.{op.capitalize()}', args.sound, parameter)
                elif op == 'delete_leases_attack':
                    exec(f'args.{op} = False')
                    go_to(f'functions.Attacks.{op.capitalize()}', args.sound, parameter)
                elif 'attack' in op:
                    exec(f'args.{op} = False')
                    go_to(f'functions.Attacks.{op.capitalize()}', args.sound, parameter)
                elif 'pool' in op:
                    exec(f'args.{op} = False')
                    go_to(f'functions.Post_attack.DHCP.{op.capitalize()}', args.sound, parameter)
                elif 'queries' in op or 'zone' in op:
                    go_to(f'functions.Post_attack.DNS.{op.capitalize()}', args.sound, parameter)
                    exec(f'args.{op} = False')
                elif 'web' in op:
                    exec(f'args.{op} = False')
                    go_to(f'functions.Post_attack.HTTP.{op.capitalize()}', args.sound, parameter)
        _option = input()
        F0re.Reset_all()
        go_to(_option, args.sound)


def console(args):
    functions.init_skynet(args.no_get_ip, args.sound, args.sniff_output)
    while True:
        try:
            exec(input('>>>'))
        except:
            print('Error')
