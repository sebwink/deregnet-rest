const getRealRoot = ({ headers }) => {
  const proto = headers['x-forwarded-proto'];
  const host = headers['x-forwarded-host'];
  const port = headers['x-forwarded-port'];
  return `${proto}://${host}:${port}`;
};

module.exports = {
  getRealRoot,
};
