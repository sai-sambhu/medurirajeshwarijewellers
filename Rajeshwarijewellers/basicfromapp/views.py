from django.shortcuts import render
from django.http import HttpResponse


import os



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR=os.path.join(BASE_DIR,"basicfromapp")
STATIC_DIR=os.path.join(STATIC_DIR,"static")

NavComps = [i for i in os.listdir(STATIC_DIR)]
print(NavComps)


carousel = {}
for itemName in NavComps:
    print(itemName)
    itemFolder = os.path.join(STATIC_DIR, itemName)
    itemFolderImages = [itemName+"/"+i for i in os.listdir(itemFolder)]
    print(itemFolderImages)    
    carousel[itemName] = itemFolderImages


print(carousel)


def index(request):
    return render(request,'webpages/index.html',{"imageurl":"jam.JPG","NaviCompos":NavComps, "carouselItems" : carousel,"splitsd":"sai-reddy"})

