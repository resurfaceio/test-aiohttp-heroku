import graphene
from aiopg.sa.result import RowProxy
from graphql import ResolveInfo
from hackernews.api.models.news import News
from hackernews.news.db_utils import select_all_news, select_news_by_id


class NewsQuery(graphene.ObjectType):
    news = graphene.Field(
        News,
        pk=graphene.Argument(graphene.Int),
        description="A news with given id",
    )

    async def resolve_news(self, info: ResolveInfo, pk) -> RowProxy:
        app = info.context["request"].app
        async with app["db"].acquire() as conn:
            return await select_news_by_id(conn, pk)


class NewsAllQuery(graphene.ObjectType):
    newss = graphene.List(
        News,
        description="A news list",
    )

    async def resolve_newss(
        self,
        info: ResolveInfo,
    ) -> RowProxy:
        app = info.context["request"].app
        async with app["db"].acquire() as conn:
            return await select_all_news(
                conn,
            )
