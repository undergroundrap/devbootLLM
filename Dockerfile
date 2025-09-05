FROM node:18

# Install required runtimes (JDK + Python3), then clean up apt cache to reduce surface
RUN set -eux; \
    apt-get update; \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        openjdk-17-jdk \
        python3 \
        ca-certificates; \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy dependency manifests first for better caching
COPY package*.json ./

# Install production dependencies
ENV NODE_ENV=production
RUN npm ci --omit=dev || npm install --only=production

# Copy the application code
COPY . .

# Drop root privileges for runtime
USER node

# Expose port
EXPOSE 3000

# Run the app
CMD ["node", "server.js"]
