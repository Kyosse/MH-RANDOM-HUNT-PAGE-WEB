window.onload = function() {

    var video = document.getElementById("header-video");
    var fullScreenButton = document.getElementById("full-screen");
                
        fullScreenButton.addEventListener("click", function() {
      if (video.requestFullscreen) {video.requestFullscreen();} 
        else if (video.mozRequestFullScreen) {video.mozRequestFullScreen(); } 
        else if (video.webkitRequestFullscreen) {video.webkitRequestFullscreen();}
    })};