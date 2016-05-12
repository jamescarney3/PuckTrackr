var express = require('express');
var DemoRouter = require('./DemoRouter')

var MainRouter = express.Router();

// @TODO this is for reference and will be removed as the app
// takes shape around it
MainRouter.get('/', function(req, res){
  res.send('root endpoint of api router');
});

MainRouter.use('/demo', DemoRouter);

module.exports = MainRouter;
