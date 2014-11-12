latex-report
============

A LaTeX template for simple reports.

Quick start
-----------

Create a new folder for your report. Within the folder, call:

```sh
git clone https://github.com/sharkdp/latex-report.git
./latex-report/bootstrap.sh main
```

where `main` is the name of your desired root LaTeX file. This script will create initial `tex` files, a `fig` and `dist` directory for figures and LaTeX output files. It also creates a git repository with a `.gitignore` file.

Editing
-------
The title and author of the report can be modified in `metadata.tex` and the content of your report resides in `report.tex`.

Compiling with `latexmk`
------------------------
```sh
latexmk -output-directory="dist" -pvc -pdf main.tex
```
where `main.tex` is the name of your root latex file.

Updating
--------
To update, go to the `latex-report` directory and call `git pull`.
