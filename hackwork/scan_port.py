# # # # # coding:utf-8 # # # # #
#     Day:3 Port sniffer       #
# # # # # # # #### # # # # # # #

import optparse
import socket


def connScan(tgtHost,tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send('ViolentPython\r\n')
        results  = connSkt.recv(100)
        print('[+]%d/tcp open' % tgtPort)
        print('[+]' + str(results))
        sonnSkt.close()
    except:
        print('[-]%d/tcp closed' %  tgtPort)
        
def portScan(tgtHost,tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve '%s': Unknown host" % tgtHost)
        return
    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print('\n[+]Scan Results for:' + tgtName[0])
    except:
        print('\n[+]Scan Results for:'  + tgtIP)
        socket.setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning port:' + str(tgtPort))
        connScan(tgtHost,int(tgtPort))

def main():
    parser = optparse.OptionParser('usaget %prog -H <target host> -p <target port>')
    parser.add_option('-H',dest='tgtHost',type = 'string',help = 'specify target host')
    parser.add_option('-p',dest='tgtPort',type = 'int',help = 'specify target port')
    (options,args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = options.tgtPort
    if (tgtHost == None)|(tgtPort ==None):
        print('[-] You must specify a target host  and port[s]!')
        exit(0)
    portScan(tgtHost,args)

if __name__ == '__main--':
    main()