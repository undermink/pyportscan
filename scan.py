#!/usr/bin/env python

import threading
import Queue
import time
import sys
from socket import *

class WorkerThread(threading.Thread) :
    def __init__(self, queue) :
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self) :
        while True :
            counter = self.queue.get()
	    if len(sys.argv) > 2 :
		if sys.argv[2] == "-v" :
			print "Scanning Port %d..."%counter

	    s = socket(AF_INET, SOCK_STREAM)
	    s.settimeout(1.0)
	    result = s.connect_ex((targetIP, counter))
   	    if(result == 0) :
            	list.append('Port %d: OPEN' % (counter,))
	    s.close()
            self.queue.task_done()
 
queue = Queue.Queue()
list = []

if len(sys.argv) < 2 :
    print "\nUSAGE: scan_ports [scan_up_to_portnumber]\n"
    sys.exit()

target = raw_input('\nEnter host to scan: ')
targetIP = gethostbyname(target)

if int(sys.argv[1]) < 20 :
    ports = 1000
else :
    ports = int(sys.argv[1])

print "\nStarting scan on host", targetIP, "Ports 20 -", ports

for j in range(20, ports+1):
 	queue.put(j)

for i in range(25) :
    worker = WorkerThread(queue)
    worker.setDaemon(True)
    worker.start()


queue.join()
print "\n------All scans on ",targetIP," completed:)-------\n"
for open in list:
	print open

print "\n------------------------------------------------\n"
