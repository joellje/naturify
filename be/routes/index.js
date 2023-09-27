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

router.get("/login", function (req, res, next) {
  console.log("here");
  const secret = COOKIE_SECRET;
  res.cookie("spotify_auth_secret", secret);

  const scope = "user-read-private user-read-email";

  const queryParams = querystring.stringify({
    client_id: SPOTIFY_CLIENT_ID,
    response_type: "code",
    redirect_uri: REDIRECT_URI,
    secret: secret,
    scope: scope,
  });
  res.redirect(`https://accounts.spotify.com/authorize?${queryParams}`);
});

router.get("/callback", async function (req, res, next) {
  try {
    const code = req.query.code || null;

    const tokenResponse = await axios.post(
      "https://accounts.spotify.com/api/token",
      querystring.stringify({
        grant_type: "authorization_code",
        code: code,
        redirect_uri: REDIRECT_URI,
      }),
      {
        headers: {
          "content-type": "application/x-www-form-urlencoded",
          Authorization: `Basic ${Buffer.from(
            `${SPOTIFY_CLIENT_ID}:${SPOTIFY_CLIENT_SECRET}`
          ).toString("base64")}`,
        },
      }
    );

    if (tokenResponse.status === 200) {
      // Handle successful authentication here
      // Store tokens?
      const { access_token, token_type } = tokenResponse.data;
      console.log(access_token);
      console.log(token_type);
      const meResponse = await axios.get("https://api.spotify.com/v1/me", {
        headers: {
          Authorization: `${token_type} ${access_token}`,
        },
      });
      console.log(meResponse.data);
      res.redirect("http://localhost:3000/home");
    } else {
      res.send(tokenResponse);
    }
  } catch (error) {
    res.send(error);
  }
});

router.get("/refresh_token", async function (req, res) {
  try {
    const { refresh_token } = req.query;

    const tokenResponse = await axios({
      method: "post",
      url: "https://accounts.spotify.com/api/token",
      data: querystring.stringify({
        grant_type: "refresh_token",
        refresh_token: refresh_token,
      }),
      headers: {
        "content-type": "application/x-www-form-urlencoded",
        Authorization: `Basic ${new Buffer.from(
          `${SPOTIFY_CLIENT_ID}:${SPOTIFY_CLIENT_SECRET}`
        ).toString("base64")}`,
      },
    });
    res.send(tokenResponse.data);
  } catch (error) {
    res.send(error);
  }
});

module.exports = router;
