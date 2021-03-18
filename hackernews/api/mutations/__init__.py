import graphene
from hackernews.api.mutations.news import CreateNews


class Mutations(graphene.ObjectType):
    """
    All created mutations
    """

    add_news = CreateNews.Field(description="News for tech enthusiast hackers")
