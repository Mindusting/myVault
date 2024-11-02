@echo off
:inicio
set i=0
set/p n=Numero de veces:
:main
echo Hola mundo!!!%i%
set/a i= %i% + 1
if not %i% == %n% goto main
pause>null
exit
