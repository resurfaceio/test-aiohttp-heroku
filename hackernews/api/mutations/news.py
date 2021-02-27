import datetime

import graphene
from graphql import ResolveInfo
from hackernews.api.models.news import News
from hackernews.news.db_utils import create_news


class CreateNews(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True)

    news = graphene.Field(News)

    async def mutate(self, info: ResolveInfo, title: str, body: str):
        app = info.context["request"].app
        async with app["db"].acquire() as conn:
            news_id = await create_news(conn, title, body)

        return CreateNews(news=News(news_id, title, body))
