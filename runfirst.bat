@echo off
SETLOCAL

:: ================================
:: Upgrade pip
:: ================================
py -m ensurepip --default-pip
py -m pip install --upgrade pip

:: ================================
:: Install required packages
:: ================================
pip install speedtest-cli pandas openpyxl

echo.
echo Required Python packages installed successfully!

pause
ENDLOCAL