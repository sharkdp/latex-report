latex-report
============

A template for simple LaTeX reports.

Quick start
-----------

Create a new folder for your report. Within the folder, call:

```sh
git clone https://github.com/sharkdp/latex-report.git
./latex-report/bootstrap.sh main
```

where `main` is the name of your desired root LaTeX file. This script will create initial `tex` files, a `fig` and `.dist` directory for figures and latex temporary files. It also creates a git repository with a `.gitignore` file.

The title and author of the report can be modified in `metadata.tex` and the content of your report resides in `report.tex`.
