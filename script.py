#%%
import PIL
from PIL import Image
import copy
# %%
img = Image.open('img-00001-00001.bmp')
# %%
img.mode 
# %%
img_copy = copy.deepcopy(img)
# %%
pixel_values = []
for x in range(img_copy.width):
    for y in range(img_copy.height):
        p = img_copy.getpixel((x,y))
        if p[0]!=p[1] and p[0]!=p[2]:
            pixel_values.append(p)
            img_copy.putpixel((x,y),(255,0,0))
        else:
            img_copy.putpixel((x,y),(0,0,0))
#now we just return the new image


set(pixel_values)
# %%
img_copy
# %%
