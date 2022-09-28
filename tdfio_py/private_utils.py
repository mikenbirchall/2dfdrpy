
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

