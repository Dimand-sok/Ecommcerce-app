FROM python:3.8 AS build

RUN pip install -r requirements.txt

FROM build AS development
RUN pip install debugpy

FROM build AS production