const axios = require('axios');

const KONG_ADMIN_API = process.env.KONG_AUTH_ADMIN_API || 'http://localhost:8001';

const kongConsumers = `${KONG_ADMIN_API}/consumers`;

const postConsumer = async username => (
  axios.post(kongConsumers, { username })
);

const getConsumer = async (consumerId) => {
  const url = `${kongConsumers}/${consumerId}`;
  return axios.get(url);
};

const deleteConsumer = async (consumerId) => {
  const url = `${kongConsumers}/${consumerId}`;
  return axios.delete(url);
};

module.exports = {
  postConsumer,
  getConsumer,
  deleteConsumer,
};
