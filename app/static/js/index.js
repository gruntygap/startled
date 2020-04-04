console.log("setting up...");
window.onload = function() {
    document.getElementById('on').setAttribute('onclick','fetch("/on")');
    document.getElementById('off').setAttribute('onclick','fetch("/off")');
    document.getElementById('rainbow').setAttribute('onclick','fetch("/rainbow")');
    console.log("set up!");
};
