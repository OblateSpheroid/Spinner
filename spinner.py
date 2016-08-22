import sys, time
import threading

def spinner():
    print "\b-",
    sys.stdout.flush()
    while True:
        if stop_spin == 1:
            break
        print "\b\b-",
        sys.stdout.flush(); time.sleep(0.2)
        if stop_spin == 1:
            break
        print "\b\b\\",
        sys.stdout.flush(); time.sleep(0.2)
        if stop_spin == 1:
            break
        print "\b\b|",
        sys.stdout.flush(); time.sleep(0.2)
        if stop_spin == 1:
            break
        print "\b\b/",
        sys.stdout.flush(); time.sleep(0.2)
		
##check if math module is in globals()
if 'math' in globals():
    print "Math already imported"
else:
    print "Math not imported"

##initiate thread
t = threading.Thread(name='wait',target=spinner)
print "Importing...",
sys.stdout.flush()
stop_spin = 0
t.start()

##run code while thread is running
import math, csv #for example
time.sleep(4) #stand in for other commands that might take some time

##stop thread after code is done
stop_spin=1
print "\b\bdone!"
sys.stdout.flush()
t.join() #just to make sure thread is done before doing anything else

##check if math module is now in globals()
if 'math' in globals():
    print "Import was successful"
else:
    print "Import not successful"

