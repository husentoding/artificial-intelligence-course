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

	# Dataset Tugas 3 AI 1718.xlsx


#kfold
#pilih kfold
#cek akurasi tiap fold
#	>> lakukan knn
#	>> data 1 ke 1, data 1 ke 2, data 1 ke 3


def euclidean(a, b):
	print("euclid a: ",a, "b: ", b)
	return math.sqrt(((a[0]-b[0])**2) + ((a[1]-b[1])**2) + ((a[2]-b[2])**2) + ((a[3]-b[3])**2))

def findMaxClass(riri):
	jum_nol=0;
	jum_satu=0;
	for i in range(len(riri)):
		if (riri[i]==0):
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

def satuknn(datatest, datatraining, k):
	hasil=[]
	for i in range(len(datatraining)):
		print("INI DATA TEST: ", datatest)
		hasil.append(euclidean(datatest, datatraining[i]))
	kterbaik= cariPalingGanteng(manipulasiNol(hasil), k)
	return findMaxClass(kterbaik)

def knn(datatest, datatraining, k):
	hasil=[]
	best=[]
	for i in range(len(datatest)):
		for j in range(len(datatraining)):
			satuknn(datatest[i], datatraining[j], k)





def kfold(k, jum_row):
	#inisialisasi indeks fold 
	kece= jum_row/k
	test_index=[]
	for i in range(0, k):
		test_index.append(i*kece)
	test_index.append(jum_row-1)

	#start
#	for i in range(0, k):




#main
eksel= open_workbook('Dataset Tugas 3 AI 1718.xlsx')
data_kereta = eksel.sheets()[0]

jum_row= data_kereta.nrows	
jum_col= data_kereta.ncols

all_data=[]

for row in range(1, 9):
	one_row= []
	for col in range(1, jum_col):
		one_cell= data_kereta.cell(row,col).value
		one_row.append(one_cell)
	all_data.append(one_row)
asdf=[1,1,1,0,0,0,0]

a=[]
b=[]
a.append(all_data[0])
a.append(all_data[1])
a.append(all_data[2])
b.append(all_data[3])
b.append(all_data[4])
b.append(all_data[5])

tes=knn(a,b,1)
hasil= cariPalingGanteng(manipulasiNol(tes),3)



# #reset tes
# tes=knn(a,b,1)
# print(tes)

# for i in range(len(hasil)):
# 	print(tes[hasil[i]])