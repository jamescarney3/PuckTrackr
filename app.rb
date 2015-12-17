require "cuba"
require "mote"
require "mote/render"

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
      res.write("This is a sandbox application for trying things out with the
                Cuba gem. In development it runs on a puma server.\n\n

                Your SecureRandom-generated CubaTutorialApp cookie is
                #{req.cookies["CubaTutorialApp"]}.")
    end
  end
end
