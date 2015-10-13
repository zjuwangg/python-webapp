import threading

__author__ = 'qiaoran'


# 数据库引擎对象:
class _Engine(object):
    def __init__(self, connect):
        self._connect = connect

    def connect(self):
        return self._connect()

engine = None


# 持有数据库连接的上下文对象:
class _DbCtx(threading.local):
    def __init__(self):
        self.connection = None
        self.transcations = 0

    def is_init(self):
        return self.connection is not None

    def init(self):
        self.connection = _LasyConnection()
        self.transcations = 0

    def cleanup(self):
        self.connection.cleanup()
        self.connection = None

    def cursor(self):
        return self.connection.cursor()

_db_ctx = _DbCtx()

