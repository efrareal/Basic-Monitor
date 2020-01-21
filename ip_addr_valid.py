import sys

#Revisa los octetos
def ip_add_valid(list):

    for ip in list:                 #Revisa cada IP en la lista
        ip = ip.rstrip('\n')        #Quita "\n" de la lista obtenida del arhivo de IPs
        octet_list = ip.split('.')  #Separa los octetos

        if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and (0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
            print('Las IPs son correctas! :)')
            continue  
        else:
            print('\n* Hay una direccion IP no valida en el archivo: {} :(\n'.format(ip))
            sys.exit

