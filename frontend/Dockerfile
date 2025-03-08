# Use a Node.js image for building the app
FROM node:16 AS build

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json first to install dependencies early in the build process
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy all the files into the container
COPY . ./

# Build the frontend app (for React, for example)
RUN npm run build

# Serve the app using a lightweight web server (e.g., Nginx)
FROM nginx:alpine

# Copy the build output to the Nginx server directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose the port on which the app will run
EXPOSE 80

# Run Nginx
CMD ["nginx", "-g", "daemon off;"]
