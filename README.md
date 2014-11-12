latex-report
============

A LaTeX template for simple reports. Comes with a bootstrap script and lots of custom LaTeX commands.

Quick start
-----------

Create a new folder for your report. *Within* the new folder, call:

```sh
git clone https://github.com/sharkdp/latex-report.git
./latex-report/bootstrap.sh main
```

where `main` is your desired name for the root LaTeX file (without ending). The bootstrap script creates initial LaTeX files as well as two directories `fig` for figures and `dist` for LaTeX output files. It also creates a new git repository for the report with an initial `.gitignore` file.

Editing
-------
The title and author of the report can be modified in `metadata.tex` and the content of your report resides in `main.tex`.

Compiling
---------
Continuously monitor changes to the main tex-file and all includes by using `latexmk`:
```sh
latexmk -output-directory="dist" -pvc -pdf main.tex
```
Here, `main.tex` is the name of your root latex file. All output goes to the `dist` directory.

Updating
--------
To update latex-report, call:
```sh
git -C latex-report pull
```
