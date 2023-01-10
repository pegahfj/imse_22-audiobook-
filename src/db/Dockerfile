# pull official base image
FROM postgres:14-alpine

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d


# COPY data /var/lib/postgresql/data/

# docker cp /Users/pegah/Desktop/IMSE/submissions-22/M2/app/Docs/authors.csv 16f7351d971e:/var/lib/postgresql/data
