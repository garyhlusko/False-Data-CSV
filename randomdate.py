import time
import random


def get_random_date():
	return time.strftime("%Y-%m-%d %H:%M:%S",(random.randrange(2000,2016),random.randrange(1,12),
	random.randrange(1,28),random.randrange(1,24),random.randrange(1,60),random.randrange(1,60),random.randrange(1,7),random.randrange(0,366),1))
	