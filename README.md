# Flask App Template

Boilerplate code for a flask app to wrap around a Machine Learning Model.

## Simple How to Use

* Clone this repo
* Update repository remote:

```bash
$ git remote set-url origin <newurl>
```

* Create your own model by extending from `BaseModel` in [declarations.py](flask_app/model/declarations.py)
* update `init_model_store` function in [`model` package](flask_app/model/__init__.py)
* update endpoints in [views.py](flask_app/views.py)

## Create Environment using Conda

```bash
$ # create conda environment
$ conda env create --file environments/environment.yml
$ conda activate <conda_env>
```

## Serve Flask App

### Using Flask Built-in Development Server

```bash
$ export FLASK_APP=flask_app
$ # export FLASK_ENV=development
$ flask run --host=0.0.0.0 --port=5000
```

## Docker

### Build and Run Flask App using Docker

* Current image is for GPU version of the app

```bash
$ docker build -t object-detection .
$ nvidia-docker run -d --rm -p 5000:5000 object-detection

$ # tear down container
$ docker stop object-detection
```
