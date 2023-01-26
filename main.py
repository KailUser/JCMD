import cmd
import os
import colorama
from colorama import *
import time
import ftplib
import getpass
import webbrowser


colorama.init(autoreset=True)
just_fix_windows_console()
username = getpass.getuser()
class MyCLI(cmd.Cmd):
    intro = Fore.LIGHTGREEN_EX + "Welcome to JCmd.\nType help or ? to list commands.\nCreated on JCore\n"
    prompt = Fore.LIGHTGREEN_EX + f"{username}: "

    def do_print(self, line):
        """
        print message
        Usage: print [text]
        """
        text = line.strip() or "Oops. Your text is Died"
        print(f"{text}")
    
    def do_cls(self, line):
        """
        Clear all cmd
        Usage: cls
        """
        os.system('cls')
    def do_ftp(self, line):
        """
        Connect to ftp server
        Usage: ftp
        """
        server = input("Enter the FTP server: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        os.system('cls')
        print(Fore.RED + "Server: ", server)
        print(Fore.RED + "Username: ", username)
        print(Fore.RED + "Password: ", password)
    
        confirm = input("Is the above information correct? (y/n)")
        if confirm.lower() == 'y':
            while True:
                os.system('cls')
                ftp = ftplib.FTP()
                ftp.connect(server, 21)
                ftp.login(user=username, passwd=password)
                ftp.cwd('/')
                print(Fore.GREEN + "1. List files")
                print(Fore.GREEN + "2. Upload a file")
                print(Fore.GREEN + "3. Download a file")
                print(Fore.GREEN + "4. Read file")
                print(Fore.GREEN + "5. Quit")
                choice = input("Enter your choice: ")
    
                if choice == '1':
                    os.system('cls')
                    ftp.retrlines('LIST')
                elif choice == '2':
                    filename = input("Enter the file name: ")
                    with open(filename, 'rb') as f:
                        ftp.storbinary('STOR '+ filename, f)
                elif choice == '3':
                    filename = input("Enter the file name: ")
                    with open(filename, 'wb') as f:
                        ftp.retrbinary('RETR '+ filename, f.write)
                elif choice == '4':
                    os.system('cls')
                    os.getcwd()
                    filename = input("File name: ")
                    with open(filename, 'r') as f:
                        lines = f.readlines()
                        for line in lines:
                            print(line)
                elif choice == '5':
                    ftp.quit()
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Exiting the program.")

    def do_pip(self, line):
        """
        Install packages from Python Package Index
        Usage: pip [package]"""
        plugin = line.strip()
        os.system(f'pip install {plugin}')
    
    def do_fp(self,line):
        """
        Open folder
        Usage: fp [folder_location]
        """
        folder_location = line.strip()
        os.startfile(folder_location)
    
    def do_fl(self, line):
        """
        File list on dir
        Usage: fl [Location]
        """
        location = line.strip() or 'C:/'
        print(f"On folder {location} all files is : \n", os.listdir(location))

    def do_python(self, line):
        """
        Start python file
        Usage: python [File_location]
        """
        file_loc = line.strip() or 'C:/'
        print(os.system(f'python {file_loc}'))
    def do_github(self, line):
        """
        GitHub for this cmd line
        Usage: github
        """
        webbrowser.open('')

if __name__ == "__main__":
    os.system('cls')
    MyCLI().cmdloop()
