CREATE DATABASE postgres_db;
-- CREATE DATABASE api_test;
GRANT ALL PRIVILEGES ON DATABASE postgres_db TO postgres;
-- docker run --name postgres_db -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 postgres