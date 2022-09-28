import tdfio
from tdfio import *
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)

fits_image_filename = 'data_files/21apr20006im.fits'
tid=tdfio_open(fits_image_filename)
file_class=tdfio_getclass(tid)
kval=tdfio_kywd_read_char(tid,"CUNIT1")
imgA=tdfio_image_read(tid)
varA=tdfio_variance_read(tid)
size1,size2=tdfio_getsize(tid)
tdfio_close(tid)
fits_tlm_filename = 'data_files/21apr20006tlm.fits'
tid=tdfio_open(fits_tlm_filename)
tlmA=tdfio_tlmap_read(tid)
tdfio_close(tid)
fib=52 -1
tlmV=tlmA[fib]
print ("TLM VALS", tlmV[0], tlmV[1],tlmV[2],tlmV[3])
npix=tlmV.size
xV=np.empty([npix])
for idx in range(npix):
    xV[idx]=idx-0.5


#a = np.empty([size1, size2], dtype = float)
#for i in range(size1):
#    for j in range(size2):
#        a[i,j]=1.0*imgA[i][j]

perV=np.empty([100,1],dtype=float)
perc=np.array([50.0,50.0])
np.percentile(imgA, 1, axis=None, out=perV)
out=np.percentile(imgA,perc)
print("OUT=", out)
print(imgA[2974][63])
if (math.isnan(imgA[2974][63])):
    print("IS A NAN")
if (imgA[2974][63]==np.nan):
    print("IS STILL A NAN")
#print(perV)
#srtA=np.copy(imgA)
srtA=imgA.flatten()
n=size1*size2
print(srtA.shape, "n=",n)
print(srtA[0],srtA[1000])
srtA.sort()
print(srtA[0],srtA[1000])
idx1=int(0.05*n)
idx2=int(0.99*n)
print(idx1,idx2)
print(srtA[idx1],srtA[idx2])
v1=srtA[idx1]
v2=srtA[idx2]
plt.figure()
#plt.imshow(imgA,cmap='gray', vmin=0.0, vmax=20000.0)
plt.imshow(imgA,cmap='gray', vmin=v1, vmax=v2,aspect='auto')
ax = plt.gca()
ax.invert_yaxis()
#ax.set_aspect(1.0/4.0)
x = [50,100,1000 ,1950]
y = [1150,1500,1600, 1100]
#plt.plot(x, y, color="red", linewidth=0.5)
for fib_idx in range(400):
    plt.plot(xV, tlmA[fib_idx], color="red", linewidth=0.5)
    s="FIB="+str(fib_idx+1)+" TYPE=P"
    plt.text(xV[int(npix/2)], tlmA[fib_idx][int(npix/2)]+1, s, color="white", ha="center")
#    plt.text(x, y, s, bbox=dict(fill=False, edgecolor='red', linewidth=2))


#bnext = Button(ax, 'ZOOM',color="green")
plt.show()
#plt.colourbar()
