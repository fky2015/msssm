from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sys

for filename in sys.argv[1:]:

    try:
        img = np.array(Image.open(filename))
    except:
        print('error happen when open file')
        exit()
    
    conf_list = [ [0,0,0,0], [0,0,0,255],[255,255,255,255],[255,0,0,255],[0,255,0,255],[0,0,255,255],[255,0,255,255] ]
    
    rows,cols,dims = img.shape
    
    def find_nearist(pix:list):
        res_array = list(map(lambda x: np.linalg.norm(np.array(x) - pix), conf_list))
        return conf_list[res_array.index(min(res_array))]
        # return [255,255,255,255]
    
    for i in range(rows):
        for j in range(cols):
            if list(img[i,j]) not in conf_list:
                img[i,j] = find_nearist(img[i,j])
    
    im = Image.fromarray(img)
    
    im.save(filename)
    
