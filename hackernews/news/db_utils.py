from aiopg.sa import SAConnection as SAConn
from aiopg.sa.result import RowProxy
from hackernews.news.tables import news


async def select_news_by_id(conn: SAConn, pk: int) -> RowProxy:
    cursor = await conn.execute(news.select().where(news.c.id == pk))
    item = await cursor.fetchone()
    return item


async def select_all_news(conn: SAConn) -> RowProxy:
    cursor = await conn.execute(news.select())
    items = await cursor.fetchall()
    return items


async def create_news(conn: SAConn, title: str, body: str) -> RowProxy:
    cursor = await conn.execute(
        news.insert().values(
            {
                "title": title,
                "body": body,
            }
        )
    )
    item = await cursor.fetchone()
    return item.id
