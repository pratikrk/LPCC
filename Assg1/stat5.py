from multiprocessing.context import SpawnContext
from tabulate import tabulate

def processInnerStatement(spaceSeparatedData, SymbolTable, LC):
    if len(spaceSeparatedData) != 1:
        lastParameter = " ".join(spaceSeparatedData[1:]).split(",")[-1].upper().strip()
        if lastParameter[0] != "=":
            if lastParameter not in SymbolTable:
                SymbolTable[lastParameter] = None
        else:
            LiteralTable[lastParameter[1:]] = None
    return LC+1

EMOT = {
    "STOP": ["1", "00"],
    "ADD": ["1", "01"],
    "SUB": ["1", "02"],
    "MULT": ["1", "03"],
    "MOVER": ["1", "04"],
    "MOVEM": ["1", "05"],
    "COMP": ["1", "06"],
    "BC": ["1", "07"],
    "DIV": ["1", "08"],
    "READ": ["1", "09"],
    "PRINT": ["1", "10"],
    "START": ["3", "01"],
    "END": ["3", "02"],
    "ORIGIN": ["3", "03"],
    "EQU": ["3", "04"],
    "LTORG": ["3", "05"],
    "DS": ["2", "01"],
    "DC": ["2", "02"],
    "AREG": ["4", "01"],
    "BREG": ["4", "02"],
    "CREG": ["4", "03"],
    "EQ": ["5", "01"],
    "LT": ["5", "02"],
    "GT": ["5", "03"],
    "NE": ["5", "04"],
    "LE": ["5", "05"],
    "ANY": ["5", "06"]
}

SymbolTable = {}
LiteralTable = {}
LC = 0

file = open("F:\Pratik\python\LPCC1\input5.txt", "r")
for line in file:
    spaceSeparatedData = [data.strip().upper() for data in line.strip().split()]
    if spaceSeparatedData[0] == "START":
        LC = int(spaceSeparatedData[1])
        continue
    
    if spaceSeparatedData[0] not in EMOT:
        SymbolTable[spaceSeparatedData[0]] = LC
        if spaceSeparatedData[1] not in ["DS", "DC"]:
            LC = processInnerStatement(spaceSeparatedData[1:], SymbolTable, LC)
        else:
            LC += 1
    else:
        LC = processInnerStatement(spaceSeparatedData, SymbolTable, LC)

print("\nLiteral Table for given code:")
print(tabulate(LiteralTable.items(), headers=["Literal", "Address"], tablefmt="pretty"))
