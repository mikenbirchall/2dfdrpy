def tdfio_fibres_read_types(tid):

    idx = FindExtension(tid,"*FIBRES_IFU")
    if (idx==-1):
            idx = FindExtension(tid,"*FIBRES")
    if (idx==-1):
        print("Error no fibre table found!")
        return -1

    # Read the fibre table
    fibreTable=tid[idx].data
    # Table.read(event_filename, hdu=1)
    fibTypes=fibreTable['TYPE']

    return fibTypes
