from task import celery_app
from app import flask_app

@celery_app.task
def foreach(x, y):
    with flask_app.app_context():
        total=0
        for i in range(x):
            for j in range(y):
                total+=i*j
        return total 
    

