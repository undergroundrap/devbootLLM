# Use an official Node.js runtime as a parent image
FROM node:18

# Install OpenJDK, which is required for Java
RUN apt-get update && apt-get install -y openjdk-17-jdk

# Install Python
RUN apt-get install -y python3

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install any needed packages
RUN npm install

# Copy the rest of the application's code
COPY . .

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Run the app when the container launches
CMD [ "node", "server.js" ]
