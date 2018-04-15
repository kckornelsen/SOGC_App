
REM File to get latest PTR and push it.
git pull

XCOPY "C:\Users\Kurt\Dropbox\SOGC Documents\Standards Documents\SCCFSPTR.htm" "C:\Users\Kurt\Documents\GitHub\SOGC_App\SCCFSPTR.html" /Y/F


git add SCCFSPTR.html
git commit -m "Update PTR"
git push

