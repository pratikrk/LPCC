import os

LC=0 

EMOT = {'STOP':('00',1),
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

file=open("F:\Pratik\python\LPCC1\input.txt")  #Enter input file with complete path if not in same directory
  

symtab={}   #Sybol Table
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