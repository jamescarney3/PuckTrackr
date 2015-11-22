require "./app"

use Rack::Static, :urls => ["/lib"]

run(Cuba)
