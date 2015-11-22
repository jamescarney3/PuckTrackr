require "cuba"
require "mote"
require "mote/render"

Cuba.plugin(Mote::Render)

Cuba.define do
  on root do
    res.write partial("home")
  end

  on get do
    on "about" do
      res.write("This is a sandbox application for trying things out with the
                Cuba gem. In development it runs on a puma server.")
    end
  end
end
