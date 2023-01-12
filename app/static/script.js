setTimeout(function () {
    document.querySelector(".preloader").style.display = "none";
    document.querySelector(".container").style.display = "block";
  }, 1000);
  
function redirectPage(){
    window.location.href = "http://127.0.0.1:8000/app/cadastro";
};