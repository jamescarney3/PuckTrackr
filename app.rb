require "cuba"
require "mote"
require "mote/render"
require "byebug"
require 'securerandom'


Cuba.plugin(Mote::Render)

Cuba.define do
  on root do
    if req.cookies["CubaTutorialApp"]
      cta_cookie = req.cookies["CubaTutorialApp"]
    else
      cookie = SecureRandom::urlsafe_base64
      res.set_cookie("CubaTutorialApp", cookie)
    end
    res.write partial("home", cookie: cta_cookie)
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

    on "deleteCookie" do
      res.delete_cookie("CubaTutorialApp")
      res.write(nil)
    end

  end
end
