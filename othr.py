import sys
from main import sshconn, xlsx
import config
import random

if len(sys.argv)==1:
	print("need arg!")
	sys.exit()
if sys.argv[1] == '-d':
	name = str(random.random())[2:]+'.xlsx'
	o = [i.split("|") for i in sshconn(config.host, config.user, config.passwd, 22, config.other_q).split("\n")]
	xlsx(o,name)
else: print("need arg -d and then i do thet you write in config.sqll)")