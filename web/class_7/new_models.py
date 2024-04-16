from sqlalchemy import create_engine, Integer, String, ForeignKey, select, Text, and_, desc, func
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship

engine = create_engine('sqlite:///:memory:', echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String)


class Post(Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[str] = mapped_column('user_id', Integer, ForeignKey('users.id'))
    user: Mapped['User'] = relationship(User)


Base.metadata.create_all(engine)


if __name__ == '__main__':
    names = ['Crystal Najera', 'Shaun Beck', 'Kathrin Reinhardt']
    for name in names:
        user = User(fullname=name)
        session.add(user)
    session.commit()

    # -
    stmt = select(User)
    result = session.execute(stmt)
    for user in result.scalars():
        print(user.id, user.fullname)

    # -
    stmt = select(User.id, User.fullname)
    result = session.execute(stmt)
    users = []
    for row in result:
        print(row)
        users.append(row)

    # -
    stmt = select(User).where(User.fullname == "Shaun Beck")
    result = session.execute(stmt).scalar_one()
    print(result.id, result.fullname)

    # -
    stmt = select(User).where(User.fullname.like("%ha%"))
    result = session.execute(stmt)
    for user in result.scalars().all():
        print(user.id, user.fullname)

    # -
    stmt = select(User).where(and_(User.fullname.like("%ha%"), User.fullname != 'Shaun Beck'))
    result = session.execute(stmt)
    for user in result.scalars():
        print(user.id, user.fullname)

    # -
    stmt = select(User).where(User.fullname.like("%ha%")).where(User.fullname != 'Shaun Beck')
    result = session.execute(stmt)
    for user in result.scalars().all():
        print(user.id, user.fullname)

    # -
    stmt = select(User).order_by(User.fullname)
    result = session.execute(stmt)
    for user in result.scalars():
        print(user.id, user.fullname)

    # -
    stmt = select(User).order_by(desc(User.fullname))
    result = session.execute(stmt)
    for user in result.scalars():
        print(user.id, user.fullname)
