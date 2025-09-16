@echo off
SETLOCAL

:: ================================
:: Upgrade pip
:: ================================
python -m ensurepip --default-pip
python -m pip install --upgrade pip

:: ================================
:: Install required packages
:: ================================
python -m pip install speedtest-cli pandas openpyxl

echo.
echo Required Python packages installed !

pause
ENDLOCAL