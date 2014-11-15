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

Custom commands
---------------
An overview of the predefined commands can be found in the [command cheatsheet](https://github.com/sharkdp/latex-report/raw/master/doc/cheatsheet.pdf).

Compiling
---------
Continuously monitor changes to the main tex-file and all includes by calling `latexmk`. latex-report comes with a default `.latexmkrc` file.

Updating
--------
To update latex-report, call:
```sh
git -C latex-report pull
```
