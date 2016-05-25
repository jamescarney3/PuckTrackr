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

  sampleGamePlayerCorsi: function(team, number){
    // ovie = u'8' (or arg number this flow assumes home team)
    // ovie_events = [event for event in game_json['events'] if ovie in [player['number'] for player in event['home_players']]]
    // ovie_shot_events = [event for event in ovie_events if event['event_type'] in ['SHOT', 'MISS', 'BLOCK', 'GOAL']]
    // ovie_shots_for = [event for event in ovie_shot_events if event['team'] == game_json['home_abbreviation']]
    // ovie_shots_against = [event for event in ovie_shot_events if event['team'] == game_json['visitor_abbreviation']]
    // ovie_corsi = float(len(ovie_shots_for)) / float(len(ovie_shots_against))
  }
}

module.exports = DemoController;
