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

>[!info] After the installtion of hercules and getting MVSCE, move the folder inside here and then start it

## Configuration

#### Manually
1. `cp extras/FTPD.MVP MVSCE/MVP/packages`
2. Launch MVSCE : `./start_mvs.sh`
3. `cat jcl/MACLFTPF.jcl|ncat --send-only -w1 127.0.0.1 3505`
2. `cat JCL/logon_screen.jcl | ncat --send-only -w1 127.0.0.1 3505`
4. Run the python script : `./upload.py motd.txt`
5. `cat upload.jcl | ncat --send-only -w1 127.0.0.1 3505`
6. Press `quit` in hercules and start it again

#### With automation
1. `pip3 install ebcdic --break-system-packages`
2. `pip install telnetlib3 --break-system-packages`
3. `./upload.py motd.txt`
4. `until python3 -u automation.py --initial; do echo "Failed, trying again"; done`





## Credits
+ I want to give big shoutouts to [@mainframed](https://github.com/mainframed) his resources provided a lot of insights on how to build the environment and opening my eyes about mainframe hacking.
+ Also want to shoutout [@moshix](https://github.com/moshix) for his videos where he had a lot of tutorials about various things related to the mainframe.
+ And finally we have to shoutout Jay Moseley who made everything possible with the MVS3.8.

