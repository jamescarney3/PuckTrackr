var express = require('express');
var controller = require('../controllers/DemoController')

var DemoRouter = express.Router();

DemoRouter.get('/gamedemo', function(req, res){
  controller.sampleGameCorsiEventsByTeam(function(data){
    res.json(data);
  });
});

DemoRouter.get('/playerdemo/:team/:number', function(req, res){
  res.json(controller.sampleGameCorsiEventsByPlayer(
    req.params.team,
    req.params.number
  ));
});

module.exports = DemoRouter;
