def tdfio_getsize(tid):
    imgA = tid[0].data
    imgDims=imgA.shape
    size1=imgDims[0]
    size2=imgDims[1]
    return size1, size2
