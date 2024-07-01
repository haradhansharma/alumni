# nginx/Dockerfile

FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY ssl/ssl-cert.crt /etc/nginx/ssl-cert.crt
COPY ssl/ssl-cert.key /etc/nginx/ssl-cert.key

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]