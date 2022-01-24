import time

from celery import shared_task


@shared_task(bind =True)
def create_task(task_type):
    for i in range(1,10):
        print(i)
    time.sleep(int(task_type) * 10)
    
    return True