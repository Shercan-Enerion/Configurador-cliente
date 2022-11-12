var e = document.getElementById("times");
var text = e.options[e.selectedIndex].text;
document.getElementById("form1").style.display = "inline";
document.getElementById("form2").style.display = "none";
document.getElementById("form3").style.display = "none";
document.getElementById("form4").style.display = "none";
document.getElementById("form5").style.display = "none";
document.getElementById("form6").style.display = "none";
function cambio() {
  var e = document.getElementById("times");
  var text = e.options[e.selectedIndex].text;
  switch (text) {
    case "Time 1":
      document.getElementById("form1").style.display = "inline";
      document.getElementById("form2").style.display = "none";
      document.getElementById("form3").style.display = "none";
      document.getElementById("form4").style.display = "none";
      document.getElementById("form5").style.display = "none";
      document.getElementById("form6").style.display = "none";
      break;
    case "Time 2":
      document.getElementById("form1").style.display = "none";
      document.getElementById("form2").style.display = "inline";
      document.getElementById("form3").style.display = "none";
      document.getElementById("form4").style.display = "none";
      document.getElementById("form5").style.display = "none";
      document.getElementById("form6").style.display = "none";
      break;
    case "Time 3":
      document.getElementById("form1").style.display = "none";
      document.getElementById("form2").style.display = "none";
      document.getElementById("form3").style.display = "inline";
      document.getElementById("form4").style.display = "none";
      document.getElementById("form5").style.display = "none";
      document.getElementById("form6").style.display = "none";
      break;
    case "Time 4":
      document.getElementById("form1").style.display = "none";
      document.getElementById("form2").style.display = "none";
      document.getElementById("form3").style.display = "none";
      document.getElementById("form4").style.display = "inline";
      document.getElementById("form5").style.display = "none";
      document.getElementById("form6").style.display = "none";
      break;
    case "Time 5":
      document.getElementById("form1").style.display = "none";
      document.getElementById("form2").style.display = "none";
      document.getElementById("form3").style.display = "none";
      document.getElementById("form4").style.display = "none";
      document.getElementById("form5").style.display = "inline";
      document.getElementById("form6").style.display = "none";
      break;
    case "Time 6":
      document.getElementById("form1").style.display = "none";
      document.getElementById("form2").style.display = "none";
      document.getElementById("form3").style.display = "none";
      document.getElementById("form4").style.display = "none";
      document.getElementById("form5").style.display = "none";
      document.getElementById("form6").style.display = "inline";
      break;
  }
}
