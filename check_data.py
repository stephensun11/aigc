import json
import pandas as pd
from tqdm import tqdm

df = pd.read_csv('/home/data/aigc/images/metadata.csv')

from PIL import Image
import os, glob
imgs = glob.glob('/home/data/aigc/images/*')
imgs.pop()



from PIL import Image
import os

def is_image_corrupted(file_path):
    try:
        # 尝试打开图像文件
        img = Image.open(file_path)
        img.load()
        return False
    except:
        # 如果打开失败，说明文件损坏
        return True

# 替换 'image_list.txt' 为包含图像文件路径的文件

for idx,image_path in enumerate(tqdm(imgs)):
    if is_image_corrupted(image_path):
        print(f'损坏的图像文件: {image_path}')


# df['is_texts'] = df['texts'].apply(lambda x:type(x)==str)
# nan_data = df[df['is_texts']==False].file_name.tolist()
# with open('nan_data.txt', 'w') as f:
#     f.writelines([each + '\n' for each in nan_data])

# df = df[df['is_texts']==True]

import ipdb;ipdb.set_trace()
