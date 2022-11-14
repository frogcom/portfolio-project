function onderWerpen(evt, codeName) {
  var i, codecontent, tablinks;
  codecontent = document.getElementsByClassName("codecontent");
  for (i = 0; i < codecontent.length; i++) {
    codecontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(codeName).style.display = "block";
  evt.currentTarget.className += " active";
}
