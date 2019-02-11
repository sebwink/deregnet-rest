const Consumer = require('../models/consumer.model');
const jwt = require('../utils/jwt.util');
const kongJwt = require('../utils/kong/jwt.util');

const token = async (kongId) => {
  const { username } = await Consumer.findOne({ kongId });
  const { key } = await kongJwt.post(username);
  const accessToken = await jwt.sign({ iss: key });
  return accessToken;
};

module.exports = {
  token,
};
