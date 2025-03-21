'''
Güncel F-1 Değerleri:
    test  --> 0.8574850299401197
    test1 --> 0.8584070796460176
    test2 --> 0.8782816229116944
    test3 --> 0.8385650224215246
    test4 --> 0.9588377723970944
    test5 --> 0.953125
    test6 --> 0.9114583333333333 (400 positive, 100 negative)
    test7 --> 0.6381322957198443 (400 negative, 100 positive)
'''
from pandas import read_excel
from polarite import calculatePolarite
import jpype

# excel'i pythona aktarıyoruz
data = read_excel('data/test.xlsx', index_col=None, header=None, skiprows=1)
dataLen = int(data.size/2)

returnMatrix = [] # geri dönen değeri tutacak bir matrix açıyoruz. // gerçek değer / tahmini değer

# Her satırı teker teker fonksiyonumuza sokup dönen değerleri depoluyoruz.
for i in range(0, dataLen):
    temp = [list(filter(lambda i: i != " ", str(data.at[i, 1])))[0].lower() == "p", calculatePolarite(str(data.at[i, 0]))]
    returnMatrix.append(temp)

    # Cümle yanlış tahmin edildiyse printliyor.
    if temp[0] != temp[1]:
        print("Hatalı polarite olan cümle --> ", str(data.at[i, 0]), returnMatrix[i][0], returnMatrix[i][1])
        

# Karmaşıklık Matrixi Hesaplama Kısmı
karMatrix = [[0, 0],[0, 0]] # [[DP, YP],[YN, DN]]

for index,i in enumerate(returnMatrix):
    if i[0] == i[1]:
        if i[0]:
            karMatrix[0][0] += 1 #DP
        else:
            karMatrix[1][1] += 1 #DN
    else:
        if i[1]:
            karMatrix[0][1] += 1 #YP
        else:
            karMatrix[1][0] += 1 #YN
    # print(data.at[index, 0] + " : " + str(i[0]) + " " + str(i[1])) # Test print

dogruluk = (karMatrix[0][0] + karMatrix[1][1])/dataLen
kesinlik = (karMatrix[0][0])/(karMatrix[0][0] + karMatrix[0][1])
anma = (karMatrix[0][0])/(karMatrix[0][0] + karMatrix[1][0])
f1olc = (2*kesinlik*anma)/(kesinlik+anma)

print()
print(karMatrix[0])
print(karMatrix[1])
print(f"Doğruluk: {dogruluk}, Kesinlik: {kesinlik}, Anma: {anma}, F1-Ölçütü: {f1olc}")

jpype.shutdownJVM()