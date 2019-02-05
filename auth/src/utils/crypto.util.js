const bcrypt = require('bcrypt');
const crypto = require('crypto');

const SALT_COST = parseInt(process.env.KONG_AUTH_SALT_COST, 10) || 10;

const AES_ALGORITHM = process.env.KONG_AUTH_AES || 'aes-192-cbc';
const AES_KEY_LENGTH = parseInt(process.env.KONG_AUTH_AES_KEY_LENGTH, 10) || 24;
const AES_PASSWORD = process.env.KONG_AUTH_AES_PASSWORD;
const AES_SALT = bcrypt.genSaltSync(SALT_COST);
const AES_KEY = crypto.scryptSync(AES_PASSWORD, AES_SALT, AES_KEY_LENGTH);
const AES_IV = crypto.randomBytes(16);

const hashPassword = async (password) => {
  const salt = await bcrypt.genSalt(SALT_COST);
  return bcrypt.hash(password, salt);
};

const encrypt = (data) => {
  const cipher = crypto.createCipheriv(AES_ALGORITHM, AES_KEY, AES_IV);
  let encrypted = cipher.update(data, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  return encrypted;
};

const decrypt = (data) => {
  const decipher = crypto.createDecipheriv(AES_ALGORITHM, AES_KEY, AES_IV);
  let decrypted = decipher.update(data, 'hex', 'utf-8');
  decrypted += decipher.final('utf-8');
  return decrypted;
};

module.exports = {
  hashPassword,
  encrypt,
  decrypt,
};
