(function(){
  if(typeof window.CubaTutorial === "undefined"){
    window.CubaTutorial = {};
  }

  var getRandNum = CubaTutorial.getRandNum = function(event){
    event.preventDefault();
    var button =  event.currentTarget;
    var randNumEl = $("#serverRandNum");
    var url = "/randnum";

    $(button).attr("disabled", true);

    $.ajax({
      method: "GET",
      url: url,
      dataType: "text",
      success: function(response, status){
        $(randNumEl).html(response);
        $(button).attr("disabled", false);
      }
    });
  };

})()
