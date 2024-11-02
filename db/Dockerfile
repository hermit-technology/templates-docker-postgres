FROM python:3.12 as requirements-stage

WORKDIR /tmp

COPY . /tmp/

RUN pip install jinja2==3.1.2
RUN python migrator.py -t migration.j2 -o /tmp/1_migration.sql -db hermit

FROM postgres:16.1

WORKDIR /pg

COPY  --from=requirements-stage /tmp/1_migration.sql /docker-entrypoint-initdb.d

RUN chmod a+r /docker-entrypoint-initdb.d/*

EXPOSE 5432