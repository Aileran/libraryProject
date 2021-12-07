$(document).ready(function(){

    $('#light').click(setLight);
    $('#dark').click(setDark);
    $('#main').click(setMain);

    function setLight() {
        $("body").css("background-color", "beige")
    }

    function setDark() {
        $("body").css("background-color", "black")
    }

    function setMain() {
        $("body").css("background-color", "brown")
    }
});
