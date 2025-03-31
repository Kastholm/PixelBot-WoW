import datetime

# using now() to get current time
current_time = datetime.datetime.now()
timestamp = f'{current_time.hour}:{current_time.minute}:{current_time.second}'

def write_to_log(text):
    with open("utils\log\\log.txt", "a", encoding="utf-8") as file:
        file.write(f'{timestamp} - {text} \n')


def welcome_msg():
    with open("utils\log\\log.txt", "w", encoding="utf-8") as file:
        file.write(r"""                                                                      
 ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ 
|______|______|______|______|______|______|______|______|______|______|______|______|______|
 _     _  _     _  _       _    _      _                                _  _     _  _     _ 
| |  _| || |_ _| || |_    | |  | |    | |                             _| || |_ _| || |_  | |
| | |_  __  _|_  __  _|   | |  | | ___| | ___ ___  _ __ ___   ___    |_  __  _|_  __  _| | |
| |  _| || |_ _| || |_    | |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \    _| || |_ _| || |_  | |
| | |_  __  _|_  __  _|   \  /\  /  __/ | (_| (_) | | | | | |  __/   |_  __  _|_  __  _| | |
| |   |_||_|   |_||_|      \/  \/ \___|_|\___\___/|_| |_| |_|\___|     |_||_|   |_||_|   | |
| |                                                                                      | |
| |                                   1. Start PixelBot                                  | |
| |                                   2. Choose Route                                    | |
|_|                                   3. Start GameBot                                   |_|
 ______ ______ ______ ______ ______ ______ ______ ______ ______ _____ ______ ______ ______ 
|______|______|______|______|______|______|______|______|______|______|______|______|______|
""")   