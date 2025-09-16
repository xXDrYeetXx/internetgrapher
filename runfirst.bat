@echo off
SETLOCAL

:: Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Downloading Python installer...

    :: Download Python installer (latest stable 3.x version)
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe -OutFile python_installer.exe"

    echo Installing Python silently...
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1

    :: Cleanup installer
    del python_installer.exe

    echo Python installation complete.
)

:: Ensure pip is installed
python -m ensurepip --default-pip

:: Upgrade pip
python -m pip install --upgrade pip

:: Install required packages
python -m pip install speedtest-cli pandas

echo.
echo Python and required packages installed successfully!
pause
ENDLOCAL
