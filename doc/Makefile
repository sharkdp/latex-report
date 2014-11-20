cheatsheet.pdf: ../include/header.tex ../include/commands.tex create-cheatsheet.py
	mkdir -p dist
	python create-cheatsheet.py ../include/commands.tex > cheatsheet.tex
	pdflatex -output-directory=dist -halt-on-error -interaction=nonstopmode cheatsheet.tex
	mv dist/cheatsheet.pdf .

clean:
	rm -rf dist
	rm -f cheatsheet.tex
