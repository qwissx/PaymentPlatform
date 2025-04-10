from uuid import UUID

from sqlalchemy import delete, insert, select, func, update
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    model = None

    @classmethod
    async def add(cls, session: AsyncSession, **data):
        query = insert(cls.model).values(**data)
        await session.execute(query)

    @classmethod
    async def get(cls, session: AsyncSession, **filter_by):
        query = select(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def rem(cls, session: AsyncSession, **filter_by) -> None:
        query = delete(cls.model).filter_by(**filter_by)
        await session.execute(query)

    @classmethod
    async def count(cls, session: AsyncSession, **filter_by) -> int:
        query = select(func.count()).select_from(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalar_one()

    @classmethod
    async def update(cls, session: AsyncSession, id: UUID, **values) -> None:
        query = (
            update(cls.model)
            .where(cls.model.id==id)
            .values(**values)
        )
        await session.execute(query)
