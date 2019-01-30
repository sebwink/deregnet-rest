FROM node:10

RUN apt-get update && apt-get -y upgrade
RUN npm i -g nodemon
RUN mkdir /app

WORKDIR /app

COPY main.js .
COPY package.json .
COPY src src 

RUN npm install

CMD ["nodemon", "main.js"]
