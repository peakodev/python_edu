from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine, async_sessionmaker

engine: AsyncEngine = create_async_engine('postgresql+asyncpg://user:password@host/database', echo=True)
AsyncDBSession = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async with AsyncDBSession() as session:
    result = await session.execute(select(User).where(User.name == "Alice"))
    user = result.scalars().first()
