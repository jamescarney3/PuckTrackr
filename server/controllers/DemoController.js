var fs = require('fs-extra');
var _ = require('underscore');

var DemoController = {
  sampleGameCorsiEventsByTeam: function(callback){
    var content = fs.readJson('./resources/sampleGame1.json', function(err, gameData){
      var shotsData = {
        home: {
          abbreviation: gameData.home_abbreviation,
          shotEvents: []
        },
        visitor: {
          abbreviation: gameData.visitor_abbreviation,
          shotEvents: []
        }
      };

      // This mess needs to get broken out into some more sort of more dedicated
      // business logic module... this ugly function will not suffice going
      // forward for anything but kicking D3 around

      _.select(gameData.events, function(gameEvent){
          return _.includes(["SHOT", "BLOCK", "MISS", "GOAL"], gameEvent.event_type);
      }).forEach(function(shotEvent){
        if(shotEvent.description.slice(0,3) === gameData.home_abbreviation) {
          shotsData.home.shotEvents.push(
            parseInt((shotEvent.period - 1) * 1200) + parseInt(shotEvent.time_elapsed.split(':')[0] * 60) + parseInt(shotEvent.time_elapsed.split(':')[1])
          );
        } else if(shotEvent.description.slice(0,3) === gameData.visitor_abbreviation) {
          shotsData.visitor.shotEvents.push(
            parseInt((shotEvent.period - 1) * 1200) + parseInt(shotEvent.time_elapsed.split(':')[0] * 60) + parseInt(shotEvent.time_elapsed.split(':')[1])
          );
        }
      });

      callback(shotsData);
    });
  },

  sampleGameCorsiEventsByPlayer: function(team, number){
    // I still don't do anything - I still need the scraper to be able to parse
    // TOI reports and attach players to events by team & number in orer to
    // computer shot differentials and relative shot differentials
  }
}

module.exports = DemoController;
