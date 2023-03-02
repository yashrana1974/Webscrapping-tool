import time
import subprocess
import webbrowser
from subprocess import Popen

class Main:
    def exe(self):
        cmd = 'Python app.py'
        subprocess.Popen(cmd, shell=True)
        time.sleep(5)
        webbrowser.open('http://127.0.0.1:8000/',new=2)
        while True:
            if KeyboardInterrupt:
                exit

if __name__=="__main__":
    a = Main()
    a.exe()
