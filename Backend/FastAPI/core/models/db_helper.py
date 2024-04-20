from asyncio import current_task
from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)

from ..settings import settings


class DatabaseHelper:
    def __init__(
        self,
        url: str,
        echo: bool = False,
    ) -> None:
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scoped_session(
        self,
    ):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    # Session creates at every request
    # Session made with session factory
    async def session_dependency(
        self,
    ) -> AsyncGenerator[AsyncSession, Any]:
        async with self.session_factory() as session:
            yield session
            await session.close()

    # Session made with scoped session
    async def scoped_session_dependency(
        self,
    ) -> AsyncGenerator[async_scoped_session[AsyncSession], Any]:
        session = self.get_scoped_session()
        yield session
        await session.close()


db_helper = DatabaseHelper(
    url=settings.db.url,
    echo=settings.db.echo,
)

db_helper_sqlite = DatabaseHelper(
    url="sqlite+aiosqlite:///C:\\MySheat\\Coding\\Projects\\Plantique\\Backend\\FastAPI\\api_v1\\db_migration\\plantique.db",
)
