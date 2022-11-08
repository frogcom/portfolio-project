let lightMode = localStorage.getItem("lightMode");

if (lightMode == "true") {
  addLightMode();
}
document.querySelector(".switch").addEventListener("click", function () {
  lightMode = localStorage.getItem("lightMode");
  if (lightMode == "true") {
    removeLightMode();
  } else {
    addLightMode();
  }
});

function addLightMode() {
  lightMode = localStorage.setItem("lightMode", "true");
  document.getElementsByTagName("body")[0].classList.add("lightMode");
}

function removeLightMode() {
  lightMode = localStorage.setItem("lightMode", "false");
  document.getElementsByTagName("body")[0].classList.remove("lightMode");
}
