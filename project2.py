#Ayoka Gooding 
#COSC 450
#Python
# The purpose for this program is to find the product of two matrices 
# from numbers given from a txt file and print the product matrix in a new file.


file1 = open("COSC450_P2_Data.txt","r")
Numbers = file1.readline()
file1.close()
Nums = Numbers.split()
numsArray=[]

for i in Nums:
    numsArray.append(int(i))
numNums= len(numsArray)


X = numNums/5
matrix1 = [[0 for i in range(X)] for j in range(5)]
count =0
for i in range(5):
    for j in range(X):
        matrix1[i][j] = numsArray[count]
        count = count +1
print("First Matrix")
print("")
print(matrix1)
print("")
print("")

matrix2 = [[0 for i in range(5)] for j in range(X)]
count=0
for i in range(X):
    for j in range(5):
        matrix2[i][j] = numsArray[count]
        count = count +1
        
        
print("Second Matrix") 
print("")
print(matrix2)
print("")
print("")


FinalMatrix = [[0 for i in range(5)] for j in range(5)]
for i in range(0,5):
    for j in range(0,5):
        for k in range(0,X):
            FinalMatrix[i][j] += matrix1[i][k] * matrix2[k][j]
            
        
print("Product") 
print(FinalMatrix)


#Adding Matrices to the file
newFile = open("COSC450_P2_Output.txt","w")
newFile.write("First Matrix \n")
for row in matrix1:
    newFile.write(str(row)+"\n")
    
	
newFile.write("Second Matrix \n")

for row in matrix2:
    newFile.write(str(row)+"\n")

newFile.close() 

newFile = open("COSC450_P2_Output.txt","a")
newFile.write("Product \n")
for row in FinalMatrix:
    newFile.write(str(row)+"\n")
    print("")
print("")
print("")
  
newFile.close()



#End of the Program