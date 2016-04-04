require "cuba"
require "mote"
require "mote/render"
require 'json'
require 'byebug'

require_relative "scraper.rb"
require_relative "game.rb"
require_relative "event.rb"

Cuba.plugin(Mote::Render)

Cuba.define do
  on root do
    res.write partial("home", some_var: "abc")
  end

  on get do
    on "about" do
      res.write("This is the beginning of an application to track NHL stats in
      real-ish time. Nothing works yet, but it will soon.")
    end

    on "samplegame" do
      res.write partial("samplegame")
    end

    # this should serve up a list of game data in string format
    on "api" do
      on "samplegame" do

        url = "http://www.nhl.com/scores/htmlreports/20152016/PL010003.HTM"

        scraper = Scraper.new.scrape(url)
        shot_data = {
          fla_shots: scraper.data.select{ |e| ["SHOT", "GOAL"].include?(e.split[5]) && e.split[6] == "FLA" },
          nsh_shots: scraper.data.select{ |e| ["SHOT", "GOAL"].include?(e.split[5]) && e.split[6] == "NSH" }
        }

        res.write(shot_data.to_json)
      end
    end
  end
end
