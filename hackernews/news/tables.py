import sqlalchemy as sa
from hackernews.migrations import metadata
from sqlalchemy.dialects import postgresql

news = sa.Table(
    "news",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True, index=True),
    sa.Column("title", sa.String(200), nullable=False),
    sa.Column("body", sa.String(500), nullable=False),
)
