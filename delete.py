import os

for i in range(29):
	os.remove('/home/eng/esrwck/transferlearning/code/DeepDG/Data/Lanzhou_ERP/' + str(i+1) + '/HC/' + 'HC' + str(i+1) + '.mat')
	
for j in range(24):
	os.remove('/home/eng/esrwck/transferlearning/code/DeepDG/Data/Lanzhou_ERP/' + str(j+30) + '/MDD/' + 'MDD' + str(j+1) + '.mat')
