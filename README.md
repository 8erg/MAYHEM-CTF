                        ███▄ ▄███▓ ▄▄▄     ▓██   ██▓ ██░ ██ ▓█████  ███▄ ▄███▓
                       ▓██▒▀█▀ ██▒▒████▄    ▒██  ██▒▓██░ ██▒▓█   ▀ ▓██▒▀█▀ ██▒
                       ▓██    ▓██░▒██  ▀█▄   ▒██ ██░▒██▀▀██░▒███   ▓██    ▓██░
                       ▒██    ▒██ ░██▄▄▄▄██  ░ ▐██▓░░▓█ ░██ ▒▓█  ▄ ▒██    ▒██ 
                       ▒██▒   ░██▒ ▓█   ▓██▒ ░ ██▒▓░░▓█▒░██▓░▒████▒▒██▒   ░██▒
                       ░ ▒░   ░  ░ ▒▒   ▓▒█░  ██▒▒▒  ▒ ░░▒░▒░░ ▒░ ░░ ▒░   ░  ░
                       ░  ░      ░  ▒   ▒▒ ░▓██ ░▒░  ▒ ░▒░ ░ ░ ░  ░░  ░      ░
                       ░      ░     ░   ▒   ▒ ▒ ░░   ░  ░░ ░   ░   ░      ░   
                              ░         ░  ░░ ░      ░  ░  ░   ░  ░       ░   

## Setting up

#### Installing Hercules
1. `git clone https://github.com/wrljet/hercules-helper.git`
2. `sudo apt-get -y install libregina3-dev regina-rexx build-essential cmake flex gawk m4 autoconf automake libtool-bin libbz2-dev zlib1g-dev libcap2-bin`
3. `mkdir herctest && cd herctest`
4. `../hercules-helper/hercules-buildall.sh --auto --flavor=sdl-hyperion --prefix=/usr/local/hercules`
5. `cd hyperion`
6. `./autogen.sh`
7. `./configure`
8. `sudo make install`

>[!warning] 
>You need to restart your terminal before moving on to the next steps


#### GET MVS
1. `wget https://github.com/MVS-sysgen/sysgen/releases/download/v2.1.2/MVSCE.release.v2.1.2.tar`
2. `tar -xvf MVSCE.release.v2.1.2.tar`

## Configuring the environment
1. `cp packages/FTPD.MVP MVSCE/MVP/packages`
2. Launch MVSCE : `./start_mvs.sh`
3. `cat JCL/MACLFTPF.jcl | ncat --send-only -w1 127.0.0.1 3505`
4. `cat JCL/logon_screen.jcl | ncat --send-only -w1 127.0.0.1 3505`
5. `cat terminal.jcl | ncat --send-only -w1 127.0.0.1 3505`
6. Clone the ARBAUTH repo: `git clone https://github.com/jake-mainframe/ARBAUTH`
7. Run the python script : `./upload.py motd.txt`
8. `cat upload.jcl | ncat --send-only -w1 127.0.0.1 3505`



## Credits
+ I want to give big shoutouts to @mainframed his resources provided a lot of insights on how to build the environment and opening my eyes about mainframe hacking.
+ Also want to shoutout @moshix for his videos where he had a lot of tutorials about various things related to the mainframe.
+ And finally we have to shoutout Jay Moseley who made everything possible with the MVS3.8.

