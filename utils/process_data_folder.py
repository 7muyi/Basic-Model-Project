import os
import shutil


src_path = '../data/coil-20-proc'
base_train_path = '../data/train'
base_test_path = '../data/test'

file_list = os.listdir(src_path)
for file in file_list:
    src = os.path.join(src_path, file)

    num = file.split("__")[1].split(".")[0]
    
    if int(num) < 65: 
        dst_dir = os.path.join(base_train_path, file.split("__")[0])
    else:
        dst_dir = os.path.join(base_test_path, file.split("__")[0])
    dst = os.path.join(dst_dir, file)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    shutil.copy(src, dst)
    print('move %s -> %s'%(src, dst))