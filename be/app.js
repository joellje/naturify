var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
const PORT = 5000;
const mongoose = require('mongoose');
require('dotenv').config();
const db_uri = process.env.MONGODB_URI;

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');
var cors = require('cors');
var app = express();

// view engine setup
app.use(cors({ origin: 'http://localhost:3000' }));
app.use(express.json());
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);

/* Connecting to the database and then starting the server. */
mongoose
    .connect(db_uri)
    .then(() => {
        app.listen(PORT, '0.0.0.0', () => console.log(`Database started. HTTP Server started on port ${PORT}`));
    })
    .catch((err) => {
        console.log(err);
    });

module.exports = app;
