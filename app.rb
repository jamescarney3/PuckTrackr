require "cuba"

Cuba.define do
  on root do
    res.write("Hello world!")
  end

  on "about" do
    res.write("This is a sandbox application for trying things out with the
              Cuba gem. In development it runs on a puma server.")
    end
end
