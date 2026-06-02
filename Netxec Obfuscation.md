# NetExec Obfuscation
If you follow this simple guide you should be able to obfuscate NetExec so that it passes the Defender defenses and enjoy all it's capabilities.

### Preface
This needs to be carried from Windows as it is required by "PyInstaller" in order to generate a self-containing executable in Windows.
Unfortunately this guide will strip down some capabilities from the toolkit like all the Mimi/PypyKatz, SamDump/NanoDump, and some less common Wmiexec vbs payloads, lastly some *.b64 that are straight base64 encoded.
**OBS: this has been tested only in Windows Defender and it might still fail.**

## Obfuscation
### Removing the base64 encoded files
Use the following PowerShell command to empty all the Base64 encoded files, as my understating those are not so interesting and it is getting flagged by the AV:
```powershell
Get-ChildItem -Path ".\NetExec\nxc\data" -Filter *.b64 -Recurse | ForEach-Object { "" | Set-Content $_.FullName }
```
### Removing the VBS files
Use the following PowerShell command to empty all the VBS files, as my understating those are not so interesting and it is getting flagged by the AV:
```powershell
Get-ChildItem -Path ".\NetExec\nxc\data" -Filter *.vbs-Recurse | ForEach-Object { "" | Set-Content $_.FullName }
```
### Obfuscate all the python files
Now is where the tedious part begins as all the files that are non "functionality" centric should be obfuscated and i used [this](https://github.com/lunarshade34/Python-Code-Obfuscator) tool to obfuscate and it transform to bytecode, base64 encode and do some marshalling shenanigans.
Start on the root folder at the following path "*\NetExec\nxc*" but execute only on the subfolders:
```powershell
Get-ChildItem -Filter *.py | Where-Object { $_.Name -notlike "__*" -and $_.Name -notlike "database.py" -and $_.Name -notlike "db_navigator.py"  -and $_.Name -notlike "proto_args.py" } | ForEach-Object { "y" | python C:\Exclusions\Tools\Python-Code-Obfuscator\obfuscator\obfuscator.py --compress $_.FullName -o $_.FullName }
```
Specifically on these subfolders content:
```powershell
d-----          6/2/2026   7:08 PM                helpers
d-----          6/2/2026   7:08 PM                loaders
d-----          6/2/2026   7:08 PM                modules
d-----          6/2/2026   7:08 PM                protocols
```
And consequently the "protocols" file & folder's subfolders as well:
```powershell
d-----          6/2/2026   7:08 PM                ftp
d-----          6/2/2026   7:08 PM                ldap
d-----          6/2/2026   7:08 PM                mssql
d-----          6/2/2026   7:08 PM                nfs
d-----          6/2/2026   7:08 PM                rdp
d-----          6/2/2026   7:08 PM                smb
d-----          6/2/2026   7:08 PM                ssh
d-----          6/2/2026   7:08 PM                vnc
d-----          6/2/2026   7:08 PM                winrm
d-----          6/2/2026   7:08 PM                wmi
-a----          6/2/2026   7:35 PM           6510 ftp.py
-a----          6/2/2026   7:35 PM          62874 ldap.py
-a----          6/2/2026   7:35 PM          24566 mssql.py
-a----          6/2/2026   7:35 PM          29334 nfs.py
-a----          6/2/2026   7:36 PM          23798 rdp.py
-a----          6/2/2026   7:36 PM          82854 smb.py
-a----          6/2/2026   7:36 PM          13270 ssh.py
-a----          6/2/2026   7:36 PM           7250 vnc.py
-a----          6/2/2026   7:36 PM          21130 winrm.py
-a----          6/2/2026   7:36 PM          17754 wmi.py
-a----          6/2/2026   7:08 PM              0 __init__.py
```
### Remove malicious dependencies
Another issue is with some of the external dependencies that NetExec loads while compiling via PyInstaller so you must remove all the Lsassy, PypyKatz,HandleKatz and NanoDump from the "*netexec.spec*" file.
**OBS: you might also want to remove those files from the "modules" folder, this breaks the structure but it is the quick way to make it work.** 
### Missing dependencies
For some reason the default spec file is missing some dploot dependencies so check that these dependencies are not missing.
```text
'dploot.triage.cng',
```
## Compilation
When done compile on Windows:
```powershell
python -m venv env
.\env\Scripts\activate.bat
pip install pyinstaller pillow .
python -m PyInstaller .\netexec.spec
```


 
 
