import tdfio
from tdfio import *

fits_image_filename = 'ccd_1_ref.fits'
tid=tdfio_open(fits_image_filename)
file_class=tdfio_getclass(tid)
print("Read class=", file_class)
kval=tdfio_kywd_read_char(tid,"CUNIS1")
print ("KVAL=", kval)
kval=tdfio_kywd_read_char(tid,"CUNIT1")
print ("KVAL=", kval)
imgA=tdfio_image_read(tid)
varA=tdfio_variance_read(tid)
size1,size2=tdfio_getsize(tid)
#size1=sizes[0]
print("SIZE=", size1, size2)

tdfio_close(tid)
