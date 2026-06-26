if %1 == "" echo Error: No filename provided.& goto :eof
if not exist "%1" echo File not found: %1& goto :eof
set "fname=%1"

python "%fname%"