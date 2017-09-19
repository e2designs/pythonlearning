from modules.gate_logger import Logger

class lazysetup(object):
    def __init__(self):
        self.logger = Logger(__name__)
        self.maint_cli = 'maint_cli container'
        self.ff_gui = 'Firefox container'

    def __getattr__(self, name):
        """
        Function is only called if the attribute did not already exist
        """
        value = None
        self.logger.general('Initializing attribute:{0}'.format(name))
        if name == 'wls_client':
            value = 'Wireless client container'
        setattr(self, name, value)
        return value


class forcelazy(object):
    def __init__(self):
        self.logger = Logger(__name__)

    def __getattribute__(self, name):
        """
        Function is always called
        """
        print('\nAttribute:{0} was called'.format(name))
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            value = None
            setattr(self, name, value)
            return value
