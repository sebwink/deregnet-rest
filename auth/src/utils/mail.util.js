const nodemailer = require('nodemailer');

const MAIL_HOST = process.env.KONG_AUTH_MAIL_HOST;
const MAIL_FROM = process.env.KONG_AUTH_MAIL_FROM;
const MAIL_USER = process.env.KONG_AUTH_MAIL_USER;
const MAIL_PASSWORD = process.env.KONG_AUTH_MAIL_PASSWORD;

const smtp = nodemailer.createTransport({
  host: MAIL_HOST,
  port: 465,
  secure: true,
  auth: {
    user: MAIL_USER,
    pass: MAIL_PASSWORD,
  },
});

const sendConfirmationLink = async (to, token, root) => {
  const mail = {
    from: `"DeRegNet API" <${MAIL_FROM}>`,
    to,
    subject: 'DeRegNet sign up confirmation',
    text: `${root}/signup/confirm/${token}`,
  };
  await smtp.sendMail(mail);
};

module.exports = {
  sendConfirmationLink,
};
