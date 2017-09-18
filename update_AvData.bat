

REM File to get new data for METARS and TAF and push it to the GitHub Pages
@echo %datetime% 

python get_MET_TAF.py

git add index.html
git commit -m "Update Index"
git push



