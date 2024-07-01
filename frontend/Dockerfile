# Dockerfile for Vue.js Frontend

# Use official Node.js image as a parent image
FROM node:14-alpine

# Set work directory
WORKDIR /app

# Copy package.json and package-lock.json to work directory
COPY package*.json ./

# Install dependencies
RUN npm install

# # Install Vue CLI globally
# RUN npm install -g @vue/cli

# RUN npm install vue-router@next bootstrap@5.3.3 bootstrap-icons @popperjs/core@^2.11.8
# RUN npm install vuex@next axios

# Copy project files into the container
COPY . .

# Expose the port
EXPOSE 8080

# Command to run the application
CMD ["npm", "run", "serve"]


# # Dockerfile for Vue.js Frontend

# # Use official Node.js image as a parent image
# FROM node:14-alpine

# # Set work directory
# WORKDIR /app

# # Copy package.json and package-lock.json to work directory
# COPY package*.json ./

# # Install dependencies
# RUN npm install

# # Install Vue CLI globally
# RUN npm install -g @vue/cli

# RUN npm install vue-router@next bootstrap@5.3.3 @popperjs/core@^2.11.8
# RUN npm install vuex@next axios
# # Copy project files into the container
# COPY . .

# # Expose the port
# EXPOSE 8080

# # Command to run the application
# CMD ["npm", "run", "serve"]
