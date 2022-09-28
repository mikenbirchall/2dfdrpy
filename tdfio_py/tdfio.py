import numpy   as np
import astropy as ap
from astropy.io    import fits
from astropy.table import Table


def ExtensionNameMatch(ref_name, ext_name):
    flag=False
    clean_ref_name=ref_name.strip('*')
    if (ref_name.startswith('*') and ref_name.endswith('*')) :
        print(ref_name, 'beg and end', clean_ref_name)
        flag=(clean_ref_name  in ext_name)
    elif (ref_name.startswith('*')):
        print(ref_name, 'beg with', clean_ref_name)
        flag=ext_name.endswith(clean_ref_name)
    elif (ref_name.endswith('*')):
        print(ref_name, 'ends with', clean_ref_name)
        flag=ext_name.startswith(clean_ref_name)
    else:
        print (ref_name, 'neither',clean_ref_name)
        flag=(ref_name==ext_name)
    print('flag',flag)
    return flag

def FindExtension(tid,ref_name):
    n_ext=len(tid)
    print(len(tid))
    for idx in range(n_ext):
        print ('Idx=', idx)
        hdr = tid[idx].header
        if (idx>0):
            extname=hdr['EXTNAME']
            match_flag=ExtensionNameMatch(ref_name,extname)
            if (match_flag):
                print('EXTNAME=',extname, "Match at idx=",idx)
                return idx
            else:
                print('EXTNAME=',extname, "No Match")
    return -1

def tdfio_open (filename):
    tid = fits.open(filename)
    return tid

print ("tdfo_open loaded")
def tdfio_close (tid):
    tid.close()
def tdfio_kywd_read_char(tid,kywd):
     hdr = tid[0].header
     nkywds=len(hdr)
     try:
         retval=hdr[kywd]
     except:
         retval="NULL"
     return retval

     for idx in range(nkywds):
         val=hdr[idx]
         print("IDX=",idx,":", val)
         if (idx>10): return "YY"
     print(" n kywds-", nkywds)


def tdfio_getclass(tid):

    # First look for a NDF_CLASS extension
    idx=FindExtension(tid,"NDF_CLASS")

    if (idx!=-1):
        # Extension found now read the one cell table
        table  = tid[idx].data
        record = table.field(0)
        value  = record[0]
        return value

    return "COULDNT FIND TMF"
def tdfio_getsize(tid):
    imgA = tid[0].data
    imgDims=imgA.shape
    size1=imgDims[0]
    size2=imgDims[1]
    return size1, size2
def tdfio_image_read(tid):
    imgA = tid[0].data
    return imgA
def tdfio_tlmap_read(tid):
    imgA = tid[0].data
    return imgA
def tdfio_tlmap_write(tid,tlmA):
    print("NOT implemented yet")
def tdfio_variance_read(tid):
    idx=FindExtension(tid,"VARIANCE")
    imgA=tid[idx].data
    return imgA
