from xlrd import open_workbook
import math
class Data(object):
	def __init__(self, idberita, like, provokasi, komentar, emosi, hoax):
		self.idberita= idberita
		self.like= like
		self.provokasi= provokasi
		self.komentar= komentar
		self.emosi= emosi
		self.hoax= hoax

def euclidean(a, b):
	return math.sqrt(((a[0]-b[0])**2) + ((a[1]-b[1])**2) + ((a[2]-b[2])**2) + ((a[3]-b[3])**2))*1.0

#rr adalah array yg digunakan untuk ngecek class// harusnya datatraining punya
def findMaxClass(indeks, riri):
	jum_nol=0
	jum_satu=0
	for i in range(len(indeks)):
		cek= riri[indeks[i]]
		if (int(cek[4])==0):
			jum_nol+=1
		else:
			jum_satu+=1
	# if jum_nol==jum_satu:
		# return 9999
	return 0 if jum_nol>jum_satu else 1

def manipulasiNol(aduhhh):
	panteque=aduhhh

	for i in range (len(panteque)):
		if(panteque[i]==0):
			panteque[i]=6666666
	return panteque

def carimin(array):
	s=999
	indeks=0;
	for i in range(len(array)):
		if array[i]<s:
			s=array[i]
			indeks=i
	return int(indeks)

#kalau mau caripaling ganteng di manipulasi dlu
def cariPalingGanteng(husen, k):
	n=0
	ini=husen
	hasil=[]
	jum_pop=0
	for i in range(len(ini)):
		if n==k:
			break
		else:
			tes=ini.index(min(ini))
			hasil.append(tes)
			ini[tes]=999
			n+=1
	return hasil	
#data test itu cuma 1 data training ada banyak
def satuknn(datatest, datatraining, k):
	hasil=[]
	for i in range(len(datatraining)):
		hasil.append(euclidean(datatest, datatraining[i]))
	kterbaik= cariPalingGanteng(manipulasiNol(hasil), k)
	return findMaxClass(kterbaik, datatraining)

def knn(datatest, datatraining, k):
	hasil=[]
	for i in range(len(datatest)):
		hasil.append(satuknn(datatest[i], datatraining, k))
	return hasil
#bakal nge load a-1 jumlah data, a minimal =1, b>a
def loadData(a,b):
	if a==0:
		a=1
	eksel= open_workbook('Dataset Tugas 3 AI 1718.xlsx')
	data_kereta = eksel.sheets()[0]

	jum_row= data_kereta.nrows	
	jum_col= data_kereta.ncols
	all_data=[]
	for row in range(a, b):
		one_row= []
		for col in range(1, jum_col):
			one_cell= data_kereta.cell(row,col).value
			one_row.append(one_cell)
		all_data.append(one_row)

	return all_data

def cekAkurasi(hasil, dataTest):
	a=0
	for i in range(len(hasil)):
		# print("if ", hasil[i], "==", dataTest[i][4])
		if hasil[i]== int(dataTest[i][4]):
			a+=1
	return (a*1.0/len(hasil))*100

def kfold(k, jum_row, jum_knn):
	#inisialisasi indeks fold 
	kece= jum_row/k
	test_index=[]
	for i in range(0, k):
		test_index.append(i*kece)
	test_index.append(jum_row-1)
	content=[]
	#masukin data ke content
	for i in range(len(test_index)-1):
		content.append(loadData(test_index[i], test_index[i+1]))

	#mulai kfold
	data_train=[]
	hasilakurasi=[]
	hasil=[]
	for i in range(len(content)):
		hasil=[]
		data_test= content[i]
		for j in range(len(content)):
			if(i!=j):
				data_train= data_train+ content[j]
		#KNN 3

		hasil.append(knn(data_test, data_train, jum_knn))

		akurasi= cekAkurasi(hasil[0], data_test)
		hasilakurasi.append(akurasi)
	total=0
	for i in range(len(hasilakurasi)):
		total= total+hasilakurasi[i]


	return total/len(hasilakurasi)

#main

for i in range(2):
	jum_k=1
	jum_fold=(i+1)*4
	for j in range(2):
		jum_k+=2
		akurasi=kfold(jum_fold, 4002,jum_k)
		print("Akurasi ", i, j, " ", akurasi, " Jumlah Fold: ", jum_fold, " Jumlah kNN: ", jum_k)

