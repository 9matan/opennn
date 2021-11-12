@echo OFF
setlocal

set error_category=

echo.
echo Generating projects
call generate_vs_projects.bat
if errorlevel 1 set "error_category=Generation" & goto error

echo.
echo Building projects
set building_error=0
call build_debug.bat
if errorlevel 1 set building_error=1
call build_release.bat
if errorlevel 1 set building_error=1

if %building_error% NEQ 0 set "error_category=Building" & goto error

echo.
echo Runnig CI tests
call run_ci_tests.bat
if errorlevel 1 set "error_category=Testing" & goto error

REM TODO
REM Add run_tests here when all tests are fixed
REM Or select green ones

echo.
echo Successful
exit /B 0

:error
echo.
echo Failed: %error_category%