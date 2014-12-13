latex-report
============

This is a simple LaTeX template for reports. It comes with a bootstrap script and lots of custom commands.

Quick start
-----------
Create a new folder for your report. *Within* the new folder, call:

```sh
git clone https://github.com/sharkdp/latex-report.git
./latex-report/bootstrap.sh main
```

Here, `main` is the name for the main file of your report (without ending). The bootstrap script creates the main LaTeX file as well as two directories `fig` for figures and `dist` for LaTeX output files. It also creates a new git repository for the report with an initial `.gitignore` file.

Custom commands
---------------
An overview of the predefined commands can be found in the [command cheatsheet](https://github.com/sharkdp/latex-report/raw/master/doc/cheatsheet.pdf) which is created automatically from `include/commands.tex`.

Compilation
-----------
To compile the report, (install and) call
```sh
latexmk
```
The configuration file for latexmk is called `.latexmkrc`. To continuously monitor changes to the main tex-file and all includes, call
```sh
latexmk -pvc
```

Updating
--------
To update latex-report, call:
```sh
git -C latex-report pull
```
