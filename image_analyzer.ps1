# image_analyzer.ps1
# Set UTF-8 encoding for the console
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "Starting Image Analyzer..." -ForegroundColor Cyan

# Activate virtual environment
& ".\.venv\Scripts\Activate.ps1"

# Set Python to use UTF-8
$env:PYTHONIOENCODING = "utf-8"

# Run the Python script
python -m src.image_analyzer

# Deactivate virtual environment
deactivate

# Pause to see results
Write-Host "`nPress any key to continue..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
