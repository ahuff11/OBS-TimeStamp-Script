import keyboard
from datetime import datetime
from obswebsocket import obsws, requests
import atexit
hotkeysave = 'pageup'
hotkeyexit = 'ctrl+*'

file_name = 'timestamps.txt'


ws = obsws('localhost', 4455)
ws.connect()


def cutstring(string):
    start = string.index('outputTimecode')
    end = string.index("'}")
    return string[start-1:end-4]

def save_timestamp():
    response = str(ws.call(requests.GetRecordStatus()))
    with open(file_name, 'a') as file:
        file.write(cutstring(response))
        file.write("\n")
    
def recording_start_date():
    current_date = datetime.now().strftime('%m-%d-%Y')
    with open(file_name, 'a') as file:
        file.write(
            "-------START OF RECORDING------ \n"+
            "----------"+current_date +"-----------\n\n"
            )
        
def exit_handler():
    current_date = datetime.now().strftime('%m-%d-%Y')
    with open(file_name, 'a') as file:
        file.write(
            "\n----------"+current_date+"-----------\n"+
            "-------END OF RECORDING-------- \n\n"
            )


def main():
    recording_start_date()
    keyboard.add_hotkey(hotkeysave, save_timestamp)
    atexit.register(exit_handler)
    keyboard.wait(hotkeyexit)




main()

