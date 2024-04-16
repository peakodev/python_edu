from sqlalchemy import func # импортируем функцию func для агрегатных функций SQL

...

    stmt = select(User.id, User.fullname)
    result = session.execute(stmt)
    users = []
    for row in result:
        users.append(row)

    for user in users: # створюємо запис Post для кожного користувача
        post = Post(title=f'Title {user[1]}', body=f'Body post user {user[1]}', user_id=user[0])
        session.add(post)
    session.commit()
    
    stmt = (
        select(User.fullname, func.count(Post.id))  # створюємо об'єкт select із вибіркою імені користувача та кількості постів
        .join(Post)  # робимо join з моделлю Post за зовнішнім ключем user_id
        .group_by(User.fullname)  # групуємо результати за ім'ям користувача
    )
    results = session.execute(stmt).all()  # виконуємо запит і отримуємо список кортежів
    for name, count in results:  # перебираємо результати
        print(f"{name} has {count} posts")  # виводимо ім'я користувача та кількість постів
