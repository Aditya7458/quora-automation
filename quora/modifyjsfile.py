import re
# remove ASCAI charecter from answer generaterd by removing emojies.

def modifyjsfile(answer):
    updated_ans = re.sub(r'\[.*?\]', '', answer)

    with open('response.txt', "w") as fs:
        fs.write(updated_ans)
    


    print("JavaScript file updated successfully.")
