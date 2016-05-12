var express = require('express');
var MainRouter = require('./config/Router.js')

// Start this with 'node testServer.js' command from the root dir

var App  = express();

App.use(express.static(__dirname + '/public'));

App.use('/api', MainRouter);

App.listen(6969, function(){
  console.log('Listening on port 6969!')
});
