from app import flask_app, flask_api, Resource
from task.for_task import foreach
from flask import request
from app.ext.db import engine, db_session
from sqlalchemy import insert, event
from app.models import Base, Account

Base.metadata.create_all(bind=engine)






@flask_api.route("/hello")
class Hello(Resource):
    @flask_api.doc(security="apikey")
    def get(self):
        if request.headers.get("X-API-KEY") != "apikey":
            return {"hello": "error"}, 403
        foreach.delay(100, 10)
        return {"hello": "done"}


@flask_app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    
    flask_app.run()
