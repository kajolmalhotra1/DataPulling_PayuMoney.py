import time
from celery import Task
from celery.exceptions import SoftTimeLimitExceeded
from celeryapp import app   # imports the app instance from the celery app module to define the pulling tasks and configure the worker.
#from logs import Logger

ClassPulling = {"Orders":'Orders'}

class MyTask(Task):
    abstract = True

    def __call__(self, *args, **kwargs):
        try:
            return super().__call__(*args, **kwargs)
        except SoftTimeLimitExceeded:
            # Handle soft time limit exceeded here
            pass
        except Exception as exc:
            # Handle other exceptions here
            pass

@app.task(base=MyTask, queue='pulling_queue')
def fetch_orders(batch_size):
    # Simulate fetching orders from an external data source
    time.sleep(5)

    # Generate a list of mock order data
    orders = [{'id': i, 'status': 'new'} for i in range(batch_size)]

    # Process each order in the batch
    for order in orders:
        process_order.delay(order)

    return f"Fetched {len(orders)} orders."

@app.task(base=MyTask, queue='processing_queue')
def process_order(order):
    # Simulate processing an individual order
    time.sleep(1)

    # Update the status of the order
    order['status'] = 'processed'

    return f"Processed order {order['id']}."

if __name__ == '__main__':
    # Start a worker to process tasks
    app.worker_main(arg=['worker', '-Q', 'pulling_queue,processing_queue'])

@app.task(base=MyTask, queue='eretail_pulling_testing')
def vinreco_works(message):
    try:   
        return_message = ClassPulling[message['operation']](message).pulling_factory()
        return return_message
    except SoftTimeLimitExceeded:
        Logger('vinreco_works').info("soft limit exceeded")
    except Exception as err:
        print(err)
        exception_message = str(err)
        exception_type, _, exception_traceback = sys.exc_info()
        filename = os.path.split(exception_traceback.tb_frame.f_code.co_filename)[1]
        Logger('vinreco_works').error(
            f"{exception_message} {exception_type} {filename}, Line {exception_traceback.tb_lineno}")






