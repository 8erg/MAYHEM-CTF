/* REXX */
"ALLOC F(INFILE) DA('MAYHEM.OPS(SCRIPT)') SHR"
"EXECIO * DISKR INFILE (STEM LINES. FINIS"
do i = 1 to lines.0
    say lines.i
end
"FREE F(INFILE)"
exit
