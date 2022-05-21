FROM nginx:latest AS build

FROM build AS development

COPY ./index.html /usr/share/nginx/html/index.html

# FROM build AS production