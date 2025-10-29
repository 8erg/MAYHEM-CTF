#!/usr/bin/env python3

# This will create MAYHEM.* datasets
# Replaced the LOGON clist with motd.txt

import sys
import math
from pathlib import Path

# Takes in a CLIST and splits the text on each line

if len(sys.argv) < 2:
    print("Missing argument\n Usage: {} motd.txt".format(sys.argv[0]))
    sys.exit()

MOTDJCL = '''//UPLOAD JOB (JOB),'MOTD',
//         CLASS=A,MSGLEVEL=(1,1),MSGCLASS=A,
//         NOTIFY=IBMUSER,USER=IBMUSER,PASSWORD=SYS1
//*
//* This JCL was generated with upload.py use that dont edit this
//*
//MOTDPROC EXEC PGM=IEBUPDTE,PARM=NEW
//SYSPRINT DD  SYSOUT=*
//SYSUT2   DD  DSN=SYS1.CMDPROC,DISP=SHR
//SYSIN    DD  DATA,DLM='><'
./ ADD NAME=STDLOGON
        PROC 0
CONTROL NOMSG,NOLIST,NOSYMLIST,NOCONLIST,NOFLUSH
CLS
{MOTD}
REVINIT
><
'''

replace_ispf_clist = '''//*
//* Replace the ISPF clist to get rid of annoying "FREE" messages
//*
//ISPFPROC EXEC PGM=IEBUPDTE,PARM=NEW
//SYSPRINT DD  SYSOUT=*
//SYSUT2   DD  DSN=SYS1.CMDPROC,DISP=SHR
//SYSIN    DD  DATA,DLM='><'
./ ADD NAME=ISPF
PROC  0                                                             
/*     ALLOCATE REQUIRED ISPF DD NAMES     */                       
ALLOC F(ISPCLIB) DA('SYSGEN.ISPF.CLIB','SYSGEN.REVIEW.CLIST') SHR   
ALLOC F(ISPLLIB) DA('SYSGEN.ISPF.LLIB','SYSGEN.REVIEW.LOAD') SHR    
ALLOC F(ISPMLIB) DA('SYSGEN.ISPF.MLIB') SHR                         
ALLOC F(ISPPLIB) DA('SYSGEN.ISPF.PLIB','SYSGEN.ISPF.RFEPLIB') SHR   
ALLOC F(ISPSLIB) DA('SYSGEN.ISPF.SLIB') SHR                         
ALLOC F(ISPTABL) DA('SYSGEN.ISPF.TLIB') SHR                         
ALLOC F(ISPTLIB) DA('SYSGEN.ISPF.TLIB') SHR                         
/* CREATE USERID.ISP.PROF IF IT DOES NOT EXIST  */                  
IF &SYSDSN('&SYSUID..ISP.PROF') NE &STR(OK) THEN DO                 
    /* CREATE THE DCB INFO */                                       
    ATTRIB PROFS BLKSIZE(3120) LRECL(80) DSORG(PO) RECFM(F,B)       
    /* ALLOCATE THE DATASET */                                      
    ALLOC DSNAME('&SYSUID..ISP.PROF') CYLINDERS SPACE(1,0) DIR(10) +
    VOLUME(PUB001) UNIT(3390) USING(PROFS) NEW                      
    /* FREE THE DCB INFO */                                         
    FREE ATTRLIST(PROFS)                                            
END                                                                 
/* ALLOCATE USER PROFILES */                                        
ALLOC F(ISPPROF) DA('&SYSUID..ISP.PROF') SHR                        
ALLOC F(REVPROF) DA('&SYSUID..ISP.PROF') SHR                        
/* LAUNCH ISPF */                                                   
CALL 'SYSGEN.ISPF.LLIB(ISPF)'                                       
FREE  F(ISPCLIB,ISPLLIB,ISPMLIB,ISPPLIB,ISPSLIB,ISPTABL,ISPTLIB)    
FREE  F(ISPPROF,REVPROF)  
><
//*
//* Replace COMMND00 with custom
//* Replace FTPD PARMLIB
//*
//NEWCOMND EXEC PGM=IEBUPDTE,PARM=NEW
//SYSUT2   DD  DSN=SYS1.PARMLIB,DISP=OLD
//SYSPRINT DD  SYSOUT=*
//SYSIN    DD  *
./ ADD NAME=COMMND00,LIST=ALL
./ NUMBER NEW1=10,INCR=10
COM='SEND 'AUTO COMMANDS IN COMMND00 BEING PROCESSED',CN=01'
COM='START JES2,,,PARM='WARM,NOREQ''                        
COM='START SETPFKEY,M=00'                                   
COM='START FTPDNSEC'                                          
COM='START NET' 
./ ADD NAME=FTPDPM00,LIST=ALL
SRVPORT=2121
SRVIP=ANY
PASVADR=127,0,0,1
PASVPORTS=31337-31347
INSECURE=1
AUTHUSER=IBMUSER
PUB000,3380         PUBLIC DATASETS (PRIVATE)                                      
./ ENDUP  
'''

sources = '''//*
//* Adds sources to MAYHEM.source
//*
//SOURCES   EXEC PGM=IEBUPDTE,REGION=1024K,PARM=NEW
//SYSPRINT  DD SYSOUT=*
//SYSUT2    DD DSN=MAYHEM.SOURCE,DISP=SHR
//SYSIN     DD DATA,DLM=$$
{sources}
$$
'''

execs = '''//*
//* Adds REXX scripts to MAYHEM.EXEC
//*
//REXXEXEC  EXEC PGM=IEBUPDTE,REGION=1024K,PARM=NEW
//SYSPRINT  DD SYSOUT=*
//SYSUT2    DD DSN=MAYHEM.EXEC,DISP=SHR
//SYSIN     DD DATA,DLM=$$
{execs}
$$
'''

mayhemops = '''//*
//* Adds MAYHEM OPS GOALS
//*
//MAYHEM    EXEC PGM=IEBUPDTE,REGION=1024K,PARM=NEW
//SYSPRINT  DD SYSOUT=*
//SYSUT2    DD DSN=MAYHEM.OPS,DISP=SHR
//SYSIN     DD DATA,DLM=$$
{sources}
$$
'''

hint = "./ ADD NAME=MAYHEMOP,LIST=ALL\nI HOPE YOU UNDERSTOOD THE MESSAGE..."

# Creates JCL to upload OVERFLOW files
jcl = ''

print("*** Generating MOTD")
motd = ''
with open(sys.argv[1],'r') as motd_text_file:
    for line in motd_text_file:
        l = len(line.rstrip())
        if l >= 80:
            # the line is too long, truncating
            l = 79
            line = line.rstrip()[:l]
        first_half = line.rstrip()[:math.floor(l/2)]
        second_half = line.rstrip()[math.floor(l/2):]
        motd += "WRITE {first}-\n{second}\n".format(first=first_half,second=second_half)

jcl = MOTDJCL.format(MOTD=motd)

create_pds = '''//*
//* Create PDS to hold overflows
//*
//CREATEOF EXEC PGM=IEFBR14
//SOURCE   DD  DSN=MAYHEM.SOURCE,DISP=(NEW,CATLG),
//             UNIT=SYSDA,VOL=SER=PUB000,
//             SPACE=(TRK,(3,3,3),RLSE),DCB=SYS1.MACLIB
//EXEC     DD  DSN=MAYHEM.EXEC,DISP=(NEW,CATLG),
//             UNIT=SYSDA,VOL=SER=PUB000,
//             SPACE=(TRK,(3,3,3),RLSE),DCB=SYS2.EXEC
//MAYHEMOP DD  DSN=MAYHEM.OPS,DISP=(NEW,CATLG),
//             UNIT=SYSDA,VOL=SER=PUB000,
//             SPACE=(TRK,(3,3,3),RLSE),DCB=SYS1.MACLIB
//FTPDDUMP DD  DSN=MAYHEM.FTPDDUMP,DISP=(NEW,CATLG),    
//             UNIT=SYSDA,VOL=SER=PUB000,                          
//             SPACE=(TRK,(10,5),RLSE),                              
//             DCB=(DSORG=PS,RECFM=FB,LRECL=121,BLKSIZE=400)
'''


print("*** CREATING MAYHEM PDS")


jcl += create_pds

print("*** Adding Source files ")

jcl += sources.format(sources=hint)

with open("matrix.txt", "r") as infile:
    jcl += mayhemops.format( sources = "./ ADD NAME=SCRIPT,LIST=ALL\n{}".format( infile.read() ) )

print("*** Adding REXX execs ")

p = Path("rexx/").glob('**/*')
files = [x for x in p if x.is_file()]

rx = ''
for rexx_script in sorted(files):
    with open(rexx_script,"r") as rexx:
       rx += execs.format( 
        execs="./ ADD NAME={},LIST=ALL\n".format(rexx_script.stem.split('.')[0].upper()) + 
        rexx.read().rstrip() 
        )

jcl += rx

jcl += replace_ispf_clist

print("*** Writting jcl/upload.jcl")
with open("JCL/upload.jcl", "w") as outfile:
    outfile.write(jcl)
