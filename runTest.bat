cd %~dp0
set behave=venv\Scripts\behave.exe

%behave% -f allure -o test_results\allure
