import time, math, os, random, requests, json
from PIL import Image
from io import BytesIO


def get(image):
    
    w, h = image.size
    img = []
    for pixel in image.getdata():
        img.append(pixel)
    return(img,w,h)

def dapple(img):
    global add
    new = []
    count = 0
    for pixel in img:
        count += 2.5559
        white = sum(pixel[0:3])/(255*3)
        ran = 0.5+math.sin(count)/2
        if ran > white:
            new.append((0,0,0,255))
        else:
            new.append((255,255,255,255))
    return new

def drawnew(img,w,h):
    final = Image.new(mode='RGB', size=(w,h))
    final.putdata(img)
    final.show()

add = 2.5557
while True:
    #print(add)
    url = "https://picsum.photos/256"
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img,w,h=get(img)

    drawnew(dapple(img),w,h)
    add += 0.0001
    







arr = os.listdir()
val = 0
for file in arr:
    if ".jpg" in file:
        file = Image.open(file)
        

        img,w,h = get(file)
        for add in range(1):
            val += 0.002
            print(val)
            drawnew(dapple(img),w,h)