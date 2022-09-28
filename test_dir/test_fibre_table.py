import tdfio
from tdfio import *

fits_image_filename = 'data_files/21apr20006im.fits'
tid=tdfio_open(fits_image_filename)
file_class=tdfio_getclass(tid)
print("Read class=", file_class)
fibTypes=tdfio_fibres_read_types(tid)
print ("FIB TYPES")
print(fibTypes.size)
print(fibTypes)

tdfio_close(tid)
