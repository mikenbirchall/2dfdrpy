import tdfio
from tdfio import *
import shutil

#Create a copy into the tmp directory
source_filename = 'data_files/ccd_1_ref.fits'
target_filename = 'tmp_dir/copy.fits'
shutil.copy(source_filename,target_filename)

# Now try to write image data
fits_image_filename =target_filename

tid=tdfio_open(fits_image_filename,mode='update')

imgA=tdfio_image_read(tid)
varA=tdfio_variance_read(tid)
size1,size2=tdfio_getsize(tid)
#size1=sizes[0]
print("SIZE=", size1, size2)
for i in range(size1):
    for j in range(size2):
        imgA[i][j]=imgA[i][j]+100.0
        varA[i][j]=varA[i][j]+100.0
tdfio_image_write(tid,imgA)
tdfio_variance_write(tid,varA)
tdfio_close(tid)
