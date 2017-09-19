from lazydb import LazyDB

class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print('Called __getattr__ (%s)' %name)
        return super().__getattr__(name)
