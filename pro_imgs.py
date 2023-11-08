import base64
import os
import multiprocessing
from PIL import Image
from io import BytesIO
from tqdm import tqdm 
import json

def save_image_from_base64(base64_data, fp, output_folder):
    try:
        image_data = base64.b64decode(base64_data)
        image = Image.open(BytesIO(image_data))
        
        image.save(os.path.join(output_folder, fp), "PNG")
        print(f"Saved: {fp}")
    except Exception as e:
        print(f"Error saving image: {str(e)}")


def get_total(base64_image_list, fps):
    output_folder = "/home/data/aigc/images"
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 使用多进程保存Base64图像为PNG文件
    with multiprocessing.Pool(processes=24) as pool:  # 指定进程池的最大工作进程数
        pool.starmap(save_image_from_base64, [(data, fp, output_folder) for data, fp in zip(base64_image_list, fps)])

def pro_total(dataset_path='/home/data/aigc/data/part-00000'):
    base64_image_list = []
    captions = []
    with open(dataset_path, 'r') as file:
        for idx, line in enumerate(tqdm(file)):
            li = line.split('\t')
            base64_image_list.append(li[3])
            
            captions.append(li[4].strip('\n'))
    
    fps = [dataset_path.split('/')[-1] + '_' + str(i) + '.png' for i in range(len(base64_image_list))]
    image2caption = {k:v for k,v in zip(fps, captions)}
    
    get_total(base64_image_list, fps)
    
    with open('/home/data/aigc/{}.json'.format(dataset_path.split('/')[-1]), 'w') as f:
        json.dump(image2caption, f, indent='\t', ensure_ascii=False)
    
    
if __name__ == "__main__": 
    # dataset_paths = ['/home/data/aigc/data/part-0000{}'.format(i) for i in range(10)] + ['/home/data/aigc/data/part-000{}'.format(i) for i in range(10,20)]
    dataset_paths = ['/home/data/aigc/data/part-0000{}'.format(i) for i in range(1)]
    
    for each in dataset_paths:
        pro_total(each)