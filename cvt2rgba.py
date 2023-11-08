import glob, os
from PIL import Image
from tqdm import tqdm

def cvt2RGBA(fp):
    # Open the image
    image = Image.open(fp)

    # Check if it's a palette image with transparency
    if image.mode == "P":
        # Convert it to RGBA
        image = image.convert("RGBA")

    image.save(fp)

images = glob.glob('/home/data/aigc/images/*.png')


err = []
for each in tqdm(images):
    image = Image.open(each)
    if image.mode == "P":
        err.append(each)

for each in tqdm(err):
    cvt2RGBA(each)

import ipdb;ipdb.set_trace()