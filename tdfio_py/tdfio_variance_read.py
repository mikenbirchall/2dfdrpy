def tdfio_variance_read(tid):
    idx=FindExtension(tid,"VARIANCE")
    imgA=tid[idx].data
    return imgA
