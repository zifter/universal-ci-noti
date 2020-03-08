@setlocal
@echo off

call %~dp0\configure_venv.bat >nul 2>&1

echo 'Execute pytest %*'
%~dp0\venv\Scripts\pytest %~dp0\src %*
