FROM python:3.9 AS build
EXPOSE 5000

WORKDIR /api
COPY . /api

#required for substitub bash file
RUN apt-get update && apt-get install gettext -y

RUN pip install -r requirements.txt

# install required packages
RUN pip install --upgrade pip\
    && pip install -r requirements.txt\
    && mv entrypoint.sh /entrypoint.sh

FROM build AS development

RUN pip install debugpy

#go to and read from bash script
ENTRYPOINT [ "/entrypoint.sh" ]

FROM build AS production

ENTRYPOINT [ "python", "run.py" ]