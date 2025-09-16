@echo off
SETLOCAL

:: ================================
:: Upgrade pip
:: ================================
python -m ensurepip --default-pip
pip install --upgrade pip

:: ================================
:: Install required packages
:: ================================
pip install speedtest-cli pandas openpyxl

echo.
echo Required Python packages installed successfully!

pause
ENDLOCAL