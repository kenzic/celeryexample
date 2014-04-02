# Example Celery Project

## Install

* `git clone git@github.com:kenzic/celeryexample.git`
* `cd celeryexample`
* `pip install -r requirements.txt`
* Setup RabbitMQ

## Start Celery Worker
* Make sure rabbit-serve is running
* `celery -A celeryexample worker`

## Run Task

```python
>>> from celeryexample.apps.main.tasks import add
>>> r = add.delay(1, 2)
```

## Setup RabbitMQ

For a full guide to setting up RabbitMQ checkout the [Installation](http://www.rabbitmq.com/download.html) page.

### Setup RabbitMQ v_host

* `rabbitmqctl add_vhost example/`
* `rabbitmqctl add_user example example`
* `rabbitmqctl set_permissions -p example/ example ".*" ".*" ".*"`
