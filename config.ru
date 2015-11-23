require "./app"

use Rack::Static, :urls => ["/javascripts", "/img"], :root => "assets"

run(Cuba)
