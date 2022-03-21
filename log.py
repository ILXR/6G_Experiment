from threading import Lock

from cv2 import log
logMutex = Lock()
LOG_SYNC = 1
LOG_ASYNC = 2

def logOutput(title, *strs):
    print("{:-^100}".format(title))
    for s in strs:
        print(s)
    # print("{:-^100}".format(""))

def LOGASYNC(title, *strs):
    logOutput(title, *strs)

def LOGLOCKSYNC(title="ANONYMOUS", *strs):
    logMutex.acquire()
    logOutput(title, *strs)
    logMutex.release()


def LOGSYNC(title="ANONYMOUS", *strs):
    LOGLOCKSYNC(title, *strs)

#默认SYNC LOG
def LOG(title, *strs, **dic):
    if(len(dic) > 0 and dic["log_sync"] == LOG_ASYNC):
        LOGASYNC(title, *strs)
    else:
        LOGSYNC(title, *strs)
