import numpy as np
from scipy.io import loadmat

for i in range(24):
	df  = loadmat('/home/eng/esrwck/transferlearning/code/DeepDG/Data/Lanzhou_ERP/' + str(i+30) + '/MDD/' + 'MDD' + str(i+1) + '.mat')['EEGdata']
	for j in range(480):
		with open('/home/eng/esrwck/transferlearning/code/DeepDG/Data/Lanzhou_ERP/' + str(i+30) + '/MDD/' + str(j) + '.npy', 'wb') as f:
			np.save(f, df[j, :])
			
 
