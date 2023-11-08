import os, json
import glob

with open('diffusers/examples/text_to_image/err_imgs.txt', 'r') as f:
    li = f.readlines()
    
li = [each.strip('\n') for each in li]


for each in li:
    if os.path.exists(each):
        os.remove(each)
        print(each + 'del done')
    # os.remove('/home/data/aigc/images/' + each)
    
    
imgs = glob.glob('/home/data/aigc/images/*')

import ipdb;ipdb.set_trace()