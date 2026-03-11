import os
import sqlite3

DATABASE_URL = os.environ.get("DATABASE_URL")

try:
    if DATABASE_URL:
        import psycopg2
        from psycopg2.extras import RealDictCursor
        IntegrityError = psycopg2.errors.UniqueViolation
    else:
        IntegrityError = sqlite3.IntegrityError
except ImportError:
    IntegrityError = sqlite3.IntegrityError
    
class CursorWrapper:
    def __init__(self, cursor, is_postgres):
        self._cursor = cursor
        self._is_postgres = is_postgres
        self.lastrowid = None
        self.rowcount = -1

    def execute(self, query, params=None):
        if self._is_postgres:
            query = query.replace("?", "%s")
            is_insert = query.strip().upper().startswith("INSERT")
            if is_insert and "RETURNING id" not in query.upper():
                query += " RETURNING id"
                
            try:
                self._cursor.execute(query, params or ())
                if is_insert:
                    row = self._cursor.fetchone()
                    if row and 'id' in row:
                        self.lastrowid = row['id']
                    elif row:
                        self.lastrowid = list(row.values())[0] if isinstance(row, dict) else row[0]
                self.rowcount = self._cursor.rowcount
            except Exception as e:
                self._cursor.connection.rollback()
                raise e
        else:
            self._cursor.execute(query, params or ())
            self.lastrowid = self._cursor.lastrowid
            self.rowcount = self._cursor.rowcount
        return self

    def fetchone(self):
        return self._cursor.fetchone()

    def fetchall(self):
        return self._cursor.fetchall()

    def executescript(self, script):
        if self._is_postgres:
            script = script.replace("AUTOINCREMENT", "SERIAL")
            script = script.replace("INTEGER PRIMARY KEY SERIAL", "SERIAL PRIMARY KEY")
            script = script.replace("BOOLEAN DEFAULT 0", "BOOLEAN DEFAULT FALSE")
            script = script.replace("BOOLEAN DEFAULT 1", "BOOLEAN DEFAULT TRUE")
            # SQLite DATE, TIMESTAMP defaults etc usually work fine in Postgres
            self._cursor.execute(script)
        else:
            self._cursor.executescript(script)
            
    def __iter__(self):
        return iter(self._cursor)

class ConnectionWrapper:
    def __init__(self, conn, is_postgres):
        self._conn = conn
        self._is_postgres = is_postgres

    def cursor(self):
        if self._is_postgres:
            cur = self._conn.cursor(cursor_factory=RealDictCursor)
        else:
            cur = self._conn.cursor()
        return CursorWrapper(cur, self._is_postgres)

    def execute(self, query, params=None):
        cur = self.cursor()
        return cur.execute(query, params)

    def executescript(self, script):
        cur = self.cursor()
        cur.executescript(script)
        return cur

    def commit(self):
        self._conn.commit()

    def rollback(self):
        self._conn.rollback()

    def close(self):
        self._conn.close()

def get_connection(db_path):
    if DATABASE_URL:
        # Connect to Postgres
        import psycopg2
        conn = psycopg2.connect(DATABASE_URL)
        return ConnectionWrapper(conn, True)
    else:
        # Connect to SQLite
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return ConnectionWrapper(conn, False)
