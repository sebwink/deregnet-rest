FROM node:10

RUN apt-get update && apt-get -y upgrade

RUN mkdir -p /app/specs
WORKDIR /app

COPY ./docs/index.js .
COPY ./docs/package.json .

RUN npm install && npm i -g nodemon

ENV SWAGGER_DOCS_HOST 0.0.0.0

CMD ["nodemon", "index.js"]
