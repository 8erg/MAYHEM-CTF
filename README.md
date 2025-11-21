```
    @@@@@@@@@@@@-@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@   @@@@@@@@@@@=#@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@         @@@@@@ :*@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@#@@@@@@@@@@@@@@@@@           @@#     - . - @@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@  -+ @@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@  @@@@@@@   @@@@@@   @@@@@@@@@@@@@@@ +.#@@@@@@@ @@@@@@@@@@@@@@
    @@@@@@@@@@@@@@    @@   @@@@@@@    %@     @@@@@@@@@@@:@#@@@*@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@     @@@@@@@@@*:  @     @@  :@@@@@@@@@#@*@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@   @@@@@@@      @@@#  @@    @@@@@@@@@@*@#@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@   @@@@@@@          @ @@    @@  :.@@@@@@@@=@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@   @@@@@@@    %@    @@ @    @@ =%*@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@  @@@@@@@     @@@@@@  @    @@= =%@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@         @@@@@@           @@@@@@ @@ .+@@ @@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@  @@@@@@@@           @@   @@@@@@@=#@@@@@@@@@ @@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@  @@@@@@@@@@           @@: * ++=-=@@@@@@@@@@ @@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@  @@@@@@@@@@@    .      @  . +@%#%@@@@@@@@@@ @@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@  %@@@@@@@@@@@@    - #::@@ =+# @*@@@@@@@@@@@ @%@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@   @@@@@@@@@@@@@ - - =#-@  .%@@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@ -   -@@@@@@@@@@@@@@@ *=@ @@@@%%@=@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@
    @@@@@@@@. +: @@@ =@@@@@@@@@@@@@ ::+#--@%%@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@% @@@@@@@@@@@@  - ##+@=@@=@@@  @%@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@+#@@@@@@@@@@@..=#%##@@@@@ *#@#@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@**@@@@@@@@@ #=+*+@%@@@=@@+@@#@@*@@ @@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@%*@%#@@@@@@ %%#@@@@@ =@=@@@@@@@@@*@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@ -%@@*** @@@@@##%@@@@ @#@ @@@@@@@@ #@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@%@@@@@@@@@@@= @@@#@@@@*@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@
    @@@@@@ %%@@@@%#@@@@@@@@@@@@@@@ #@%@%@@@@@@@@@@@@@ @@@@@%@@@ @@@@@@@@@@@@@@@
    @@@@@            _____ _____  ___.__.|  |__   ____   _____            @@@@@
    @@@@@           /     \\__  \<   |  ||  |  \_/ __ \ /     \           @@@@@
    @@@@@          |  Y Y  \/ __ \\___  ||   Y  \  ___/|  Y Y  \          @@@@@
    @@@@@          |__|_|  (____  / ____||___|  /\___  >__|_|  /          @@@@@ 
    @@@@@                \/     \/\/          \/     \/      \/           @@@@@           
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
```
## Setup

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

>[!note] 
>After the installtion of hercules and getting MVSCE, move the folder inside here and then start it

## Configuration

#### Manually
1. `cp extras/FTPD.MVP MVSCE/MVP/packages/FTPD`
2. Launch MVSCE : `./start_mvs.sh`
3. `cat JCL/MACLFTPD.jcl|ncat --send-only -w1 127.0.0.1 3505`
4. `cat JCL/logon_screen.jcl | ncat --send-only -w1 127.0.0.1 3505`
5. `cat JCL/terminals.jcl | ncat --send-only -w1 127.0.0.1 3505`
6. `git clone https://github.com/jake-mainframe/ARBAUTH`
6. Run the python script : `./upload.py motd.txt`
7. `cat JCL/upload.jcl | ncat --send-only -w1 127.0.0.1 3505`
8. Press `quit` in hercules and start it again

#### With automation
1. `cp extras/FTPD.MVP MVSCE/MVP/packages/FTPD`
2. `pip install automvs --break-system-packages`
4. `chmod +x *.py`
4. `./upload.py motd.txt`
5. `python ./MVS_INIT_CONFIG.py`
5. `python ./MVS_FTP_INIT.py`





## Credits
+ I want to give big shoutouts to [@mainframed](https://github.com/mainframed) his resources provided a lot of insights on how to build the environment and opening my eyes about mainframe hacking.
+ Also want to shoutout [@moshix](https://github.com/moshix) for his videos where he had a lot of tutorials about various things related to the mainframe.
+ And finally we have to shoutout Jay Moseley who made everything possible with the MVS3.8.

