@echo off

set SRCDIR=%~dp0
set SRV_OUT=%SRCDIR%
set CLI_OUT=%SRCDIR%..\..\client\Assets\Scripts\

@echo Source dir: %SRCDIR%

:: call protoc -I=%SRCDIR% --plugin=protoc-gen-python3=C:\protoc-3.5.1-win32\bin\protoc-gen-python3.cmd --python3_out=%SRCDIR%out %SRCDIR%protocol.proto

@echo Generating protocol for server
call protoc -I=%SRCDIR% --python_out=%SRV_OUT% %SRCDIR%protocol.proto

@echo Generating protocol for client
call protoc -I=%SRCDIR% --csharp_out=%CLI_OUT% %SRCDIR%protocol.proto
