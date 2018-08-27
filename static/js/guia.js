function mouseoutDisplayShow() {
  document.getElementById('logo-small1').style.display = "block";
}

function mouseoverDisplayNone() {
  document.getElementById('logo-small1').style.display = "none";
}

var sidebar_status = Boolean(false);

function sidebarButton(){
  if (sidebar_status == false) {
    $('body').removeClass('sidebar-mini');
    document.getElementById('logo-small1').style.display = "none";
    document.getElementById('logo-small2').style.display = "none";
    console.log("ok none");
    sidebar_status = true;
  } else {
    $('body').addClass('sidebar-mini');
    document.getElementById("logo-small1").style.display = "block";
    document.getElementById("logo-small2").style.display = "block";
    console.log("ok block");
    sidebar_status = false;
  }

}
