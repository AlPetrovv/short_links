from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from config import settings


class DBHelper:
    """
    Database helper, this class is adapter for database
    """

    def __init__(
        self,
        db_url: str,
        echo: bool = False,
        echo_pool: bool = False,
        pool_size: int = 50,
        max_overflow: int = 10,
    ):
        self.engine = create_async_engine(
            url=db_url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )
        # skip auto flush, autocommit, expire_on_commit for async
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )


helper = DBHelper(
    db_url=settings.db.url,
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)
