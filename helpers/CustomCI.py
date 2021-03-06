from termcolor import colored, cprint

def CustomInput(textToInput, color = 'green', attr=[]) : 
    return input(colored(textToInput, color, attrs=attr))

def CustomPrint(textToPrint, color = 'green', attr=[]) : 
    cprint(textToPrint, color, attrs=attr)
