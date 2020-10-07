FROM nginx:1.17.4-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
#RUN rm -rf /etc/nginx/certs && mkdir /etc/nginx/certs
#COPY cert/phoenix.crt /etc/nginx/certs/phoenix.crt
#COPY cert/phoenix.key /etc/nginx/certs/phoenix.key
