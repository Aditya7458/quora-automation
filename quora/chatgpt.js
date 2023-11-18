// copying answer om consloe getting by data_by_chatgpt

async function copyStringToClipboard(str) {
  try {
    await navigator.clipboard.writeText(str);
    console.log("Successfully copied string");
  } catch (err) {
    console.error("Failed to copy string using Clipboard API: ", err);
    try {
      const tempInput = document.createElement("textarea");
      tempInput.value = str;
      document.body.appendChild(tempInput);
      tempInput.select();
      document.execCommand("copy");
      document.body.removeChild(tempInput);
      console.log("Successfully copied string using execCommand");
    } catch (err) {
      console.error("Failed to copy string using execCommand: ", err);
    }
  }
}

async function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function main() {
  let looper = true;
  while (looper == true) {
    console.log("Start");
    let data = document.getElementsByClassName("markdown")[0].innerHTML;
    const myString = data;
    let regeneratebtn = document.getElementsByClassName(
      "flex ml-auto gap-1 items-center rounded-md p-1 text-xs gizmo:gap-1.5 gizmo:pl-0 dark:text-gray-400 dark:hover:text-gray-200 disabled:dark:hover:text-gray-400 hover:text-gray-950 md:invisible md:group-hover:visible md:group-[.final-completion]:visible"
    )[0];
    // let continuebtn = document.getElementsByClassName('btn-neutral')[1];
    if (regeneratebtn) {
      console.log("content generated");
      await copyStringToClipboard(myString);
      await sleep(2000);
      looper = false;
    }
    await sleep(2000); // Sleep for 2 seconds
    console.log("End");
  }
}

main();
