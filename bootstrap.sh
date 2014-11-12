if [[ $# != 1 ]]; then
    echo "Usage: boostrap.sh <name of main tex file>"
    exit 1
fi

if [[ ! -e latex-report ]]; then
    echo "Call this script from the directory including the 'latex-report' repository"
    exit 1
fi

if [[ -e main.tex ]]; then
    echo "Error: main.tex already exists"
    exit 1
fi

# Name of the main LaTeX file
mainfile="${1}.tex"

# Copy all boostrap files
cp -iv latex-report/bootstrap/* .
cp -iv latex-report/bootstrap/.gitignore .
mv main.tex "$mainfile"

# Create directories for figures and temporary files
mkdir -p fig
mkdir -p .dist

# Add output file to .gitignore
echo "${1}.pdf" >> .gitignore

# Create git repository and make initial commit
if [[ ! -e .git ]]; then
    git init
    git add .
    git commit -m "bootstrapped from latex-report"
fi
