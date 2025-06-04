import os
import psycopg2
from dotenv import load_dotenv
import hashlib

load_dotenv()


class Database:
    def __init__(self):
        self.conn = None
        self.connect()

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=os.getenv('DB_HOST'),
                port=os.getenv('DB_PORT'),
                dbname=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD')
            )
            self._init_db()
            print(" Connection to database successful!")
        except Exception as e:
            print(f" Error connection: {e}")

    def _init_db(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            self.conn.commit()

    def create_user(self, username, password):
        try:
            with self.conn.cursor() as cur:
                # Проверка на занятость логина
                cur.execute("SELECT id FROM users WHERE username = %s", (username,))
                if cur.fetchone():
                    return False  # Логин занят

                password_hash = hashlib.sha256(password.encode()).hexdigest()

                print(f"[INFO] Creating user '{username}' with password: {password}")

                # Сохраняем в БД
                cur.execute(
                    "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
                    (username, password_hash)
                )
                self.conn.commit()
                return True
        except Exception as e:
            print(f"Registration error: {e}")
            return False

    def authenticate_user(self, username, password):
        #Проверяем логин и пароль
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    "SELECT password_hash FROM users WHERE username = %s",
                    (username,)
                )
                result = cur.fetchone()
                if result:
                    # Сравниваем хеши паролей
                    return result[0] == hashlib.sha256(password.encode()).hexdigest()
                return False
        except Exception as e:
            print(f"Entry error: {e}")
            return False

    def close(self):
        if self.conn:
            self.conn.close()