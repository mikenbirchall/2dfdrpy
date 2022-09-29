all:
	cd ../; make all;
	cp ../tdfio.py .
	if [ ! -e tmp_dir ]; then  mkdir tmp_dir; fi

clean:
	rm -f tdfio.py
	rm -rdf __pycache__
	rm -rdf tmp_dir
