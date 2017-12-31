@echo off

set SRCDIR=%~dp0
set SRV_OUT=%SRCDIR%
set CLI_OUT=%SRCDIR%..\..\client\Assets\Scripts\
set SRC_PROTO=%SRCDIR%protocol.proto

@echo Source dir: %SRCDIR%


@echo Generating protocol for server
:: Using native python generator
:: call protoc -I=%SRCDIR% --python_out=%SRV_OUT% %SRC_PROTO%

:: Using python3 generator
call protoc -I=%SRCDIR% --plugin=protoc-gen-python3=C:\protoc-3.5.1-win32\bin\protoc-gen-python3.cmd --python3_out=%SRV_OUT% %SRC_PROTO%


@echo Generating protocol for client
call protoc -I=%SRCDIR% --csharp_out=%CLI_OUT% %SRC_PROTO%
