import numpy as np

try:
	a = np.load('respuestas.npy',allow_pickle='TRUE').tolist()
#	a = np.load('estados.npy',allow_pickle='TRUE').tolist()
	if(a):
		print(a)
	else: print('log vacío')
except:
	print('No existe log')

