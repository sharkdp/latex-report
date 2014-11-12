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

mainfile="${1}.tex"

cp -iv bootstrap/* .
mv main.tex "$mainfile"

mkdir fig
mkdir .dist

echo "$mainfile" >> .gitignore
