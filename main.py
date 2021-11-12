import numpy as np
import pydicom

for i in range(84):
    file_path=f'dicom\\CT_1.2.840.113619.2.278.3.2831258147.694.1627862774.358.{i+1}'
    ds=pydicom.dcmread(file_path,force=True)
    ds.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian
    if i == 0:
        data=np.array(ds.pixel_array)
        data = data.reshape(data.shape[0], data.shape[0], 1)
    else:
        array=np.array(ds.pixel_array)
        data = np.insert(data,i,array,2)

print(data.shape)
