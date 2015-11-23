require "./app"

use Rack::Static, :urls => ["/javascripts"], :root => "assets"

run(Cuba)
