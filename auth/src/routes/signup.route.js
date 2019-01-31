const { Router } = require('express');

const proxy = require('../utils/proxy.util');
const messages = require('../utils/messages.util');
const signup = require('../controllers/signup.controller');

const router = Router();

// POST /signup
router.post('/', async (req, res) => {
  try {
    const usernameInvalid = await signup.usernameOccupied(req.body.username);
    const emailInvalid = await signup.emailOccupied(req.body.email);
    if (usernameInvalid) {
      messages.send(['Username already in use.', 409], res);
    } else if (emailInvalid) {
      messages.send(['Email already in use.', 409], res);
    } else {
      const root = proxy.getRealRoot(req);
      const response = await signup.post(req.body, root);
      res.status(201);
      res.json(response);
    }
  } catch (error) {
    console.log(error);
    messages.send(messages.INTERNAL_SERVER_ERROR, res);
  }
});

// POST /signup/confirm/:confirmationToken
router.get('/confirm/:confirmationToken', async (req, res) => {
  try {
    const verified = await signup.confirm(req.params.confirmationToken);
    if (!verified) {
      messages.send(messages.INVALID_TOKEN, res);
    } else {
      const validSignup = await signup.stillInDatabase(verified);
      if (validSignup) {
        await signup.registerConsumer(validSignup);
        messages.send(['Your account has been confirmed.', 201], res);
      } else {
        messages.send(messages.INVALID_TOKEN, res);
      }
    }
  } catch (error) {
    console.log(error);
    messages.send(messages.INTERNAL_SERVER_ERROR, res);
  }
});

module.exports = router;
