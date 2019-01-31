const joi = require('joi');

const schemas = new Map();

const postSignupSchema = joi.object().keys({
  username: joi.string().required(),
  email: joi.string().email().required(),
  password: joi.string().required(),
  name: joi.string(),
});

schemas.set('POST@/signup', postSignupSchema);

module.exports = schemas;
