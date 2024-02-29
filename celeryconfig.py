import os
# from dotenv import load_dotenv

# load_dotenv()

# sets the timezone used by the celery worker for scheduling tasks
timezone = 'Asia/Kolkata'

# option determines whether the Celery worker should use Coordinated Universal Time(UTC) for scheduling tasks, regardless of the local timezone.
enable_utc = False


# a dictionary of options that control how the Celery worker communicates with the message broker
broker_transport_options = {'region': 'ap-south-1', 'visibility_timeout': 43200, 'polling_interval': 0.3,
                            'wait_time_seconds': 20}

# a dictionary of settings for the result backend that Celery will use to store the results of completed tasks.
mongodb_backend_settings = {
    "taskmeta_collection": os.getenv('CELERY_TASKMETA_COLLECTION')
}

# This is the URL of the message broker that celery will use.
broker_url = 'redis://localhost:6379/0'

# This is the URL of the result backend that celery will use.
result_backend = 'mongodb://localhost:27017/'

# This sets the default queue that tasks will be assigned to if no specific queue is specified.
# task_default_queue = os.getenv('CELERY_DEFAULT_QUEUE')

# The worker processing the task will be killed and re-placed with a new one when this is exceeded
task_time_limit = 7200

# It will be raised when it is exceeded.The task can catch this to clean up before the hard limit comes.
task_soft_time_limit = 7200


result_backend_always_retry = True

# task_annotations option set the rate limit for the tasks.add task
task_annotations = {'tasks.add': {'rate_limit': '10/s'}}

# this ensures that the worker acks the task after it’s completed. If the worker crashes, it will just restart.
task_acks_late = True

# this ensures that the worker process can reserve at most one un-acked task at a time. If this is used with
# ACKS_LATE=False (the default), the worker will reserve a task as soon as it starts processing the first one.
worker_prefetch_multiplier = 1

# If you have it set to True, whenever you call delay or apply_async it will just run the task synchronously instead
# of delegating it to a worker. This simplifies debugging in your local environment and facilitates automated testing.
task_always_eager = False   #used for testing and debugging

