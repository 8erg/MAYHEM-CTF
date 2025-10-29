import os
from automvs import automation

build = automation(
    system='MVSCE',
    system_path='/home/kali/MAYHEM-CTF/MVSCE/',
    ip = '127.0.0.1',
    punch_port = 3505,
    username='IBMUSER',
    password='SYS1'
    )
cwd = os.getcwd()
build.ipl(clpa=False)


try:
    os.chdir("../")
    cwd = os.getcwd()
    
    print("[+] Submitting {}/JCL/MACLFTPD.jcl".format(cwd))
    with open("{}/JCL/MACLFTPD.jcl".format(cwd),"r") as jcl:
        build.submit(jcl.read())
    build.wait_for_string("$HASP250 MACLFTPD IS PURGED")

    print("[+] Submitting {}/JCL/logon_screen.jcl".format(cwd))
    with open("{}/JCL/logon_screen.jcl".format(cwd),"r") as jcl:
        build.submit(jcl.read())
    build.wait_for_string("$HASP395 AWESOME  ENDED")

    #print("[+] Submitting {}/JCL/terminals.jcl".format(cwd))
    #with open("{}/JCL/terminals.jcl".format(cwd),"r") as jcl:
    #    build.submit(jcl.read())
    #build.wait_for_string("$HASP250 TERMINAL IS PURGED")

    print("[+] Submitting {}/JCL/upload.jcl".format(cwd))
    with open("{}/JCL/upload.jcl".format(cwd),"r") as jcl:
        build.submit(jcl.read())
    build.wait_for_string("$HASP250 UPLOAD   IS PURGED")

    print("[+] Starting FTP Server on port 2121")
    build.send_oper("/S FTPDPARM,SRVPORT=2121")
except Exception as e:
    build.quit_hercules()

finally:
    build.reset_hercules()
