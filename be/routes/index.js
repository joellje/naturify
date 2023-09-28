var express = require("express");
require("dotenv").config();
const axios = require("axios");
const { token } = require("morgan");
var router = express.Router();

const SPOTIFY_CLIENT_ID = process.env.SPOTIFY_CLIENT_ID;
const SPOTIFY_CLIENT_SECRET = process.env.SPOTIFY_CLIENT_SECRET;
const REDIRECT_URI = process.env.REDIRECT_URI;
const COOKIE_SECRET = process.env.COOKIE_SECRET;

/* GET home page. */
router.get("/", function (req, res, next) {
  res.send("Index!");
});

router.post("/query", function (req, res, next) {
  console.log(req.body);
  const dummyData = {
    message: "This is a dummy JSON response",
    data: {
      key1: "value1",
      key2: "value2",
    },
  };

  res.json(dummyData);
});

module.exports = router;
