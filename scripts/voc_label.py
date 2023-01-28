import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

#sets=[('2012', 'train'), ('2012', 'val'), ('2007', 'train'), ('2007', 'val'), ('2007', 'test')]
sets=[('2012', 'test')]
#classes = ["eyebrow", "ear", "glasses", "mask","hat"]
classes = ["person", "phone"]


basepath ="E:/0/test1000"

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(year, image_id):
    in_file = open(basepath+'/annotations/%s.xml'%(image_id))#xml文件
    out_file = open(basepath+'/labels/%s.txt'%(image_id), 'w')#txt文件
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            print(image_id)
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()

for year, image_set in sets:
    if not os.path.exists(basepath+'/labels/'):#txt生成目录
        os.makedirs(basepath+'/labels/')
    image_ids = open(basepath+'/%s.txt'%(image_set)).read().strip().split()#上面txt文件
    list_file = open('%s_%s.txt'%(year, image_set), 'w')#文件列表
    for image_id in image_ids:
        list_file.write(basepath+'/jpg/%s.jpg\n'%(image_id))
        convert_annotation(year, image_id)
    list_file.close()

#os.system("cat 2007_train.txt 2007_val.txt 2012_train.txt 2012_val.txt > train.txt")
#os.system("cat 2007_train.txt 2007_val.txt 2007_test.txt 2012_train.txt 2012_val.txt > train.all.txt")

