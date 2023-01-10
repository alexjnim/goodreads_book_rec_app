FROM nginx:1.13-alpine

COPY conf /etc/nginx/conf.d/default.conf.template

# nginx by default launches on port 80
CMD ["/bin/sh", "-c", "envsubst < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf; nginx -g 'daemon off;'"]