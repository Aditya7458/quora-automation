import time
import pyperclip
import pyautogui
import platform
import subprocess


def postAnswer(answer,url):
    system = platform.system()
    if system == "Windows":
        subprocess.Popen(f"start chrome {url}", shell=True)

    elif system == "Darwin":  # macOS
        subprocess.Popen(f'open -a "Google Chrome" {url}', shell=True)
    elif system == "Linux":
        subprocess.Popen(f"google-chrome {url}", shell=True)
    else:
        print(f"Unsupported operating system: {system}")

    

    #wait for website to open
    time.sleep(5)

    #Open console
    pyautogui.hotkey('ctrl','shift','j')

    # Waiting time to load console
    time.sleep(2)

    # replace hello world from actual answer
    postcode=open('postans.js').read().replace('Hello world!',f"{answer}")
    # cpoying postcode from postans.js
    pyperclip.copy(postcode)
    time.sleep(2)
    # executing postcode
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    # waiting time to post an answer
    time.sleep(10)
    pyautogui.hotkey('alt','f4')

if __name__=="__main__":
    ans=open('response.txt').read()
    code=open('writeans.js').read()
    postAnswer(ans,'https://www.quora.com/How-can-I-earn-200-dollars-online',code)