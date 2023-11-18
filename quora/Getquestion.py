import subprocess
import platform
import sys
import time
import pyautogui
import pyperclip
def getQuestion():
    code_to_execute=open('getQuestion.js').read()
    url="""https://www.quora.com/search?q=food&type=question"""
    # https://www.quora.com/search?q=spritual%20water&type=question
    system = platform.system()

    if system == "Windows":
        subprocess.Popen(f'start chrome "{url}"', shell=True)

    elif system == "Darwin":  # macOS
        subprocess.Popen(f'open -a "Google Chrome" {url}', shell=True)
    elif system == "Linux":
        subprocess.Popen(f"google-chrome {url}", shell=True)
    else:
        print(f"Unsupported operating system: {system}")
    # Copy the code to clipboard
    pyperclip.copy(code_to_execute)
    # Wait for the browser to open

    time.sleep(7)


    # Simulate keyboard shortcut to open developer console
    # pyautogui.hotkey('command', 'option', 'j')  # macOS
    pyautogui.hotkey("ctrl", "shift", "j")  # Windows and Linux

    # Wait for the console to open
    time.sleep(2)

    # Simulate keyboard shortcut to paste the code in the console
    # pyautogui.hotkey('command', 'v')  # macOS
    pyautogui.hotkey("ctrl", "v")  # Windows and Linux

    # Simulate pressing Enter to execute the code
    pyautogui.press("enter")

    getQuestion = open("getQuestion.js", "r")
    file_content = getQuestion.read()

    def copying_data():
        duration = 0
        while True:
            if duration < 4 * 60:
                clipboard_content = pyperclip.paste()
                if duration % 10 == 0:
                    pyautogui.hotkey("ctrl", "l")
                    pyautogui.hotkey("ctrl", "v")  # Windows and Linux
                    pyautogui.press("enter")
                    print("Repasted to console")
                    duration += 2
                elif clipboard_content == file_content:
                    print("content not copyed")
                    time.sleep(2)
                    duration += 2

                else:
                    print(pyperclip.paste())
                    break
            else:
                print("exiting the programme, failed to get content")
                sys.exit()

    copying_data()

    list = eval(pyperclip.paste())

    return list
if __name__=="__main__":
    getQuestion()