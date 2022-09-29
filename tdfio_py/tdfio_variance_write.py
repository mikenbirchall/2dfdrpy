def tdfio_variance_write(tid,imgA):
    idx=FindExtension(tid,"VARIANCE")
    tid[idx].data=imgA
    return 0
