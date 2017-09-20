import os

#from log import *
from pyutils.Log import Log

l = Log('a')
l.LogInfo('test')
l.LogDebug('debug')
print os.environ.get('KEY_THAT_MIGHT_EXIST')
