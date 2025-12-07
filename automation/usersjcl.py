#!/usr/bin/env python3

from pathlib import Path


# This job does all the magic
USERJOB = ('''//{usern} JOB (1),'ADD {usern}',CLASS=S,MSGLEVEL=(1,1),
//             MSGCLASS=A,USER=IBMUSER,PASSWORD=SYS1,NOTIFY=IBMUSER
// EXEC TSONUSER,ID={usern},
//      PW='{usern}',
//      PR='IKJACCNT',
//      OP='NOOPER',
//      AC='NOACCT',
//      JC='JCL',
//      MT='NOMOUNT'
//STEP01   EXEC PGM=IEFBR14   
//DUMP001  DD  DSN={usern}.DUMP001,DISP=(NEW,CATLG),    
//             UNIT=SYSDA,VOL=SER=PUB000,                          
//             SPACE=(TRK,(10,5),RLSE),                              
//             DCB=(DSORG=PS,RECFM=FB,LRECL=121,BLKSIZE=400)       
//DUMP002  DD  DSN={usern}.DUMP002,DISP=(NEW,CATLG),    
//             UNIT=SYSDA,VOL=SER=PUB000,                          
//             SPACE=(TRK,(10,5),RLSE),                              
//             DCB=(DSORG=PS,RECFM=FB,LRECL=121,BLKSIZE=400)        
//DUMP003  DD  DSN={usern}.DUMP003,DISP=(NEW,CATLG),    
//             UNIT=SYSDA,VOL=SER=PUB000,                          
//             SPACE=(TRK,(10,5),RLSE),                              
//             DCB=(DSORG=PS,RECFM=FB,LRECL=121,BLKSIZE=400)        
//DUMP004  DD  DSN={usern}.DUMP004,DISP=(NEW,CATLG),    
//             UNIT=SYSDA,VOL=SER=PUB000,                          
//             SPACE=(TRK,(10,5),RLSE),                              
//             DCB=(DSORG=PS,RECFM=FB,LRECL=121,BLKSIZE=400)
//JCLLIB   DD  DSN={usern}.JCLLIB,DISP=(NEW,CATLG),
//             UNIT=SYSDA,VOL=SER=PUB000,
//             SPACE=(CYL,(1,1,20)),DCB=SYS1.MACLIB 
//* COPY ALL MEMBERS FROM ONE PDS TO ANOTHER
//COPYTHEM EXEC PGM=IEBCOPY
//SYSPRINT DD SYSOUT=*
//* SYSUT1 is source SYSUT2 is destination
//SYSUT1 DD DSN=MAYHEM.OPS,DISP=SHR
//SYSUT2 DD DSN={usern}.OPS,DISP=SHR
//SYSIN DD DUMMY
//* 
//* COPY ALL MEMBERS FROM ONE PDS TO ANOTHER
//*
//COPYOVRF EXEC PGM=IEBCOPY
//SYSPRINT DD SYSOUT=*
//* SYSUT1 is source SYSUT2 is destination
//SYSUT1 DD DSN=MAYHEM.EXEC,DISP=SHR
//SYSUT2 DD DSN={usern}.EXEC,DISP=SHR
//SYSIN DD DUMMY
//*
//* 
//* COPY ALL MEMBERS FROM ONE PDS TO ANOTHER
//*
//COPYOVRF EXEC PGM=IEBCOPY
//SYSPRINT DD SYSOUT=*
//* SYSUT1 is source SYSUT2 is destination
//SYSUT1 DD DSN=MAYHEM.FTPDUMP,DISP=SHR
//SYSUT2 DD DSN={usern}.FTPDUMP,DISP=SHR
//SYSIN DD DUMMY
//*
//COPYSRC  EXEC PGM=IEBCOPY
//SYSPRINT DD SYSOUT=*
//* SYSUT1 is source SYSUT2 is destination
//SYSUT1 DD DSN=MAYHEM.SOURCE,DISP=SHR
//SYSUT2 DD DSN={usern}.SOURCE,DISP=SHR
//SYSIN DD DUMMY
//* 
''')

for x in range(0,2):
    with open("users/MH{}.jcl".format(str(x).zfill(2)), 'w') as jclfile:
        print("*** Writting users/MH{}.jcl".format(str(x).zfill(2)))
        jclfile.write(USERJOB.format(usern="MH{}".format(str(x).zfill(2))))

