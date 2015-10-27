from pystockfish import *
import time
import re

deep = Engine(depth=15,param={"Threads":8})

t1 = time.time()
deep.setposition(['e2e4'])
deep.bestmove()
print time.time()-t1
print re.search("cp (.+) nodes",deep.bestmove()['info']).groups()[0]

deep = Engine(depth=17,param={"Threads":8})

t1 = time.time()
deep.setposition(['e2e4'])
deep.bestmove()
print time.time()-t1
print re.search("cp (.+) nodes",deep.bestmove()['info']).groups()[0]


deep = Engine(depth=19,param={"Threads":8})

t1 = time.time()
deep.setposition(['e2e4'])
deep.bestmove()
print time.time()-t1
print re.search("cp (.+) nodes",deep.bestmove()['info']).groups()[0]


deep = Engine(depth=21,param={"Threads":8})

t1 = time.time()
deep.setposition(['e2e4'])
deep.bestmove()
print time.time()-t1
print re.search("cp (.+) nodes",deep.bestmove()['info']).groups()[0]
