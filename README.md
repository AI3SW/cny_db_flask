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

## Configuration

There are two configuration files:

* [`config.py`](./config.py)
  * Config file for non-sensitive and default variables
  * This file will be included in the repository when cloned
* `instance/config.py`
  * Config file for instance specific variables or variables that contain sensitive information
  * This file will __NOT__ be included in the repository when cloned, so you will have to create this file
  * Variables declared in `instance/config.py` will override those in `default_config.py`
  * Current variables:
    * `SQLALCHEMY_DATABASE_URI`
        * connect to `staging_ai_3` db for testing purposes
    * `SECRET_KEY`
        * Generate this yourself: [Official Flask documentation on generating a secret key](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY)

## Docker

### Build and Run Flask App using Docker

* Current image is only CPU compatible
* Add `instance/config` file
* Build and Run Image

```bash
$ docker build -t chinese_words -f DockerFile .
$ docker run -d --rm -p 5000:5000 chinese_words

$ # tear down container
$ docker stop chinese_words
```
