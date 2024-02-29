from celery import Celery
import os

os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('Data-Pulling-PayUMoney', include=['payu_pulling'])  #Creates a celery application instance vinstore with include parameter set to ['Data_Pulling'] task should be included in this worker.
app.config_from_object("celeryconfig") #object=app and set the config settings of the worker
app.conf.update(
    result_expires=3600, # (1hour) task will expire after one hour instead of being saved indefinitely.
)

if __name__ == '__main__':
    app.Worker(optimization='fair', loglevel='INFO').start()