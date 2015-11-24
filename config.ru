require "./app"

use Rack::Static, :urls => ["/javascripts", "/img"],
                  :root => "assets"

use Rack::Session::Cookie, :key => 'rack.session',
                           :domain => 'foo.com',
                           :path => '/',
                           :expire_after => 2592000

run(Cuba)
