from flask import Flask
from .graphql import graphql_view

def create_app(*args, **kwargs):
    app = Flask(__name__)
    app.add_url_rule("/graphql", methods=["GET", "POST"], view_func=graphql_view)
    return app
