import pyfiglet

def print_banner(text):
    if text != None:
        return print(pyfiglet.figlet_format(text, font="digit", justify='right'))
print_banner(input('escribe algo:    '))







