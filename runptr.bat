@echo Started %date% %time% >> PTRLog.txt
call "update_PTR.bat" >> PTRLog.txt
@echo Completed: %date% %time%
@echo &&