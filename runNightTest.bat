cd %~dp0
set behave=venv\Scripts\behave.exe

%behave% --tags=@NightTest
