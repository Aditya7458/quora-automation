// Clicked on answer button
setTimeout(() => {
ansbtn = document.getElementsByClassName(
  "q-click-wrapper qu-active--textDecoration--none qu-focus--textDecoration--none qu-borderRadius--pill qu-alignItems--center qu-justifyContent--center qu-whiteSpace--nowrap qu-userSelect--none qu-display--inline-flex qu-tapHighlight--white qu-textAlign--center qu-cursor--pointer qu-hover--textDecoration--none qu-hover--bg--darken ClickWrapper___StyledClickWrapperBox-zoqi4f-0  base___StyledClickWrapper-lx6eke-1"
)[3];
ansbtn.click();  
}, 1000);


// waiting for add content to the answer
setTimeout(() => {
// Add answer to the element (Content) 
  document.getElementsByClassName(
    "content"
  )[0].innerText = `Hello world! `;
  // www.techbhopali.com/2023/09/how-to-get-your-first-project-on-upwork.html
  
  // waiting to click post button
    setTimeout(() => {
        let postbtn = document.getElementsByClassName(
          "q-click-wrapper qu-active--textDecoration--none qu-focus--textDecoration--none qu-borderRadius--pill qu-alignItems--center qu-justifyContent--center qu-whiteSpace--nowrap qu-userSelect--none qu-display--inline-flex qu-bg--blue qu-tapHighlight--white qu-textAlign--center qu-cursor--pointer qu-hover--textDecoration--none ClickWrapper___StyledClickWrapperBox-zoqi4f-0 base___StyledClickWrapper-lx6eke-1 puppeteer_test_modal_submit "
        )[0];
        postbtn.click();
        
    }, 2000);
}, 4000);
