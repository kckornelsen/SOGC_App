

REM File to get new data for METARS and TAF and push it to the GitHub Pages
@echo %datetime% 

XCOPY "C:\Users\Home\Dropbox\SOGC Documents\Standards Documents\SCCFSPTR.htm" "C:\Users\Home\Documents\GitHub\SOGC_App\SCCFSPTR.html" /y

git add SCCFSPTR.html
git commit -m "Update PTR"
git push



