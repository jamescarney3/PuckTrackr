(function(){
  if(typeof window.CubaTutorial === "undefined"){
    window.CubaTutorial = {};
  }

  var setUserArray = CubaTutorial.setUserArray = function(event){
    event.preventDefault();
    var url = "/database/set";
    var formData = $("#userArraySetter");

    $.ajax({
      method: "GET",
      url: url,
      dataType: "text",
      data: formData.serialize(),
      success: function(){
        alert("Current user array updated!")
      },
      error: function(){
        alert("There was an error...")
      }
    });
  };

  var getUserArray = CubaTutorial.getUserArray = function(){
    var url = "database/get";
    var userArrayEl = $("#userArrayEl");
    var userArrayWrapper = $("#userArrayWrapper");

    $.ajax({
      method: "GET",
      url: url,
      dataType: "text",
      success: function(response){
        $(userArrayWrapper).show();
        $(userArrayEl).html(response);
      }
    });
  };
})()
