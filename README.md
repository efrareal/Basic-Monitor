# Basic-Monitor
Ping monitor with smtp alert mail and optional graph time response

# How to use
In a txt file storage your IP address you want to poll, in the next format:

     10.1.1.1
     10.1.1.2
     10.1.1.3
     ...

In ip_monitor.py fill your SMTP server configuration:

    FROM = 'source@example.com
    TO = 'dest@example.com'
    user = 'username'
    password = '*******'
    server = smtplib.SMTP_SSL('SMTP.SERVER', TCP_port)

In order to collect the time response, please uncomment the next area in ip_monitor script ,and put your path:

    #if ping_reply == 0:
    #    ping = subprocess.run(['ping', '%s' % (ip)], stdout = subprocess.PIPE)
    #    respuesta = re.search(b'(time=\d+)', (ping.stdout))
    #    resp = ((respuesta.group(0)).decode('utf-8')).lstrip('time=')
    #    with open(('+++DESTINATION PATH+++\\{}.txt').format(ip), 'a') as f:
    #        f.write(resp + ',' + str(datetime.now()) + '\n')

    #else:
    #    with open(('+++++DESTINATION PATH++++\\{}.txt').format(ip), 'a') as f:
    #        f.write('np.nan' +',' + str(datetime.now()) + '\n')

***Notice that I'm using regular expression to match "time=\d+" if your OS is in differente language, you should modify this expression!

Once the programm is running, now you can use the Main-Graph.py script to build graphs in parallel

# Main.py
This is the Main script for ping and ping response stored

# ip_file_valid.py
This script verifies the path of the file that contains the IP addresses and extract the IP in a list

# ip_addr_valid.py
This scripts verifies all the IP address

# create_threads.py
This is a simple threading scripts to run in parallel the ip_monitor.py script for each IP

# ip_monitor.py
This script performs the actual ping and appends the ping response in a txt file. Also if there are 4 missing pings in a row the scripts sends the email.

