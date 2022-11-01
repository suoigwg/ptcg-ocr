import sqlite3
import time

import sql


class Connection:
    def __init__(self):
        self.DB_NAME = 'ptcg-code.db'
        self.con = sqlite3.connect(self.DB_NAME)
        self.execute(sql.CREATE_TABLE_CODE)
        self.execute(sql.CREATE_TABLE_VIDEO)

    def execute(self, query):
        cursor = self.con.execute(query)
        # for row in cursor:

    def insert_new_code(self, code, video, redeem=False, timestamp=str(time.time())):
        query = sql.INSERT_CODE.format(code, redeem, timestamp, video)
        self.con.execute(sql.INSERT_CODE.format(code, redeem, timestamp, video))
        self.con.commit()

    def insert_new_video(self, name, url, timestamp=str(time.time())):
        self.con.execute(sql.INSERT_VIDEO.format(name, url, timestamp))
        self.con.commit()
