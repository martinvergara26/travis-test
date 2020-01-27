FROM python:3.7.3-alpine3.10
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

WORKDIR /
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN rm requirements.txt

WORKDIR /app