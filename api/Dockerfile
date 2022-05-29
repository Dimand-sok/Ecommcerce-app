FROM python:3.9 AS build

WORKDIR /api

COPY . /api

RUN pip install -r requirements.txt

FROM build AS development
EXPOSE 5000

RUN pip install debugpy

#run in module debugpy listen on localhost port 5678 wait for debug client start then run run.py
ENTRYPOINT [ "python","-m","debugpy","--listen","0.0.0.0:5678","--wait-for-client", "run.py" ]

FROM build AS production
ENTRYPOINT [ "python", "run.py" ]