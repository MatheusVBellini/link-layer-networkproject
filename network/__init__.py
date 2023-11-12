from datetime import datetime

def time():
    return'[' + datetime.now().strftime("%H:%M:%S") + ']'