$(document).ready(function(){
    var audioElement = document.createElement("audio");

    audioElement.src = "http://codeskulptor-demos.commondatastorage.googleapis.com/descent/gotitem.mp3";
    $('#Play_Button').click(function(){
        audioElement.play();
    });
});
