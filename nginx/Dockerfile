FROM nginx:latest AS build

FROM build AS development

RUN rm -rf /etc/nginx/nginx.conf
COPY ./nginx.conf /etc/nginx/

RUN cat /etc/nginx/nginx.conf
CMD [ "nginx", "-g" , "daemon off;" ]

# COPY ./index.html /usr/share/nginx/html/index.html

FROM build AS production