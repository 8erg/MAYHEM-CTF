import os
from automvs import automation

home = os.path.expanduser("~")
build = automation(
    system='MVSCE',
    system_path=f'{home}/MAYHEM-CTF/MVSCE/',
    ip = '127.0.0.1',
    punch_port = 3505,
    username='IBMUSER',
    password='SYS1'
    )
build.ipl(clpa=False)


try:
    build.send_oper("/S FTPDPARM,SRVPORT=2121")

finally:
    print("[+] Starting FTP Server on port 2121")
