FROM python:3.12-slim
RUN mkdir /code
WORKDIR /code

RUN apt-get update && apt-get install -y gettext libgettextpo-dev vim

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./develop/requirements* /code/
COPY ./develop/app-entrypoint.sh /

RUN python -m pip install --upgrade pip && pip install -r requirements.txt
RUN chmod +x /app-entrypoint.sh

ENTRYPOINT ["/app-entrypoint.sh"]
