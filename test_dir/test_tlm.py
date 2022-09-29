import tdfio
from tdfio import *
import shutil

#Create a copy into the tmp directory
source_filename = 'data_files/21apr20006tlm.fits'
target_filename = 'tmp_dir/tlm.fits'
shutil.copy(source_filename,target_filename)

# Now try to write image data
fits_image_filename =target_filename

tid=tdfio_open(fits_image_filename,mode='update')

tlmA=tdfio_tlmap_read(tid)
size1,size2=tdfio_getsize(tid)
#size1=sizes[0]
print("SIZE=", size1, size2)
for i in range(size1):
    for j in range(size2):
        tlmA[i][j]=tlmA[i][j]+100.0
tdfio_tlmap_write(tid,tlmA)

tdfio_close(tid)
