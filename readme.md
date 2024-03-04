pip install "celery[librabbitmq,redis,auth,msgpack]"


1. docker run -p 6379:6379 redis

2. python main.py 

3. celery -A task.for_task worker -l INFO