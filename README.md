# Chinese Words

Simple flask app to serve chinese words from database for CNY 2021.

## Create Environment using Conda

```bash
$ # create conda environment
$ conda env create --file environments/environment.yml
$ conda activate chinese_words
```

## Run PostgreSQL using Docker

```bash
$ # Running db wih volume mounted for staging purposes
$ docker run --rm -p 5432:5432 --name postgres \
    -v /data/kianboon/staging:/var/lib/postgresql/data \
    -e POSTGRES_PASSWORD=password -d postgres
$ docker stop postgres
```

## Create Database and Tables

### 1. Using `psql`

```bash
$ PGPASSWORD=password psql -U postgres -h localhost -f database/create_db.sql
$ PGPASSWORD=password psql -U postgres -h localhost -d ai_3_staging -f database/create_table.sql
$ PGPASSWORD=password psql -U postgres -h localhost -d ai_3 -f database/create_table.sql
```

### 2. Using interactive shell into the container

```bash
$ docker exec -it postgres /bin/bash
root@container:/$ apt-get update && apt-get install git
root@container:/$ git clone https://github.com/kw01sg/ai_toolbox_db.git
root@container:/$ PGPASSWORD=password psql -U postgres -h localhost -f chinese_words/scripts/create_db.sql
root@container:/$ PGPASSWORD=password psql -U postgres -h localhost -d ai_3_staging -f chinese_words/scripts/create_tables.sql
root@container:/$ PGPASSWORD=password psql -U postgres -h localhost -d ai_3 -f chinese_words/scripts/create_tables.sql
```

## Seed Staging Database

```bash
$ # from project directory
$ python -m database.seed_db
```

## Serve Flask App

### Using Flask Built-in Development Server

```bash
$ export FLASK_APP=flask_app
$ export FLASK_ENV=development
$ flask run --host=0.0.0.0 --port=5000
```

## Docker

### Build and Run Flask App using Docker

* Current image is only CPU compatible
* Update dockerfile, replacing `<app_name>`
* Add `instance/config` file
* Build and Run Image

```bash
$ docker build -t <app_name> -f DockerFile .
$ nvidia-docker run -d --rm -p 5000:5000 <app_name>

$ # tear down container
$ docker stop <app_name>
```
