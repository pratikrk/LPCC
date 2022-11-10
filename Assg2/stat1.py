import os
from re import I
LC=0 

EMOT = {    'STOP':('00','IS',1),
            'ADD':('01','IS',1),
            'SUB':('02','IS',1),
            'MUL':('03','IS',1),
            'MOVER':('04','IS',1),
            'MOVEM':('05','IS',1),
            'COMP':('06','IS',1),
            'BC':('07','IS',1),
            'DIV':('08','IS',1),
            'READ':('09','IS',1),
            'PRINT':('10','IS',1),
            'START':('01','AD',3),
            'END':('02','AD',3),
            'ORIGIN':('03','AD',3),
            'EQU':('04','AD',3),
            'LTORG':('05','AD',3),
            'DS':('01','DL',2),
            'DC':('02','DL',2),
            'AREG':('01','RG',4),
            'BREG':('02','RG',4),
            'CREG':('03','RG',4),
            'EQ':('01','CC',5),
            'LT':('02','CC',5),
            'GT':('03','CC',5),
            'NE':('04','CC',5),
            'LE':('05','CC',5),
            'GTE':('06','CC',5),
            'ANY':('07','CC',5)
            }

file=open("F:\Pratik\python\LPCC2\inp.txt")  
  
symtab={}
words=[]

#prints symbol table
def symbol():
    global symtab
    print("Symbol Table:")
    print(symtab)

#handles END directive        
def END():
    global LC
    pool=0
    z=0

#handles LTORG mnemonic
def LTORG():
    global LC
    pool=0
    z=0
    
#handles ORIGIN mnemonic
def ORIGIN(addr):
    global LC
    LC =int(addr)

#handles DS mnemonic
def DS(size):
    global LC
    LC=LC+int(size)

#handles DC mnemonic
def DC(value):
    global LC
    LC+=1


#identifies type of operands i.e. registers, literals, symbols and add approprite data in symbol table.   
def OTHERS(mnemonic,k):
    global words
    global EMOT   
    global symtab
    global LC,symindex
    z=EMOT [ mnemonic]
    i=0
    y=z[-1]
    LC+=1
 

def detect_mn(k):
    global words,LC
    if(words[k]=="START"):
        LC=int(words[1])
    elif(words[k]=='END'):
        END()
    elif(words[k]=="LTORG"):
       LTORG()
    elif(words[k]=="ORIGIN"):
       ORIGIN(words[k+1])
    elif(words[k]=="DS"):
        DS(words[k+1])
    elif(words[k]=="DC"):
        DC(words[k+1])
    else:
        OTHERS(words[k],k)


# main
symindex=0
for line in file:
    #print(line)
    words=line.split()
    #print(words)
   
    k=0
        
    if words[0] in EMOT . keys():
      
        val=EMOT [ words[0]]
        k=0
        detect_mn(k)
    else:
      
        if words[k] not in symtab.keys():
            symtab[words[k]]=(LC,symindex)
            symindex+=1
            # symbol()
        k=1
        detect_mn(k)
print("Symbol Table: ", symtab)
sym=open("SymTab.txt","a+")
sym.truncate(0)
for x in symtab:
    sym.write(x+"\t"+str(symtab[x][0])+"\n")
sym.close()