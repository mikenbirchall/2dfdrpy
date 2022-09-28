def tdfio_open (filename):
    tid = fits.open(filename)
    return tid

print ("tdfo_open loaded")
