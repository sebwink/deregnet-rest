const { Router } = require('express');
const bcrypt = require('bcrypt');
const joi = require('joi');

const messages = require('../utils/messages.util');
const jwt = require('../utils/jwt.util');
const mail = require('../utils/mail.util');
const Consumer = require('../models/consumer.model');
const SignUp = require('../models/signup.model');

const SALT_COST = process.env.KONG_AUTH_SALT_COST || 10;

const usernameOccupied = async (username) => {
  const usernameRegistered = await Consumer.findOne({ username });
  if (usernameRegistered) {
    return true;
  }
  const usernamePendingSignUp = await SignUp.findOne({ username });
  return usernamePendingSignUp;
};

const emailOccupied = async (email) => {
  const emailRegistered = await Consumer.findOne({ email });
  if (emailRegistered) {
    return true;
  }
  const emailPendingSignUp = await SignUp.findOne({ email });
  return emailPendingSignUp;
};

const router = Router();

const signUpPostPayload = joi.object().keys({
  username: joi.string().required(),
  email: joi.string().email().required(),
  password: joi.string().required(),
  name: joi.string(),
});

const isValid = (payload, schema) => (
  new Promise((resolve) => {
    joi.validate(payload, schema, (error) => {
      if (error) {
        resolve(false);
      } else {
        resolve(true);
      }
    });
  })
);

// POST /signup
router.post('/', async (req, res) => {
  try {
    const payloadInvalid = !(await isValid(req.body, signUpPostPayload));
    if (payloadInvalid) {
      messages.send(messages.INVALID_PAYLOAD, res);
    } else {
      const usernameInvalid = await usernameOccupied(req.body.username);
      const emailInvalid = await emailOccupied(req.body.email);
      if (usernameInvalid) {
        messages.send(['Username already in use.', 409], res);
      } else if (emailInvalid) {
        messages.send(['Email already in use.', 409], res);
      } else {
        const { username, email } = req.body;
        let { password } = req.body;
        const salt = await bcrypt.genSalt(SALT_COST);
        password = await bcrypt.hash(password, salt);
        const signup = new SignUp({
          username,
          email,
          password,
        });
        await signup.save();
        const confirmationToken = await jwt.sign({ username }, {
          algorithm: jwt.algorithm,
          expiresIn: jwt.expiresIn,
        });
        mail.sendConfirmationLink(email, confirmationToken);
        res.status(201);
        res.json({
          username,
          email,
        });
      }
    }
  } catch (error) {
    messages.send(messages.INTERNAL_SERVER_ERROR, res);
  }
});

router.get('/confirm/:confirmationToken', async (req, res) => {
  try {
    const { confirmationToken } = req.params;
    const verified = await jwt.verify(confirmationToken, {
      algorithms: [jwt.algorithm],
    });
    if (!verified) {
      messages.send(messages.INVALID_TOKEN, res);
    } else {
      const { username } = verified;
      const signup = await SignUp.findOne({ username });
      if (signup) {
        messages.send(['Your account has been confirmed.', 201], res);
      } else {
        messages.send(messages.INVALID_TOKEN, res);
      }
    }
  } catch (error) {
    messages.send(messages.INTERNAL_SERVER_ERROR, res);
  }
});

module.exports = router;
