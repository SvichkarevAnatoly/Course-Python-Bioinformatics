SHELL := /bin/bash

report=report4

read:	pdf clean
	evince ${report}.pdf &
	
pdf:	${report}.tex
	pdflatex ${report}.tex

clean:
	@rm -f ${report}.{ps,log,aux,out,dvi,bbl,blg}

cleanall:	clean
	@rm -f ${report}.{ps,log,aux,out,dvi,bbl,blg}
	@rm -f ${report}.pdf
