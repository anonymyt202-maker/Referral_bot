import asyncio

from data.database import engine
from data.models import Base


async def create_tables():

    async with engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.create_all
        )

    print("Table yaratildi ✅")


asyncio.run(create_tables())
