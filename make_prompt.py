import json
import glob
import pandas as pd

infos = glob.glob('/home/data/aigc/*.json')

from collections import ChainMap
import os

infos = [json.load(open(each, 'r')) for each in infos]

merged_dict = dict(ChainMap(*infos))
    

file_name = list(merged_dict.keys())
texts = list(merged_dict.values())


df = pd.DataFrame(data={'file_name':file_name, 'texts':texts})

images = os.listdir('/home/data/aigc/images')

df = df[df['file_name'].isin(images)]


df.to_csv('/home/data/aigc/images/metadata.csv',index=False)

import ipdb;ipdb.set_trace()