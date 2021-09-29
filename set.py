#https://www.youtube.com/watch?v=Qul_UT5nYrw&list=PLA0M1Bcd0w8xIdFNA95aQrwJ_GQJEV8ko&index=19

setA = {1,2,3,4}
setB = set([3,4,5,6])

setE = setA | setB
setR = setA.union(setB)
print(setE)
print(setR)

setC = setA & setB
setd = setA.intersection(setB)

print(setC)
print(setd)