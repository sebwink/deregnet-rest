FROM node:10

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y openssl
RUN npm i -g nodemon
RUN mkdir /app

WORKDIR /app

COPY main.js .
COPY package.json .
COPY src src 

RUN npm install

ENTRYPOINT ["nodemon", "main.js"]
