from datetime import datetime

RED = "\033[31m"    
GREEN = "\033[32m"   
YELLOW = "\033[33m" 
BLUE = "\033[34m"    
MAGENTA = "\033[35m" 
CYAN = "\033[36m"    
WHITE = "\033[37m"   
RESET = "\033[0m"    

def time():
    return f'{YELLOW}[{datetime.now().strftime("%H:%M:%S")}]{RESET}'

def cstr(str,color="white"):
    colors = {
        "RED": RED,
        "GREEN": GREEN,
        "YELLOW": YELLOW,
        "BLUE": BLUE,
        "MAGENTA": MAGENTA,
        "CYAN": CYAN,
        "WHITE": WHITE
    }

    # Get the code for the requested color, default to WHITE if not found
    color_code = colors.get(color.upper(), WHITE)

    return f'{color_code}{str}{RESET}'