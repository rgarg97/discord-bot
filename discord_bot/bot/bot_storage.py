import os
import sqlite3

_DB_NAME = "bot"
_TABLE_NAME = "searches"


class BotStorage:

    def __init__(self):
        self._db_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            f"{_DB_NAME}.db"
        )
        self.db_conn = None

    def __enter__(self):
        self.db_conn = sqlite3.connect(self._db_file)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db_conn.close()

    def save_keyword(self, user, keyword):
        self.db_conn.cursor().execute(
            f"INSERT INTO {_TABLE_NAME} (user, keyword) VALUES ({user}, '{keyword}');"
        )
        self.db_conn.commit()

    def get_matched_keywords(self, user, arg):
        cursor = self.db_conn.cursor().execute(
            f"SELECT DISTINCT keyword from {_TABLE_NAME} where user={user} and keyword LIKE '%{arg}%';"
        )
        return cursor.fetchall()


def initialize_schema():
    with BotStorage() as storage:
        storage.db_conn.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {_TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user INTEGER NOT NULL,
                keyword TEXT NOT NULL
            );
            """
        )
