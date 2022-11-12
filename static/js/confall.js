$(document).ready(function () {
  $.getJSON("/static/js/data.json", function (jd) {
    if (jd.solarSell == 1) {
      $("#solarSellCheck").attr("checked", "");
    }
    if (jd.pattern == 1) {
      $("#selectPattern option[value='0']").attr("selected", true);
    }
    $("#maxSellPower").attr("value", jd.maxSellPower);
    $("#maxSolarPower").attr("value", jd.maxSolarPower);
  });
});

$(document).ready(function () {
  $(document).on("submit", "#my-form", function () {
    $.ajax({
      url: "/confall",
      type: "post",
      dataType: "html",
      data: $("#my-form").serialize(),
    });
    return false;
  });
});
