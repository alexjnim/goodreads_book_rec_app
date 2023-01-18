FROM nginx:1.13-alpine

COPY conf /etc/nginx/conf.d/default.conf.template

# ARG SERVER_NAME=localhost
# ARG FLASK_APP_SERVICE_HOST=app

# nginx by default launches on port 80
CMD ["/bin/sh", "-c", "envsubst < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf; nginx -g 'daemon off;'"]