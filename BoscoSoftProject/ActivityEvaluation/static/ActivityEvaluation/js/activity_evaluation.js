$(document).ready(function() {
    $("#SearchActivities").click(function () {
        overlay(true);
    });
});
function overlay(makeVisible) {
    setPopupVisibilityById("overlay", makeVisible);
    /*
    if(makeVisible) {
        el.style.visibility = "visible";
    }
    else {
        el.style.visibility = "hidden";
    }
    */
}
function setPopupVisibilityById(id, makeVisible) {
    var el = $("#"+ id);
     if(makeVisible) {
        el.toggleClass("hide");
    }
    else {
        el.toggleClass("hide");
    }
}