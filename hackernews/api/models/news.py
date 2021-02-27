import graphene
from aiopg.sa.result import RowProxy
from graphql import ResolveInfo


class News(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    body = graphene.String()
