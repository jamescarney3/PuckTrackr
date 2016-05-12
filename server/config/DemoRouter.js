var express = require('express');
var controller = require('../controllers/DemoController')

var DemoRouter = express.Router();

DemoRouter.get('/gamedemo', function(req, res){
  res.json(controller.sampleGameCorsiEventsByTeam());
});

DemoRouter.get('/playerdemo/:team/:number', function(req, res){
  res.json(controller.sampleGameCorsiEventsByPlayer(
    req.params.team,
    req.params.number
  ));
});

module.exports = DemoRouter;
