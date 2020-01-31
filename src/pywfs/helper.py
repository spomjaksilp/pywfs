"""
Helper
======

Module for functions that might be useful.
"""

import getpass, logging
from six import string_types, iteritems

#TODO this code is copied from qao.io.helper!
##############################################################
# extend logging mechanism
SPAM = 5
setattr(logging, 'SPAM', 5)
logging.addLevelName(levelName='SPAM', level=5)


class Logger(logging.Logger):
    def setLevel(self, level, globally=False):
        if isinstance(level, string_types):
            level = level.upper()
        try:
            level = int(level)
        except ValueError:
            pass
        logging.Logger.setLevel(self, level)
        if globally:
            for name, logger in iteritems(logging.root.manager.loggerDict):
                if not hasattr(logger, 'setLevel'):
                    continue
                logger.setLevel(level)

    def spam(self, msg, *args, **kwargs):
        self.log(SPAM, msg, *args, **kwargs)

logging.setLoggerClass(Logger)
format = "%(asctime)-15s %(name)s {user}: %(message)s".format(user=getpass.getuser())
logging.basicConfig(format=format)


log = logging.getLogger("Simtools")
log.setLevel(logging.SPAM)

