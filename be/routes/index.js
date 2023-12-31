var express = require('express');
require('dotenv').config();
const axios = require('axios');
const { token } = require('morgan');
var router = express.Router();

const SPOTIFY_CLIENT_ID = process.env.SPOTIFY_CLIENT_ID;
const SPOTIFY_CLIENT_SECRET = process.env.SPOTIFY_CLIENT_SECRET;
const REDIRECT_URI = process.env.REDIRECT_URI;
const COOKIE_SECRET = process.env.COOKIE_SECRET;

/* GET home page. */
router.get('/', function (req, res, next) {
    res.send('Index!');
});

router.post('/query', async function (req, res, next) {
    try {
        const response = await fetch('http://localhost:8080/query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                accessToken: req.body.access_token,
                queryString: req.body.search_query,
            }),
        });
        const jsonResponse = await response.json();
        console.log(jsonResponse);
        res.json({ result: jsonResponse.result });
    } catch (error) {
        // Handle any errors that occurred during the request
        console.error(error);
    }
});

module.exports = router;
