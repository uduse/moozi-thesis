#!/usr/bin/env bash

set -e

# mkdir -p ./build
# cp main.tex bibs.bib ./build/
# cp -r assets ./build/

# git show HEAD:main.tex > ./build/old.tex
# git show HEAD:bibs.bib > ./build/old.bib

# cd ./build
# pdflatex -interaction=nonstopmode main.tex
# pdflatex -interaction=nonstopmode old.tex

# biber main.bcf
# biber old.bcf

# latexdiff --subtype=COLOR --append-textcmd="field,name" old.bbl main.bbl > diff.bbl
# latexdiff old.tex main.tex > diff.tex

# biber diff.bcf

# pdflatex -interaction=nonstopmode diff.tex

# echo "Difference PDF generated in diff.pdf"

rm -rf ./old/

mkdir ./old
git show HEAD:main.tex > ./old/main.tex
git show HEAD:bibs.bib > ./old/main.bib
cp -r assets ./old/

cd old
pdflatex -interaction=nonstopmode main
biber main

# pdflatex -output-directory=build -interaction=nonstopmode new.tex

# # Run `biber` on the `.bcf` files to generate `.bbl` files.
# biber --output-directory=build --input-directory=build old.bcf
# biber --output-directory=build --input-directory=build new.bcf

# # Create the `diff.bbl` file.
# latexdiff --append-textcmd=field ./build/old.bbl ./build/new.bbl > ./build/diff.bbl

# # Run `latexdiff` on the `.tex` files with the options removed.
# latexdiff old.tex new.tex > ./build/diff.tex

# # Run `pdflatex` to produce the `.pdf`.
# pdflatex -output-directory=build -interaction=nonstopmode diff.tex