@setlocal
@echo off

call %~dp0\configure_venv.bat >nul 2>&1

echo 'Execute python %*'
%~dp0\venv\Scripts\python %*
