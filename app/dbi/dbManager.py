import contextlib

import mysql.connector as _mysql


class DBInterface():

    def __init__(self, **config):
        self.config = config
        self.conn = self._connect()

    def _connect(self):
        return _mysql.connect(**self.config)

    def connection(self):
        return self.conn

    def cursor(self):
        return self.conn.cursor()

    def transaction(self):
        self.conn.start_transaction()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    @contextlib.contextmanager
    def __call__(self, *args, **kwargs):
        try:
            self.transaction()
            yield self.cursor()
        except Exception as e:
            raise e
        finally:
            self.commit()
            self.close()
