from termcolor import cprint

def terminal_info(text: str):
    return cprint(f"{text}", 'blue')

def terminal_warning(text: str):
    return cprint(f"{text}", 'red')