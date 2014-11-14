#!/bin/bash

if [[ $# != 1 ]]; then
    echo "Usage: bootstrap.sh <name of main tex file>"
    exit 1
fi

if [[ ! -e latex-report ]]; then
    echo "Call this script from the directory including the 'latex-report' repository"
    exit 1
fi

# Name of the main LaTeX file
mainfile="${1}.tex"

# Copy all bootstrap files
cp -iv latex-report/bootstrap/main.tex "$mainfile"
cp -iv latex-report/bootstrap/.gitignore .
cp -iv latex-report/bootstrap/.latexmkrc .

# Create directories for figures and LaTeX output files
mkdir -p fig
mkdir -p dist

# Create git repository and make initial commit
if [[ ! -e .git ]]; then
    git init
    git add .
    git commit -m "bootstrapped from latex-report"
fi
