import time
import logging

def timeit(fn):
    def timed(*args, **kw):
        ts = time.time()
        result = fn(*args, **kw)
        te = time.time()
        logging.debug('%r  %2.2f ms' % (fn.__name__, (te - ts) * 1000))
        return result
        
    return timed
