import time
from Getquestion import getQuestion
from data_by_chatgpt import open_website_with_console
from postAnswer import postAnswer
from modifyjsfile import modifyjsfile

questionlist=getQuestion()
questionfile=open('question.txt').readlines()
for questionelem in questionlist:
    time.sleep(2)
    if f'{questionelem[0]}\n' in questionfile:
        print('question already exist')
    else:
        url="https://chat.openai.com/?AIPRM_PromptID=1784520619539562496"
        code_to_execute=open("chatgpt.js").read()

        open_website_with_console(url,code_to_execute,questionelem[0])

        #Modify writeans.js
        preAnswer=open('response.txt').read()
        modifyjsfile(preAnswer)

        time.sleep(2)
        answer=open('response.txt').read()
        # writeans=open('writeans.js').read()
        postAnswer(answer,questionelem[1])
        with open('question.txt','a') as fs:
            fs.write(f'{questionelem[0]}\n')
        time.sleep(3)