import pandas as pd
import os, json, shutil
from tqdm import tqdm

prefix = '/home/data/aigc/images/'


df = pd.read_csv('/home/data/aigc/images/metadata.csv')


samples = df.sample(2000)

fps = samples.file_name.tolist()
fps = [prefix + each for each in fps]

os.makedirs('/home/data/aigc/images_samples', exist_ok=True)
for each in tqdm(fps):
    shutil.copy(each, '/home/data/aigc/images_samples/'+each.split('/')[-1])

samples.to_csv('/home/data/aigc/images_samples/metadata.csv', index=False)


import ipdb;ipdb.set_trace()