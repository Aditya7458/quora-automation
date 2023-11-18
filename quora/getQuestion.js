async function copyStringToClipboard(str) {
    try {
        await navigator.clipboard.writeText(str);
        console.log('Successfully copied string');
    } catch (err) {
        console.error('Failed to copy string using Clipboard API: ', err);
        try {
            const tempInput = document.createElement('textarea');
            tempInput.value = str;
            document.body.appendChild(tempInput);
            tempInput.select();
            document.execCommand('copy');
            document.body.removeChild(tempInput);
            console.log('Successfully copied string using execCommand');
        } catch (err) {
            console.error('Failed to copy string using execCommand: ', err);
        }
    }
}
async function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function main() {
    console.log('Start');
    let queobj = []
    let questionelemlist = document.getElementsByClassName(
      "q-box Link___StyledBox-t2xg9c-0 puppeteer_test_link qu-display--block qu-cursor--pointer qu-hover--textDecoration--underline"
    //   "q-box Link___StyledBox-t2xg9c-0 dFkjrQ puppeteer_test_link qu-display--block qu-cursor--pointer qu-hover--textDecoration--underline"
    );
    for (let index = 0; index < questionelemlist.length; index++) {
        const questionelem = questionelemlist[index];
        if (questionelem) {
            data = [questionelem.innerText, questionelem.href]
            queobj.push(data)
            console.log(data)
            console.log('End');
        }
    }
    mystring = JSON.stringify(queobj) // converted to string

    console.log(mystring)
    await sleep(2000); // Sleep for 2 seconds
    copyStringToClipboard(mystring)
}

main();
