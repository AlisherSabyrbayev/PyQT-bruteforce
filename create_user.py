# from database import Database
# import hashlib
#
# db = Database()
# with db.conn.cursor() as cur:
#     cur.execute(
#         "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
#         ("admin", hashlib.sha256("admin123".encode()).hexdigest())
#     )
#     db.conn.commit()
# print(" User created")