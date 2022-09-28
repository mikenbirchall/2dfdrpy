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

