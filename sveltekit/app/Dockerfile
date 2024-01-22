# check newest node version: https://hub.docker.com/_/node
FROM node:21-alpine

WORKDIR /app

USER node

# install dependencies
COPY package*.json ./
RUN npm install
# copy source code
COPY . .

# start dev server
CMD [ "npm", "run", "dev"]