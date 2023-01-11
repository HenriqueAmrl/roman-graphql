from graphql_server.flask import GraphQLView

from .schema import schema

graphql_view = GraphQLView.as_view(
    "graphql",
    schema=schema.graphql_schema,
    # Para ativar o playground
    graphiql=True,
)
