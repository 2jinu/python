import os, tqdm
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array

base_dir        = os.path.join(os.getcwd(),'python')
image_dir       = os.path.join(base_dir, 'apple')
output_dir      = os.path.join(base_dir, 'dataset')
width, height   = 32, 32
dataset         = []
datagen         = ImageDataGenerator(rotation_range = 20, # 이미지 회전
                                    zoom_range = [0.5, 1.0],
                                    width_shift_range=0.1, #이미지 좌우로 움직이기
                                    height_shift_range=0.1, #이미지 위아래로 움직이기
                                    fill_mode='nearest' #빈값 채우기
                                    )

for img_file in tqdm.tqdm(os.listdir(image_dir)):
    img             = img_to_array(Image.open(os.path.join(image_dir, img_file)).resize((width, height)).convert('RGB'))
    expanded_img    = np.expand_dims(img, 0)
    datagen.fit(expanded_img)
    i   = 0
    for x in datagen.flow(expanded_img, save_to_dir=output_dir, save_prefix=1, save_format='jpg'):
        i+=1
        if i == 20: break