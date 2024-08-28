document.addEventListener("DOMContentLoaded", function () {
  var login = document.getElementById("login");
  login.addEventListener("click", function () {
    window.location.href = "./login.html";
  });
});

document.addEventListener("DOMContentLoaded", function () {
  var login = document.getElementById("start");
  login.addEventListener("click", function () {
    window.location.href = "./chat.html";
  });
});

var socket = io();
socket.on("connect", function () {
  socket.emit("my event", { data: "I'm connected!" });
});
