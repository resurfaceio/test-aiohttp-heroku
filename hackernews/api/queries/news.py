import graphene
from aiopg.sa.result import RowProxy
from graphql import ResolveInfo
from hackernews.api.models.news import News
from hackernews.news.db_utils import select_all_news, select_news_by_id


class NewsQuery(graphene.ObjectType):
    news_by_id = graphene.Field(
        News,
        id=graphene.Argument(graphene.String),
        description="A news with given id",
    )

    async def resolve_news_by_id(self, info: ResolveInfo, id) -> RowProxy:
        app = info.context["request"].app
        async with app["db"].acquire() as conn:
            return await select_news_by_id(conn, int(id))


class NewsAllQuery(graphene.ObjectType):
    all_news = graphene.List(
        News,
        description="A news list",
    )

    async def resolve_all_news(
        self,
        info: ResolveInfo,
    ) -> RowProxy:
        app = info.context["request"].app
        async with app["db"].acquire() as conn:
            return await select_all_news(
                conn,
            )
