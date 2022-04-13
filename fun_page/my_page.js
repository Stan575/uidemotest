function addImage() {
    const personalityDiv = document.querySelector("#personality");
    const personalityImage = document.createElement("img");
    personalityImage.id = "picture";
    personalityImage.src = "personality_type.png";
    personalityImage.alt = "image";
    personalityImage.width = "500";
    personalityImage.onclick = function() { closeImage(); };
    personalityDiv.appendChild(personalityImage);
}

function closeImage() {
    const image = document.querySelector("#picture");
    image.remove();
}

function printToConsole() {
    var login = document.querySelector("input[name=login]");
    var password = document.querySelector("input[name=password]");
    console.log("login: " + login.value);
    console.log("password: " + password.value);
    login.value = '';
    password.value = '';
}

function changeColor(newColor) {
    const colorDiv = document.querySelector("body");
    colorDiv.style.backgroundColor = newColor;
}

function openSelection() {
    var url;
    var selection = document.querySelector("select[name=lang]");
    if (selection.value == 1) {
        url = "https://www.python.org";
    } else if (selection.value == 2) {
        url = "https://www.javascript.com/";
    } else if (selection.value == 3) {
        url = "https://www.java.com/en/";
    } else if (selection.value == 4) {
        url = "https://en.wikipedia.org/wiki/SQL";
    } else {
        return null;
    }
    window.open(url, "_blank").focus();
}