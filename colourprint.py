#Preset colour codes
ORANGE = '38;5;208'
BLUE = '34'
YELLOW = '33'
GREEN = '32'
RED = '31'

#Colour printing function
def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m") #Command used to print in colours