const apm = require('elastic-apm-node').start({
  serviceName: 'kong-auth',
  serverUrl: 'http://apm-server:8200',
});

const express = require('express');
const morgan = require('morgan');
const bodyParser = require('body-parser');
const helmet = require('helmet');
const mongoose = require('mongoose');

const schemaValidator = require('./src/middleware/schema.validation.middleware');
const signUp = require('./src/routes/signup.route');
const consumer = require('./src/routes/consumer.route');

const app = express();

const MONGO_URI = process.env.KONG_AUTH_MONGO_URI || 'mongodb://db/kong_auth';

app.use(morgan('common', { immediate: true }));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(helmet());

app.use(schemaValidator);
app.use('/signup', signUp);
app.use('/consumer', consumer);

const HOST = process.env.KONG_AUTH_HOST || 'localhost';
const PORT = process.env.KONG_AUTH_PORT || 5000;

const listen = async () => {
  try {
    await mongoose.connect(MONGO_URI, {
      connectTimeoutMS: 10000,
    });
  } catch (error) {
    console.log(error);
  }
  app.listen(PORT, HOST, () => {
    console.log(`[KONG AUTH] listening on http://${HOST}:${PORT}`);
  });
};

listen();
