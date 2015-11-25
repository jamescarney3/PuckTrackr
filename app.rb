require "cuba"
require "mote"
require "mote/render"
require "byebug"
require 'securerandom'


Cuba.plugin(Mote::Render)

Cuba.define do
  on root do
    byebug
    cookie = SecureRandom::urlsafe_base64
    res.set_cookie("CubaTutorialApp", cookie)
    res.write partial("home")
  end

  on get do
    on "about" do
      res.write("This is a sandbox application for trying things out with the
                Cuba gem. In development it runs on a puma server.\n\n

                Your SecureRandom-generated CubaTutorialApp cookie is
                #{req.cookies["CubaTutorialApp"]}.")
    end

    on "randnum" do
      sleep 2
      res.write(rand(100))
    end
  end
end
