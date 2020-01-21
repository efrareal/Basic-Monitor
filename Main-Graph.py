#Importando modulos necesarios
import sys
import time
#from ip_reach import ip_reach
from create_threads import create_threads
from ip_file_valid import ip_file_valid
from ip_addr_valid import ip_add_valid
from graph_plot import plot

#Verifica que exista el archivo
ip_list = ip_file_valid()

#Verifica que la IP sea correcta
try:
    ip_add_valid(ip_list)

except KeyboardInterrupt:
    print('La IP proporcionada es invalida!')
    sys.exit()

try:
    create_threads(ip_list, plot)
    time.sleep(3)

except KeyboardInterrupt:
    print('Programa detenido por Usuario')
    sys.exit()