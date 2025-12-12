# Stage 1: Build the Next.js application
FROM node:20-alpine AS builder

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application's code
COPY . .

# Build the Next.js application (creates 'out' folder for static export)
RUN npm run build

# Stage 2: Serve the static application
FROM node:20-alpine

# Set the working directory
WORKDIR /app

# Install serve globally for static file serving
RUN npm install -g serve

# Copy the static output from the builder stage
COPY --from=builder /app/out ./out

# Expose port 3000
EXPOSE 3000

# Serve the static files
CMD ["serve", "-s", "out", "-l", "3000"]
