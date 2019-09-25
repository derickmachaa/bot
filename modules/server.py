from modules import printer
import subprocess,threading
def server(directory,port):
    printer.print_info("Starting server on port %s"%port)
    subprocess.call(['xterm','-title', 'server','-fg', 'green' ,'-e', 'python3' ,'-m' ,'http.server','-d',directory, str(port)])
def main():
    dir=input(printer.color_blue("Enter the Directory >"))
    port=input(printer.color_cyan("Enter the port >"))
    thread=threading.Thread(target=server,args=(dir,port))
    thread.daemon = True
    thread.start()
    printer.print_info("To Close The Server Close The X-term Started")
