dataset='Lanzhou_ERP'
algorithm='Mixup' 
test_envs=2
gpu_ids=0
data_dir='/home/eng/esrwck/transferlearning/code/DeepDG/Data/Lanzhou_ERP/'
max_epoch=2
net='resnet18'
task='img_dg'
output='home/eng/esrwck/transferlearning/code/DeepDG/train_output/test'

i=0

# Mixup
python train.py --data_dir $data_dir --max_epoch $max_epoch --net $net --task $task --output $output \
--test_envs $test_envs --dataset $dataset --algorithm ${algorithm[i]}
