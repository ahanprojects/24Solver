# Program 24 Solver
# Mencari solusi game 24
from itertools import permutations

# operator
def operate(val1,op,val2):
    if val2 == 0:
        return -999
    
    hasil = 0
    if op == '+':
        hasil = val1+val2
    elif op == '-':
        hasil = val1-val2
    elif op == '*':
        hasil = val1*val2
    elif op == '/':
        hasil = val1/val2
    return hasil

# COUNT VALUE
def countValue1(pk,po):
    
    val = operate(pk[0],po[0],pk[1])
    val = operate(val,po[1],pk[2])
    val = operate(val,po[2],pk[3])
    return val

def countValue2(pk,po):
    
    val1 = pk[0]
 
    val2 = operate(pk[1],po[1],pk[2])
    val2 = operate(val2,po[2],pk[3])

    val = operate(val1,po[0],val2)
    return val

def countValue3(pk,po):
    val1 = operate(pk[0],po[0],pk[1])
    val2 = operate(pk[2],po[2],pk[3])

    val = operate(val1,po[1],val2)
    return val

def countValue4(pk,po):
    val1 = pk[0]
    val2 = operate(pk[1],po[1],pk[2])
    val3 = pk[3]

    val12 = operate(val1,po[0],val2)
    val123 = operate(val12,po[0],val3)

    return val123

# Print Jawaban
def printSolution(pk,po,kode):

    if kode == 1:
        print(pk[0],po[0],pk[1],po[1],pk[2],po[2],pk[3],"= 24")
    
    elif kode == 2:
        print(pk[0],po[0],"(",pk[1],po[1],pk[2],po[2],pk[3],") = 24")
        
    elif kode == 3:
        print("(",pk[0],po[0],pk[1],")",po[1],"(",pk[2],po[2],pk[3],") = 24")
    
    elif kode == 4:
        print(pk[0],po[0],"(",pk[1],po[1],pk[2],")",po[2],pk[3],"= 24")

def main():

    # a = [1,2,3,4] ; b=['+','-','*']
    # print(countValue1(a,b)) # 0
    # print(countValue2(a,b)) # -3
    # print(countValue3(a,b)) # -10
    # print(countValue4(a,b)) # 0

    kartu = [(int(input("Kartu"+" "+str(i+1)+" : "))) for i in range(4)]
    allKartu1 = permutations(kartu)
    allKartu = []
    for p in allKartu1:
        allKartu.append(p)

    operator = ['+','-','*','/','+','-','*','/','+','-','*','/']
    allOperator1 = permutations(operator,3)

    allOperator = []
    for p in allOperator1:
        allOperator.append(p)

    solusi1 = []
    solusi2 = []
    solusi3 = []
    solusi4 = []

    for i in range(len(allKartu)):
        pkartu = allKartu[i]
        for j in range(len(allOperator)):
            pop = allOperator[j]
            if pkartu+pop not in solusi1:
                if countValue1(pkartu,pop) == 24:
                    printSolution(pkartu,pop,1)
                    solusi1.append(pkartu+pop)
            if pkartu+pop not in solusi2:
                if countValue2(pkartu,pop) == 24:
                    printSolution(pkartu,pop,2)
                    solusi2.append(pkartu+pop)
            if pkartu+pop not in solusi3:
                if countValue3(pkartu,pop) == 24:
                    printSolution(pkartu,pop,3)
                    solusi3.append(pkartu+pop)
            if pkartu+pop not in solusi4:
                if countValue4(pkartu,pop) == 24:
                    printSolution(pkartu,pop,4)
                    solusi4.append(pkartu+pop)

    if len(solusi1+solusi2+solusi3+solusi4) == 0:
        print("Tidak ada solusi.")
main()