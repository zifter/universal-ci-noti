echo 'pip install virtualenv'
pip install virtualenv

if not exist %~dp0\venv (
	echo 'virtualenv %~dp0\venv'
	virtualenv %~dp0\venv

	if not exist %~dp0\venv (
		echo "virtualenv is not working properly"
		exit /b 1
	)
) else (
	echo 'venv already exists'
)

echo 'pip install -r requirements.txt'
%~dp0\venv\Scripts\pip install -r %~dp0\requirements.txt