const nodemailer = require('nodemailer');

const MAIL_HOST = process.env.KONG_AUTH_MAIL_HOST;
const MAIL_FROM = process.env.KONG_AUTH_MAIL_FROM;
const MAIL_USER = process.env.KONG_AUTH_MAIL_USER;
const MAIL_PASSWORD = process.env.KONG_AUTH_MAIL_PASSWORD;

const PUBLIC_HOST = process.env.PUBLIC_HOST || 'https://dereg.net';

const smtp = nodemailer.createTransport({
  host: MAIL_HOST,
  port: 465,
  secure: true,
  auth: {
    user: MAIL_USER,
    pass: MAIL_PASSWORD,
  },
});

const sendConfirmationLink = async (to, token, ui, tries = 3) => {
  let triesLeft = tries;
  let link;
  if (ui) {
    link = `${PUBLIC_HOST}/ui/signup/confirmation/${token}`;
  } else {
    link = `${PUBLIC_HOST}/signup/confirm?token=${token}`;
  }
  const mail = {
    from: `"DeRegNet API" <${MAIL_FROM}>`,
    to,
    subject: 'DeRegNet sign up confirmation',
    text: link,
  };
  while (triesLeft) {
    try {
      await smtp.sendMail(mail);
      break;
    } catch (error) {
      console.error(error);
      triesLeft--;
    }
  }
  if (!triesLeft) {
    console.log(`Could not send confirmation Link to ${to}`);
    // delete signup from db?
  } else {
    console.log(`Successfully send confirmation link to ${to}`);
  }
};

module.exports = {
  sendConfirmationLink,
};
