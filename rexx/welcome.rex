/* REXX */
/* Display content from member MAYHEM.OPS(SCRIPT) */

dsname = "MAYHEM.OPS(SCRIPT)"     /* The PDS member with your text */

/* Allocate the dataset member */
"ALLOC F(INFILE) DA('"dsname"') SHR"

/* Read all lines into a stem variable */
"EXECIO * DISKR INFILE (STEM LINES. FINIS"

/* Display each line */
do i = 1 to lines.0
    say lines.i
end

/* Free the dataset */
"FREE F(INFILE)"

exit
