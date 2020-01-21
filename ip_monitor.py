#Ping App for Monitoring
import sys
import subprocess
import time
import smtplib
import re
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def ip_ping(ip):
    #Realiza ping y solo se trae el tipo de respuesta: 0 = echo reply, 1= no response
    ping_reply = subprocess.call('ping %s /n 2' % (ip), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    #if ping_reply == 0:
    #    ping = subprocess.run(['ping', '%s' % (ip)], stdout = subprocess.PIPE)
    #    respuesta = re.search(b'(time=\d+)', (ping.stdout))
    #    resp = ((respuesta.group(0)).decode('utf-8')).lstrip('time=')
    #    with open(('+++DESTINATION PATH+++\\{}.txt').format(ip), 'a') as f:
    #        f.write(resp + ',' + str(datetime.now()) + '\n')

    #else:
    #    with open(('+++++DESTINATION PATH++++\\{}.txt').format(ip), 'a') as f:
    #        f.write('np.nan' +',' + str(datetime.now()) + '\n')

    return ping_reply

def ip_monitor(ip):
    #PING DOWN
    ip = ip.rstrip('\n')
    while True:
        ping_count_down = 0
        try:
            while ping_count_down < 4:
                reply = ip_ping(ip)
                print(reply)
            
                if reply == 1:
                    ping_count_down +=1
                    print('Perdio un paquete')
                    time.sleep(5)
                    reply2 = ip_ping(ip)

                    if reply2 == 1:
                        ping_count_down +=1
                        print('Perdio 2 pkts seguidos')
                        time.sleep(10)
                        reply3 = ip_ping(ip)

                        if reply3 == 1:
                            ping_count_down +=1
                            print('Perdio 3 pkts seguidos')
                            time.sleep(15)
                            reply4 = ip_ping(ip)

                            if reply4 == 1:
                                ping_count_down +=1
                                print('Perdio 4 pkts seguidos')

                                #Deja de responder PING
                                print('Fuera de alcance... Mandar correo por sitio fuera')
                                #Manda correo con alerta ping down!
                                fromaddr = 'name@example.com'
                                toaddr = 'dest@example.com'
                                msg = MIMEMultipart()
                                msg['From'] = fromaddr
                                msg['To'] = toaddr
                                msg['Subject'] = 'Ping down {}'.format(ip)
                        
                                #Envia correo por puerto 465
                                server = smtplib.SMTP_SSL('smtp.com', 465)
                                server.ehlo()
                                #server.starttls
                                #Haciendo logging a GMAIL
                                user = 'user'
                                contra = 'password'
                                server.login(user, contra)
                                server.sendmail(fromaddr, toaddr, msg.as_string())
                                server.quit()
                        else:
                            ping_count_down = 0
                    else:
                        ping_count_down = 0
                else:
                    ping_count_down = 0                    
        except KeyboardInterrupt:
            print('Programa detenido por Usuario')
            sys.exit()

        #Ping UP
        ping_count_up = 0
        try:
            while ping_count_up < 5:
                reply = ip_ping(ip)
                print(reply)

                if reply == 0:
                    ping_count_up +=1
                    print('responde un pkt')
       
        except KeyboardInterrupt:
            print('Programa detenido por Usuario')
            sys.exit()

        print('Equipo activo nuevamente')
        #Manda correo con alerta ping down!
        fromaddr = 'name@example.com'
        toaddr = 'destination@example.com'
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = 'Ping Up {}'.format(ip)
                        
        #Envia correo por puerto 465
        server = smtplib.SMTP_SSL('smtp.com', 465)
        server.ehlo()
        #server.starttls
        #Haciendo logging a GMAIL
        user = 'user'
        contra = 'password'
        server.login(user, contra)
        server.sendmail(fromaddr, toaddr, msg.as_string())
        server.quit()
