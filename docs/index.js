const fs = require('fs');
const app = require('express')();
const morgan = require('morgan');
const swaggerUi = require('swagger-ui-express');

const HOST = process.env.SWAGGER_DOCS_HOST || 'localhost';
const PORT = process.env.SWAGGER_DOCS_PORT || 5000;


const SPEC = process.env.SWAGGER_DOCS_SPEC;
const spec = JSON.parse(fs.readFileSync(SPEC));

const NAME = process.env.SWAGGER_DOCS_NAME;
const BASE = process.env.SWAGGER_DOCS_BASE || `/docs/${NAME}/`;
const AUTH = process.env.SWAGGER_DOCS_AUTH || 'basic';

if (AUTH === 'basic') {
  spec.securityDefinitions = {
    basicAuth: {
      type: 'basic',
    },
  };
  spec.security = {
    basicAuth: [],
  };
}

app.use(morgan('common', { immediate: true }));

const swaggerUiSetup = (
  swaggerDoc,
  base,
  opts,
  options,
  customCss,
  customfavIcon,
  swaggerUrl,
  customeSiteTitle,
) => {
  let htmlWithOptions = swaggerUi.generateHTML(
    swaggerDoc,
    opts,
    options,
    customCss,
    customfavIcon,
    swaggerUrl,
    customeSiteTitle,
  );
  htmlWithOptions = htmlWithOptions.replace(
    '<title>Swagger UI</title>\n',
    `<title>${NAME} UI</title>\n  <base href="${base}">\n`,
  );
  return (req, res) => res.send(htmlWithOptions);
};

app.use('/', swaggerUi.serve);
app.get('/', (req, res) => {
  const { headers } = req;
  const proto = headers['x-forwarded-proto'];
  const host = headers['x-forwarded-host'];
  const port = headers['x-forwarded-port'];
  const base = `${proto}://${host}:${port}${BASE}`;
  spec.host = `${host}:${port}`;
  spec.basePath = `/${NAME}`;
  return swaggerUiSetup(spec, base)(req, res);
});


// app.set('trust proxy', '172.27.0.9');

app.listen(PORT, HOST, () => {
  console.log(`[SWAGGER DOCS] listening at http://${HOST}:${PORT}`);
});
