FROM nginx:1.17.4-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
RUN rm -rf /etc/nginx/certs && mkdir /etc/nginx/certs
COPY cert/morozovblog.crt /etc/nginx/certs/morozovblog.crt
COPY cert/morozovblog.crt /etc/nginx/certs/ca.crt
COPY cert/morozovblog.key /etc/nginx/certs/morozovblog.key
