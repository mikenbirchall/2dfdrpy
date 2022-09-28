py_files = tdfio_header.py    \
	   private_utils.py   \
           tdfio_open.py      \
	   tdfio_close.py     \
           tdfio_kywd_read.py \
           tdfio_getclass.py  \
           tdfio_getsize.py   \
           tdfio_image_read.py \
           tdfio_tlmap_read.py \
           tdfio_tlmap_write.py\
           tdfio_variance_read.py

all: tdfio.py


tdfio.py: $(py_files)
	cat $(py_files) > $@

clean:
	rm -f tdfio.py
