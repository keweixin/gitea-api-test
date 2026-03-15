import pymysql

from common.config import Config


class MySQLHelper:
    def __init__(self):
        self.connection = None

    def connect(self):
        self.connection = pymysql.connect(
            host=Config.MYSQL_HOST,
            port=Config.MYSQL_PORT,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
        return self.connection

    def query_one(self, sql, params=None):
        if self.connection is None:
            self.connect()

        with self.connection.cursor() as cursor:
            cursor.execute(sql, params or ())
            return cursor.fetchone()

    def query_all(self, sql, params=None):
        if self.connection is None:
            self.connect()

        with self.connection.cursor() as cursor:
            cursor.execute(sql, params or ())
            return cursor.fetchall()

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
