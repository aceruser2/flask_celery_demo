from app import flask_app, flask_api, Resource
from task.for_task import foreach
from flask import request
from app.ext.db import engine
from sqlalchemy import insert
from app.models import Base, Account, Rate
from flask_restx import reqparse, fields

Base.metadata.create_all(bind=engine)

ns = flask_api.namespace("todos", description="TODO operations")

rate = flask_api.model(
    "rate",
    {"rate": fields.Integer(required=True, description="The task unique identifier")},
)
# 表單用
# parser = reqparse.RequestParser()
# parser.add_argument("rate", type=int, help="Rate to charge for this resource")


@flask_api.route("/hello")
class Hello(Resource):
    @flask_api.doc(security="apikey")
    def get(self):
        if request.headers.get("X-API-KEY") != "apikey":
            return {"hello": "error"}, 403
        foreach.delay(100, 10)
        return {"hello": "done"}

    @ns.expect(rate)
    @ns.marshal_with(rate, code=201)
    def post(self):
        try:
            with engine.connect() as con:
                data = flask_api.payload
                # form data
                # args = parser.parse_args(strict=True)
                print(type(data["rate"]))
                stmt = insert(Rate).values(rate=int(data["rate"]))
                result = con.execute(stmt)
                print("数据插入成功！插入的记录ID为:", result.inserted_primary_key)
                con.commit()
                return {"rate": data["rate"]}
        except Exception as e:
            print(e)


if __name__ == "__main__":

    flask_app.run()
