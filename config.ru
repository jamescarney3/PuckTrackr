require "./app"

use Rack::Static, :urls => ["/javascripts", "/img"],
                  :root => "assets"

# use Rack::Session::Cookie, :key => 'rack.session',
#                            :domain => 'foo.com',
#                            :path => '/',
#                            :expire_after => 2592000,
#                            :secret => 'change_me',
#                            :old_secret => 'also_change_me'

# use Rack::Session::Pool

run(Cuba)
