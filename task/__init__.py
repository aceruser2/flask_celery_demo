from celery import Celery

celery_app = Celery(__name__,
                    backend = 'redis://localhost:6379/0',
                    broker = 'redis://localhost:6379/1',)

celery_app.conf['imports'] = ('task.for_task', )