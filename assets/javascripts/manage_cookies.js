(function(){
  if(typeof window.CubaTutorial === "undefined"){
    window.CubaTutorial = {};
  }

  var deleteCookie = CubaTutorial.deleteCookie = function(event){
    event.preventDefault();

    var button = event.currentTarget;
    var cookieDisplay = $("#cookieDisplay");
    var url = "/deleteCookie";

    $(button).attr("disabled", true);

    $.ajax({
      method: "GET",
      url: url,
      dataType: "text",
      success: function(){
        $(cookieDisplay).html("Cookie deleted!")
      }
    });
  };


})()
