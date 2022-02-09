@echo off

call %~dp0bot\venv\Scripts\activate

cd %~dp0mybotingit

set  TOKEN=5248458671:AAFC2uhJmgZm-SxC-aUKS6gsf0fGUG5HR1U

python bot_tg.py

pause