from raiseExceptionClass import *

cb = CircuitBreaker(30)
cb.connect(10)
cb.connect(10)
cb.connect(10)
cb.connect(10)
cb.connect(-10)