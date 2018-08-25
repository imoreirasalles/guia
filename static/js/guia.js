function mouseoutDisplayShow(id) {
  document.getElementById(id).style.display = "block";
}
function mouseoverDisplayNone(id) {
  document.getElementById(id).style.display = "none";
}

sidebar_mini_active = true;

function navbarExpand() {
  if (sidebar_mini_active == true;){
    console.log('true');
    sidebar_mini_active = false;
  }else{
    console.log('false');
    sidebar_mini_active = true;
  }

}
// function mouseClikOutDisplayShow(id) {
//   document.getElementsByTagName(body).classList.add("logo-small");
//   document.getElementById("logo-small").style.display = "block";
// }
// function mouseClickOverDisplayNone(id) {
//   document.getElementsByTagName(body).removeClass("logo-small");
//   document.getElementById("logo-small").style.display = "none";
// }
