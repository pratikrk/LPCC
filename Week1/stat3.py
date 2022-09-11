import os

mnemonics={'STOP':('00',1),
            'ADD':('01',1),
            'SUB':('02',1),
            'MUL':('03',1),
            'MOVER':('04',1),
            'MOVEM':('05',1),
            'COMP':('06',1),
            'BC':('07',1),
            'DIV':('08',1),
            'READ':('09',1),
            'PRINT':('10',1),
            'START':('01',3),
            'END':('02',3),
            'ORIGIN':('03',3),
            'EQU':('04',3),
            'LTORG':('05',3),
            'DS':('01',2),
            'DC':('02',2),
            'AREG':('01',4),
            'BREG':('02',4),
            'CREG':('03',4),
            'EQ':('01',5),
            'LT':('02',5),
            'GT':('03',5),
            'NE':('04',5),
            'LE':('05',5),
            'GTE':('06',5),
            'ANY':('07',5)
            }

file=open("F:\Pratik\python\LPCC1\input.txt")

symtab={}
words=[]

# main
symindex=0
for line in file:

    words=line.split()
    print(words)
    k=0
        
    if words[0] in mnemonics.keys():
        val=mnemonics[words[0]]
        k=0
    else:
        if words[k] not in symtab.keys():
            symtab[words[k]]=(symindex)
            symindex+=1
        k=1
    
print("Symbol Table: ", symtab)

sym=open("SymTab.txt","a+")
sym.truncate(0)
for x in symtab:
    sym.write(x+"\n")
sym.close()
