import os
import random

trainval_percent = 1
train_percent =1#train
xmlfilepath = 'E:/0/test1000/annotations'#设置
txtsavepath = 'E:/0/test1000'#设置
total_xml = os.listdir(xmlfilepath)#所有xml文件

num = len(total_xml)#xml数量
list = range(num)
tv = int(num * trainval_percent)#train+val数量
tr = int(tv * train_percent)#train数量
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open(txtsavepath+'/trainval.txt', 'w')
ftest = open(txtsavepath+'/test.txt', 'w')
ftrain = open(txtsavepath+'/train.txt', 'w')
fval = open(txtsavepath+'/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)
print('生成完毕...')

#ftrainval.close()
ftrain.close()
#fval.close()
ftest.close()
