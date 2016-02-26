filename=MAIN_LATEX_FILE_NAME_WITHOUT_.tex

pdf:
	latex ${filename}
	bibtex ${filename}||true
	latex ${filename}
	latex ${filename}

read:
	open ${filename}.pdf

clean:
	rm -f ${filename}.{ps,pdf,log,aux,out,dvi,bbl,blg}
