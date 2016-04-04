(function(){
  if(typeof window.CubaTutorial === "undefined"){
    window.CubaTutorial = {};
  }

  CubaTutorial.sayHello = function(){
    alert("Hello, world!");
  };

  CubaTutorial.generateChart = function(){
    $.ajax({
      url: "api/samplegame",
      method: "GET",
      success: function(response){
        respData = JSON.parse(response);
        CubaTutorial.shotsChart(respData.fla_shots, respData.nsh_shots);
      }
    });
  };

  CubaTutorial.shotsChart = function(homeShots, awayShots) {
    var seconds = [];
    for (i = 1; i <= 3900; i ++) {
      seconds = seconds.concat(i);
    }

    var homeTeamShotTimes = _.map(homeShots, function(shotEvent){
      var period = shotEvent[1];
      var minutes = shotEvent[3].split[":"][0];
      var seconds = shotEvent[3].split[":"][1];
      return (period - 1) * 1200 + minutes * 60 + seconds
    });

    var awayTeamShotTimes = _.map(awayShots, function(shotEvent){
      var period = shotEvent[1];
      var minutesElapsed = shotEvent[3].split[":"][0];
      var secondsElapsed = shotEvent[3].split[":"][1];
      return (period - 1) * 1200 + minutesElapsed * 60 + secondsElapsed
    });

    homeShotsData = [0];
    awayShotsData = [0];
    homeShotsIdx = 0;
    awayShotsIdx = 0;
    seconds.forEach(function(second){
      if(homeTeamShotTimes[homeShotsIdx] == second){
        homeShotsData.concat(second);
        homeShotsIdx += 1;
      } else {
        homeShotsData.concat(null);
      }
      if(awayTeamShotTimes[awayShotsIdx] == second){
        awayShotsData.concat(second);
        awayShotsIdx += 1;
      } else {
        awayShotsData.concat(null);
      }
    });


    data = {
      labels: seconds,
      datasets: [
        {
          label: "Home team shots",
          fillColor: "rgba(220,220,220,0.2)",
          strokeColor: "rgba(220,220,220,1)",
          pointColor: "rgba(220,220,220,1)",
          pointStrokeColor: "#fff",
          pointHighlightFill: "#fff",
          pointHighlightStroke: "rgba(220,220,220,1)",
          data: homeShotsData
        },
        {
          label: "My Second dataset",
          fillColor: "rgba(151,187,205,0.2)",
          strokeColor: "rgba(151,187,205,1)",
          pointColor: "rgba(151,187,205,1)",
          pointStrokeColor: "#fff",
          pointHighlightFill: "#fff",
          pointHighlightStroke: "rgba(151,187,205,1)",
          data: awayShotsData
        }
      ]
    }
    var ctx = document.getElementById("shotChart").getContext("2d");
    var lineChart = new Chart(ctx).Line(data);
  };

})()
