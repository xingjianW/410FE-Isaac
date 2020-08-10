function find() {
    var input = document.getElementById("input");
    var inputID="#"+input.value;
    var parent = document.getElementById(input.value).parentElement.parentElement.parentElement;
    document.querySelector(inputID).scrollIntoView();
    parent.style.backgroundColor="lightgreen";
}