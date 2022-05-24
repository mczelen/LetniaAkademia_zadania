// creates button and its onclick method
function createBtn(div) {
    let btn = document.createElement("button");
    // trash bin icon
    btn.innerHTML = '<i class="fa fa-trash-o"></i>';
    btn.type = "button";
    btn.classList.add("btn", "btn-outline-danger", "btn-lg");
    // when button is clicked call this method
    btn.onclick = function () {
        alert("usunięto dane");
        // add "disappeared" class to parent div which makes it invisible
        div.classList.add("disappeared");
    };
    return btn;
  }

// get reference to container for data/tile elements
let dataContainer = document.querySelector("#data-container")

// create 3*4 tiles with data and remove button
for(let n = 0; n<3*4; n++){
    let div = document.createElement("div");
    div.innerHTML = "<p>Dane " + (n+1) + "</p>";
    div.appendChild(createBtn(div));
    div.classList.add("tile");
    dataContainer.appendChild(div);
}