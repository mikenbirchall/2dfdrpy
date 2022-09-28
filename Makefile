all:
	cd tdfio_py; make all
	cp tdfio_py/tdfio.py .

clean:
	cd tdfio_py; make clean
	cd test_dir; make clean
	rm -rdf tdfio.py
