$(document).ready(function() {
    $("#Search-Activities").click(function () {
        toggleClassById("overlay", "hide");
    });
    $("#Close-search").click(function() {
        toggleClassById("overlay", "hide");
        clearInputTextById("Search-age");
        clearInputTextById("Search-name");
    });
    $(function () {
        $(".datepicker").datepicker();
    });
});

function toggleClassById(id, className) {
    var elementToToggle = $("#"+ id);
    elementToToggle.toggleClass(className);
}

function clearInputTextById(id) {
    var inputTextToClear = $("#" + id);
    inputTextToClear.val("");
}
