import numpy as np
import pydicom
import matplotlib.pyplot as plt

import time

for i in range(84):
    file_path=f'dicom\\CT_1.2.840.113619.2.278.3.2831258147.694.1627862774.358.{i+1}'
    ds=pydicom.dcmread(file_path,force=True)
    ds.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian
    if i == 0:
        data=np.array(ds.pixel_array)
        data = data.reshape(data.shape[0], data.shape[0], 1)
    else:
        array=np.array(ds.pixel_array)
        #array=array.reshape(array.shape[0],array.shape[0],1)
        data = np.insert(data,i,array,2)

print(data.shape)

for j in range(84):
    pic=data[:,:,j]
    plt.figure()
    plt.ion()# 打开交互模式
    plt.imshow(pic,cmap=plt.cm.bone)
    #plt.show()
    plt.pause(0.5)  # 该句显示图片0.5秒
    plt.ioff()  # 显示完后一定要配合使用plt.ioff()关闭交互模式，否则可能出奇怪的问题
    plt.clf()  # 清空图片
    plt.close()