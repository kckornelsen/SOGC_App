@echo Started %date% %time% >> outfile2.txt
call "update_AvData.bat" >> outfile2.txt
@echo Completed: %date% %time%
@echo &&