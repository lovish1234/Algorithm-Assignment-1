import atexit
from time import clock

def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % \
        reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],
            [(t*1000,),1000,60,60])

line = "*"*100
def log(s, elapsed=None):
    print line
    if s!="":
        print s
    if elapsed:
        print "Total Time taken by programme :", elapsed
    print line
def endlog():
    end = clock()
    elapsed = end-start
    log("", secondsToStr(elapsed))

def now():
    return secondsToStr(clock())

start = clock()
atexit.register(endlog)
log("Start Program with Linked List as Data Structure")
