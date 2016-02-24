SHELL := /bin/bash

report=report2

read:	pdf clean_tmp
	evince ${report}.pdf &
	
pdf:	${report}.tex
	pdflatex ${report}.tex

clean_tmp:
	rm -f ${report}.{ps,log,aux,out,dvi,bbl,blg}

clean:
	rm -f ${report}.{ps,pdf,log,aux,out,dvi,bbl,blg}
