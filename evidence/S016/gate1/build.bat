@echo off
call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat" >nul
cd /d C:\Almost-Stacked-Proof\build\S016
cl /nologo /O2 /EHsc /I. /FIpopcount_shim.h /Fe:s015_layers_v3.exe ..\..\tools\s015_layers_v3.cpp
cl /nologo /O2 /I. /FIpopcount_shim.h /Fe:s015_check_v2.exe ..\..\tools\s015_check_v2.c
