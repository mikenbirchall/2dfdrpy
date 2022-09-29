def tdfio_open (filename,mode='update'):
    tid = fits.open(filename,mode=mode)
    return tid
