from termcolor import cprint
from pyfiglet import figlet_format as asci

def run_function():
    inpu = input("> ")
    print(inpu)
    return inpu, inpu + "hello"

a, b = run_function()

print(a, b)