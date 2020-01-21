import threading

#Crea threads
def create_threads(list, function):

    threads = []

    for ip in list:
        th = threading.Thread(target = function, args = (ip,)) #args es un tuple con un solo elemento
        th.start()
        threads.append(th)
    
    for th in threads:       #espera a que acaben todos los threads juntos
        th.join()

