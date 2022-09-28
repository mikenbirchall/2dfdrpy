import tdfio
from tdfio import *
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)

fits_image_filename = 'ccd_1_ref.fits'
tid=tdfio_open(fits_image_filename)
file_class=tdfio_getclass(tid)
kval=tdfio_kywd_read_char(tid,"CUNIT1")
imgA=tdfio_image_read(tid)
varA=tdfio_variance_read(tid)
size1,size2=tdfio_getsize(tid)
tdfio_close(tid)

a = np.empty([size1, size2], dtype = float)
for i in range(size1):
    for j in range(size2):
        a[i,j]=1.0*imgA[i][j]



plt.figure()
plt.imshow(imgA,cmap='gray')
plt.show()
#plt.colourbar()
