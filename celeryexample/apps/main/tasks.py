from celeryexample import celery_app as app
from time import sleep


@app.task
def add(a, b):
    return a + b


@app.task
def xsum(iterable):
    return sum(iterable)


@app.task
def long_add(a, b):
    sleep(20)
    return a + b
