from app import flask_app, flask_api, Resource
from task.for_task import foreach
from flask import request


@flask_api.route("/hello")
class Hello(Resource):
    @flask_api.doc(security="apikey")
    def get(self):
        if request.headers.get("X-API-KEY") != "apikey":
            return {"hello": "error"}, 403
        foreach.delay(100, 10)
        return {"hello": "done"}


if __name__ == "__main__":
    flask_app.run()
