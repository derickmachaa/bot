def color_red(string):
    """Recieves a string and prints it in color red"""
    return("\033[31m{}\033[0m").format(string)

def color_blue(string):
    """Recieves a string and returns the string in color blue"""
    return("\033[34m{}\033[0m").format(string)

def color_cyan(string):
    """Recieves a string and returns the string in color cyan"""
    return("\033[36m{}\033[0m").format(string)

def print_info(*args):
    """Prints error messages"""
    print("\033[36m[*]\033[0m",*args)
    
def print_error(*args):
    """Prints error messages"""
    print("\033[31m[-]\033[0m",*args)
    
def print_success(*args):
    """Prints success messages"""
    print("\033[33m[+]\033[0m",*args)