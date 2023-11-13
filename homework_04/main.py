"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from homework_04.view import create_users, create_posts
from jsonplaceholder_requests import fetch_users, fetch_posts
from models import User, Post, engine, Session, Base


async def set_data():
    try:
        async with Session() as session:
            users_data, posts_data = await asyncio.gather(
                fetch_users(),
                fetch_posts(),
            )

            await create_users(session=session, users_data=users_data)
            await create_posts(session=session, posts_data=posts_data)

    except Exception as e:
        print(f"Error in set_data: {e}")


async def create_tables():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        await engine.dispose()
    except Exception as e:
        print(f"Error in create_tables: {e}")


async def drop_tables():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
        await engine.dispose()

    except Exception as e:
        print(f"Error in drop_tables: {e}")


async def async_main():
    await drop_tables()
    await create_tables()
    await set_data()


def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()
