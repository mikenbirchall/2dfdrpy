
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
