FROM python:3.9 AS build

WORKDIR /api

COPY . /api

RUN pip install -r requirements.txt

FROM build AS development

RUN pip install debugpy

ENTRYPOINT [ "python", "run.py" ]

FROM build AS production