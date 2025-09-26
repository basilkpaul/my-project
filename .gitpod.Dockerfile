# Start from Gitpod full workspace image
FROM gitpod/workspace-full

# Install Docker and docker-compose
USER root
RUN apt-get update && \
    apt-get install -y docker.io docker-compose && \
    rm -rf /var/lib/apt/lists/*

# Add current user to docker group
RUN usermod -aG docker gitpod

USER gitpod
