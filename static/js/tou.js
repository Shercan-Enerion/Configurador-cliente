function dec2bin(dec) {
  return (dec >>> 0).toString(2);
}
$(document).ready(function () {
  $.getJSON("/static/js/data.json", function (jd) {
    if (dec2bin(jd.timeOfUse)[0] == 1) {
      $("#timeOfUse").attr("checked", "");
    }
    if (dec2bin(jd.timeOfUse)[1] == 1) {
      $("#monday").attr("checked", "");
    }
    if (dec2bin(jd.timeOfUse)[2] == 1) {
      $("#tuesday").attr("checked", "");
    }
    if (dec2bin(jd.timeOfUse)[3] == 1) {
      $("#wednesday").attr("checked", "");
    }
    if (dec2bin(jd.timeOfUse)[4] == 1) {
      $("#thursday").attr("checked", "");
    }
    if (dec2bin(jd.timeOfUse)[5] == 1) {
      $("#friday").attr("checked", "");
    }
    if (dec2bin(jd.timeOfUse)[6] == 1) {
      $("#saturday").attr("checked", "");
    }
    if (dec2bin(jd.timeOfUse)[7] == 1) {
      $("#sunday").attr("checked", "");
    }
    let texto = "#formMode1 option[value=";
    let texto1 = "'" + jd.mode1 + "']";
    $(texto + texto1).attr("selected", true);
    texto = "#formMode2 option[value=";
    texto1 = "'" + jd.mode2 + "']";
    $(texto + texto1).attr("selected", true);
    texto = "#formMode3 option[value=";
    texto1 = "'" + jd.mode3 + "']";
    $(texto + texto1).attr("selected", true);
    texto = "#formMode4 option[value=";
    texto1 = "'" + jd.mode4 + "']";
    $(texto + texto1).attr("selected", true);
    texto = "#formMode5 option[value=";
    texto1 = "'" + jd.mode5 + "']";
    $(texto + texto1).attr("selected", true);
    texto = "#formMode6 option[value=";
    texto1 = "'" + jd.mode6 + "']";
    $(texto + texto1).attr("selected", true);
  });
});

$(document).ready(function () {
  $(document).on("submit", "#my-form", function () {
    $.ajax({
      url: "/tou",
      type: "post",
      dataType: "html",
      data: $("#my-form").serialize(),
    });
    return false;
  });
});
function settings() {
  let text = document.getElementById("textSetting").value;
  let description = document.getElementById("textDescription").value;
  window.alert("Save event");
  $.ajax({
    type: "POST", // la variable type guarda el tipo de la peticion GET,POST,..
    url: "/settings/" + text + "/" + description, //url guarda la ruta hacia donde se hace la peticion
    data: $("#my-form").serialize(), // data recive un objeto con la informacion que se enviara al servidor
    dataType: "html", // El tipo de datos esperados del servidor. Valor predeterminado: Intelligent Guess (xml, json, script, text, html).
  });
}
