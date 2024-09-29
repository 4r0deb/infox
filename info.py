#!/usr/bin/env python3
import sys
import platform
import os
import subprocess

def sys_info():
    print("")
    #print(platform.uname())
    os.system("uname -amr;echo '';pwd")

def help():
    os.system("echo 'The following options are valid: '| pv -qL 10")
    print("sys              --system")
    print("list             --ls -lah")
    print("man              --man")
    print("statdir          --stat dir")
def list():
    list_files = subprocess.run(["ls", "-l"])
    print("The exit code was: %d" % list_files.returncode)

def man():
    os.system("x-terminal-emulator -b -noclose -e man x-terminal-emulator &")

def statdir():
    os.system("x-terminal-emulator -b -noclose -e opt/info/statdir")



if __name__ == "__main__":
    opt = sys.argv[1] if len(sys.argv) > 1 else None

    if opt == "sys":
        sys_info()
    elif opt == "help":
        help()
    elif opt == "list":
        list()
    elif opt == "man":
        man()
    elif opt == "statdir":
        statdir()
    else:
        print("      Please run info help")

