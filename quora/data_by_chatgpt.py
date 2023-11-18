# generate data from chatgpt
import subprocess
import platform
import time
import pyautogui
import pyperclip
import sys
from bs4 import BeautifulSoup



def open_website_with_console(url, code_to_execute, question):
    system = platform.system()

    if system == "Windows":
        subprocess.Popen(f"start chrome {url}", shell=True)

    elif system == "Darwin":  # macOS
        subprocess.Popen(f'open -a "Google Chrome" {url}', shell=True)
    elif system == "Linux":
        subprocess.Popen(f"google-chrome {url}", shell=True)
    else:
        print(f"Unsupported operating system: {system}")

    # Copy the code to clipboard
    pyperclip.copy(code_to_execute)

    # wait for the website to load
    time.sleep(7)

    # writing message
    pyautogui.typewrite(question)
    pyautogui.press("enter")

    time.sleep(3)

    # Simulate keyboard shortcut to open developer console
    # pyautogui.hotkey('command', 'option', 'j')  # macOS
    pyautogui.hotkey("ctrl", "shift", "j")  # Windows and Linux

    # Wait for the console to open
    time.sleep(2)

    # wait for chatgpt to generate

    time.sleep(10)
    pyautogui.click(300, 600)
    pyautogui.hotkey("ctrl", "l")

    # Simulate keyboard shortcut to paste the code in the console
    # pyautogui.hotkey('command', 'v')  # macOS
    pyautogui.hotkey("ctrl", "v")  # Windows and Linux

    # Simulate pressing Enter to execute the code
    pyautogui.press("enter")

    chatgptfile = open("chatgpt.js", "r")
    file_content = chatgptfile.read()

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
    chatgptfile.close()

    html = f"""{pyperclip.paste()}"""
    soup = BeautifulSoup(html, "html.parser")

    def unwanted_text_remover():
        # Find all <em> tags and their parent tags, then remove them
        em_tags = soup.find_all("em")
        for tag in em_tags:
            if tag:
                tag.parent.decompose()
        
        
    unwanted_text_remover()
    paragraphs=soup.find_all('p')
    answer=''
    for para in paragraphs:
        answer+=f' {para.get_text()}'

    with open('response.txt','w',encoding='cp1252') as fs:
        # Remove emojis and their decoded characters
        cleaned_answer = ''.join([c for c in answer if c.isascii()])
        fs.write(cleaned_answer)

    


if __name__ == "__main__":
    web_link = "https://chat.openai.com/?AIPRM_PromptID=1784224785543462912"
    code = open("chatgpt.js", "r").read()
    open_website_with_console(web_link, code, "can dogs eat mango?")
