const bcrypt = require('bcrypt');

const jwt = require('../utils/jwt.util');
const mail = require('../utils/mail.util');
const Consumer = require('../models/consumer.model');
const SignUp = require('../models/signup.model');
const kongConsumer = require('../utils/kong/consumer.util');
const kongBasicAuth = require('../utils/kong/basic.auth.util');

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

const postSignup = async (data, root) => {
  const { username, email, password } = data;
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
  await mail.sendConfirmationLink(
    email,
    confirmationToken,
    root,
  );
  return {
    username,
    email,
  };
};

const confirm = token => (
  new Promise(async (resolve) => {
    try {
      const verified = await jwt.verify(token, {
        algorithms: [jwt.algorithm],
      });
      resolve(verified);
    } catch (error) {
      resolve(false);
    }
  })
);

const stillInDatabase = async ({ username }) => {
  const signup = await SignUp.findOne({ username });
  return signup;
};

const registerConsumer = async (signup) => {
  const { username, password } = signup;
  // delete signup entity
  await SignUp.deleteOne({ username });
  // kong consumer and credentials
  const kongResponse = await kongConsumer.post(username);
  await kongBasicAuth.postCredentials(username, password);
  // password hash
  const salt = await bcrypt.genSalt(SALT_COST);
  const passwordHash = await bcrypt.hash(password, salt);
  // consumer
  const consumer = new Consumer({
    username,
    password: passwordHash,
    kongId: kongResponse.data.id,
    email: signup.email,
  });
  try {
    await consumer.save();
  } catch (error) {
    kongConsumer.delete(username);
    throw error;
  }
};

module.exports = {
  usernameOccupied,
  emailOccupied,
  confirm,
  stillInDatabase,
  registerConsumer,
  post: postSignup,
};
