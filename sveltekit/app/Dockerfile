# check newest node version: https://hub.docker.com/_/node
FROM node:21-alpine

WORKDIR /app

# install dependencies
COPY package*.json ./
RUN npm install

# copy source code
COPY . .

RUN chown -R node:node /app
USER node

# start dev server
CMD [ "npm", "run", "dev"]