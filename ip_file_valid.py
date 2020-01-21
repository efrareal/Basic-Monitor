import os.path
import sys

#Revisa el archivo de direcciones IP y valida su contenido
def ip_file_valid():

    #Le pide al usuario el archivo de entrada
    ip_file = input('\n# Introduzca el path del arhivo de IPs y su nombre: ')

    #Valida si el archivo existe
    if os.path.isfile(ip_file) == True:
        print('\n El archivo es valido :) \n')

    else:
        print('\n El archivo {} no existe :( Por favor intenta de nuevo. \n'.format(ip_file))
        sys.exit()
    
    #Abre el archivo como lectura
    selected_ip_file = open(ip_file, 'r')

    #Inicia el archivo desde la primera linea
    selected_ip_file.seek(0)

    #Lee el archivo linea por linea
    ip_list = selected_ip_file.readlines()

    #cierra el archivo
    selected_ip_file.close()

    #Salida de este modulo
    return ip_list

