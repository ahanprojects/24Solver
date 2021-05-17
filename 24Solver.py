# Program 24 Solver
# Mencari solusi game 24
from sympy.utilities.iterables import multiset_permutations

# operator
def operate(val1,op,val2):
    if val2 == 0:
        return -99999999
    
    hasil = 0
    if op == '+':
        hasil = val1+val2
    elif op == '-':
        hasil = val1-val2
    elif op == '×':
        hasil = val1*val2
    elif op == '÷':
        hasil = val1/val2
    return hasil

# COUNT VALUE
def countValue1(pk,po):
    # 1, 2, 3
    valAB = operate(pk[0],po[0],pk[1])
    valABC = operate(valAB,po[1],pk[2])
    valABCD = operate(valABC,po[2],pk[3])
    return valABCD

def countValue2(pk,po):
    # 1, 3, 2 dan 3, 1, 2
    valAB = operate(pk[0],po[0],pk[1])
    valCD = operate(pk[2],po[2],pk[3])
    valABCD = operate(valAB,po[1],valCD)

    return valABCD

def countValue3(pk,po):
    # 2, 1, 3
    valBC = operate(pk[1],po[1],pk[2])
    valABC = operate(pk[0],po[0],valBC)
    valABCD = operate(valABC,po[2],pk[3])

    return valABCD

def countValue4(pk,po):
    # 2, 3, 1
    valBC = operate(pk[1],po[1],pk[2])
    valBCD = operate(valBC,po[2],pk[3])
    valABCD = operate(pk[0],po[0],valBCD)

    return valABCD

def countValue5(pk,po):
    # 2, 3, 1
    valCD = operate(pk[2],po[2],pk[3])
    valBCD = operate(pk[1],po[1],valCD)
    valABCD = operate(pk[0],po[0],valBCD)

    return valABCD

# Print Jawaban
def printSolution(pk,po,kode):

    out = -999
    if kode == 1:
        out = "((( {} {} {} ) {} {} ) {} {} ) = 24".format(pk[0],po[0],pk[1],po[1],pk[2],po[2],pk[3])
    
    elif kode == 2:
        out = "(( {} {} {} ) {} ( {} {} {} )) = 24".format(pk[0],po[0],pk[1],po[1],pk[2],po[2],pk[3])

    elif kode == 3:
        out = "(( {} {} ( {} {} {} )) {} {} ) = 24".format(pk[0],po[0],pk[1],po[1],pk[2],po[2],pk[3])

    elif kode == 4:
        out = "( {} {} (( {} {} {} ) {} {} )) = 24".format(pk[0],po[0],pk[1],po[1],pk[2],po[2],pk[3])
    
    elif kode == 5:
        out = "( {} {} ( {} {} ( {} {} {} ))) = 24".format(pk[0],po[0],pk[1],po[1],pk[2],po[2],pk[3])
    
    return out

def main():

    # permutasi semua kartu
    kartu = [(int(input("Kartu"+" "+str(i+1)+" : "))) for i in range(4)]
    permKartu = list(multiset_permutations(kartu))

    # permutasi semua operasi hitung
    op = ['+','+','+','-','-','-','×','×','×','÷','÷','÷']
    permOp = list(multiset_permutations(op,3))

    # himpunan solusi
    himpunan_solusi = []
    jumlah_tes = 0
    # menghitung nilai semua permutasi (angka, operasi hitung, kurung)
    for i in range(len(permKartu)):
        current_kartu = permKartu[i]
        for j in range(len(permOp)):
            current_op = permOp[j]
            jumlah_tes += 5
            if countValue1(current_kartu,current_op) == 24:
                himpunan_solusi.append(printSolution(current_kartu,current_op,1))

            if countValue2(current_kartu,current_op) == 24:
                himpunan_solusi.append(printSolution(current_kartu,current_op,2))

            if countValue3(current_kartu,current_op) == 24:
                himpunan_solusi.append(printSolution(current_kartu,current_op,3))

            if countValue4(current_kartu,current_op) == 24:
                himpunan_solusi.append(printSolution(current_kartu,current_op,4))

            if countValue5(current_kartu,current_op) == 24:
                himpunan_solusi.append(printSolution(current_kartu,current_op,5))
    
    if len(himpunan_solusi) == 0:
        print("Tidak ada solusi.")
    else:
        print("{} solusi ditemukan :".format(len(himpunan_solusi)))
        for solusi in himpunan_solusi:
            print(solusi)
        
    print("{} permutasi dicoba.".format(jumlah_tes))
main()