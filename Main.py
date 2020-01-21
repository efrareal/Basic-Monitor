#Importando modulos necesarios
import sys
import time

from create_threads import create_threads
from ip_file_valid import ip_file_valid
from ip_addr_valid import ip_add_valid
from ip_monitor import ip_monitor

#Verifica que exista el archivo
ip_list = ip_file_valid()

#Verifica que la IP sea correcta
try:
    ip_add_valid(ip_list)

except KeyboardInterrupt:
    print('La IP proporcionada es invalida!')
    sys.exit()

try:
    create_threads(ip_list, ip_monitor)
    time.sleep(3)

except KeyboardInterrupt:
    print('Programa detenido por Usuario')
    sys.exit()
