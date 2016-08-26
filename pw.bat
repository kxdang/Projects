@ECHO OFF

SET mypath=%~dp0
ECHO %mypath:~0,-1%
python.exe %mypath:~0,-1%/pw.py %1