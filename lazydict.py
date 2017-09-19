from modules.gate_logger import Logger

LOGGER = Logger(__name__)

class LazyStuff(object):
    def __init__(self):
        self.logger = LOGGER
        self.logger.general('LOCALS:{0}'.format(locals()))

    def __getattr__(self, name):
        value = None
        setattr(self, name, value)
        return value

    def printstuff(self):
        self.logger.general(self.__dict__)
