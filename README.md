# Object Detection App

## Create Environment using Conda

```bash
$ # create detectron_cpu conda environment
$ conda env create --file environments/cpu_environment.yml
$ conda activate detectron_cpu

$ # create detectron_gpu conda environment
$ conda env create --file environments/gpu_environment.yml
$ conda activate detectron_gpu
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
