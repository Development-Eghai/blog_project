FROM ubuntu:latest
LABEL authors="Thanesh"

FROM nginx:1.21

# Remove default Nginx config
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom Nginx config
COPY nginx.conf /etc/nginx/conf.d/
