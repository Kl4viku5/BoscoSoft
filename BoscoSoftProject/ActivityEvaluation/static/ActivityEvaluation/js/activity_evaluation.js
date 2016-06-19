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
        el.prop("visibility","visible");
    }
    else {
        el.prop("visibility","hidden");
    }
}