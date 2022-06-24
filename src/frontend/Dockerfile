FROM node:alpine 
RUN mkdir /home/frontend
COPY . /home/frontend
WORKDIR /home/frontend
RUN npm install
CMD ["npm", "start"]
