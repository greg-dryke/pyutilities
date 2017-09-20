import datetime
import os
import os.path


log_file = open('/var/log/standard.log', 'a')

class Log:
    
    def __init__(self,filePath):
        global log_file
        log_file = open(filePath, 'a')
    


    def LogMsg(self,msg, level):
        curTime = str(datetime.datetime.now())
        full_msg = '[{0} {1}] {2}'.format(level, curTime, msg)
        print(full_msg)
        log_file.write(full_msg+'\n')
        log_file.flush()
        os.fsync(log_file)
    
    def LogDebug(self,msg):
        trace = os.environ.get('PYUTILS_DEBUG')
        if trace is not None:
            self.LogMsg(msg, 'Debug')

    def LogInfo(self,msg):
        self.LogMsg(msg, 'Info')
    
    def LogWarning(self,msg):
        self.LogMsg(msg, 'Warning')
    
    def LogTraceback(self,ex, ex_traceback=None):
        traceBack = [ line.rstrip('\n') for line in
                    traceback.format_exception(ex.__class__, ex, ex_traceback)]
        self.LogError(traceBack)
    
    # Just for Adafruit right now?
    def LogError(self,msg):
        self.LogMsg(msg, 'Error')

    def FlushLog(self):
        log_file.flush()
        os.fsync(log_file)
