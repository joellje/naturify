var express = require("express");
require("dotenv").config();
const querystring = require("querystring");
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


module.exports = router;
