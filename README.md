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

where `main` is the desired name for the report LaTeX file (without ending). The bootstrap script creates a starting LaTeX file as well as two directories `fig` for figures and `dist` for LaTeX output files. It also creates a new git repository for the report with an initial `.gitignore` file.

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
