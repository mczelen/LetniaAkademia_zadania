function createBtn(div) {
    let btn = document.createElement("button");
    btn.innerHTML = '<i class="fa fa-trash-o"></i>';
    btn.type = "button";
    btn.classList.add("btn", "btn-outline-danger", "btn-lg");
    btn.onclick = function () {
        div.classList.add("disappeared");
        alert("usunięto dane");
      };
    return btn;
  }


let dataContainer = document.querySelector("#data-container")

for(let n = 0; n<3*4; n++){
    let div = document.createElement("div");
    div.innerHTML = "<p>Dane " + (n+1) + "</p>";
    div.appendChild(createBtn(div));
    div.classList.add("tile");
    dataContainer.appendChild(div);
}