#!/bin/bash

# Print message $2 with log-level $1 to STDERR, colorized if terminal
log() {
    local level=${1?}
    shift
    local code=''
    local line=">>> $*"
    if [ -t 2 ]
    then
        case "$level" in
            INFO) code=36 ;;
            DEBUG) code=30 ;;
            WARN) code=33 ;;
            ERROR) code=31 ;;
            *) code=37 ;;
        esac
        echo -e "\e[${code}m${line}\e[0m"
    else
        echo "$line"
    fi >&2
}


if [[ $# != 1 ]]; then
    log ERROR "Usage: bootstrap.sh <name of main tex file>"
    exit 1
fi

if [[ ! -e latex-report ]]; then
    log ERROR "Call this script from the directory including the 'latex-report' repository"
    exit 1
fi

# Name of the main LaTeX file
mainfile="${1}.tex"

# Copy all bootstrap files
log INFO "Creating '$mainfile' and standard settings"
cp -iv latex-report/bootstrap/main.tex "$mainfile"
cp -iv latex-report/bootstrap/.gitignore .
cp -iv latex-report/bootstrap/.latexmkrc .

# Create directories for figures and LaTeX output files
log INFO "Creating 'fig' and 'dist' directory"
mkdir -p fig
mkdir -p dist

# If pplatex is installed, use it:
if ppdflatex -V > /dev/null 2>&1; then
    log INFO "ppdflatex is installed, using instead of pdflatex"
    sed -i -e "s/'pdflatex/'ppdflatex/g" .latexmkrc
else
    log WARN "ppdflatex is not installed, using pdflatex"
fi

# Create git repository and make initial commit
if [[ ! -e .git ]]; then
    log INFO "Creating new git repository for this report"
    git init
    git submodule add https://github.com/sharkdp/latex-report.git latex-report
    git add .
    git commit -m "bootstrapped from latex-report"
else
    log INFO "This directory is already under version control."
    log INFO "You might want to add latex-report as a submodule:"
    log INFO "> git submodule add https://github.com/sharkdp/latex-report.git latex-report"
fi
