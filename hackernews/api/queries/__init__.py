# from graphene.relay import Node
from hackernews.api.queries.news import NewsAllQuery, NewsQuery


class Query(NewsQuery, NewsAllQuery):
    """
    The main GraphQL query point.
    """

    # node = Node.Field()
