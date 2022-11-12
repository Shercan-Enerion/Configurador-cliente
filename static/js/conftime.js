function int2Hour(num) {
  if (num.toString().length == 4){  
  let hour = num.toString().slice(0, 2);
  let minutes = num.toString().slice(2, 4);
    return hour + ":" + minutes;
  } else{
    let hour = num.toString().slice(0, 1);
    let minutes = num.toString().slice(1, 3);
    return '0' + hour + ":" + minutes;
    }
}

$(document).ready(function () {
  $.getJSON("/static/js/data.json", function (jd) {
    $("#hour1").attr("value", int2Hour(jd.hour1));
    $("#hour2").attr("value", int2Hour(jd.hour2));
    $("#hour3").attr("value", int2Hour(jd.hour3));
    $("#hour4").attr("value", int2Hour(jd.hour4));
    $("#hour5").attr("value", int2Hour(jd.hour5));
    $("#hour6").attr("value", int2Hour(jd.hour6));
    $("#power1").attr("value", jd.power1);
    $("#power2").attr("value", jd.power2);
    $("#power3").attr("value", jd.power3);
    $("#power4").attr("value", jd.power4);
    $("#power5").attr("value", jd.power5);
    $("#power6").attr("value", jd.power6);
    $("#soc1").attr("value", jd.soc1);
    $("#soc2").attr("value", jd.soc2);
    $("#soc3").attr("value", jd.soc3);
    $("#soc4").attr("value", jd.soc4);
    $("#soc5").attr("value", jd.soc5);
    $("#soc6").attr("value", jd.soc6);
  });
});

$(document).ready(function () {
  $(document).on("submit", "#my-form", function () {
    $.ajax({
      url: "/conftime1",
      type: "post",
      dataType: "html",
      data: $("#my-form").serialize(),
    });
    return false;
  });
});
