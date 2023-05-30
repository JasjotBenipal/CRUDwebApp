const body = document.querySelector("body");
const sidebar = body.querySelector(".sidebar");
const toggle = body.querySelector(".toggle");
const mode = body.querySelector(".mode");
const modeText = body.querySelector(".mode-text");


if (localStorage.getItem("dark") == null){
  localStorage.setItem("dark", 0);
}

if (localStorage.getItem("dark") != null){
  if (localStorage.getItem("dark") == 1){
    body.classList.toggle("dark");
        
        if(body.classList.contains("dark")){
          modeText.innerText = "Light Mode";
          localStorage.setItem("dark", 1);
        } else {
          modeText.innerText = "Dark Mode";
          localStorage.setItem("dark", 0);
        }
  }
}

if (mode != null){
    mode.addEventListener("click", () =>{
        body.classList.toggle("dark");
        
        if(body.classList.contains("dark")){
          modeText.innerText = "Light Mode";
          localStorage.setItem("dark", 1);
        } else {
          modeText.innerText = "Dark Mode";
          localStorage.setItem("dark", 0);
        }
    });
}

if (toggle != null){
    toggle.addEventListener("click", () =>{
        if (sidebar != null){
            sidebar.classList.toggle("close");
        }
    });
}