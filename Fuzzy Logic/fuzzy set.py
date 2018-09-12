from Shape import Shape
from Berita import Berita

import math

def fuzzification(nilai, tipe):
    hasil=[]
    result=[]
    jenis=[]
    if (tipe== "emosi"):
        vlow= Shape(0, 10, 30)
        low= Shape(10, 30, 50)
        norm= Shape(30, 50, 70)
        high= Shape(50, 70, 90)
        vhigh= Shape(70, 90, 100)
    elif (tipe=="provokasi"):
        vlow= Shape(0, 10, 30)
        low= Shape(10, 30, 39)
        norm= Shape(30, 50, 74)
        high= Shape(71, 85, 90)
        vhigh= Shape(75, 81, 100)

    if nilai < vlow.c and nilai >vlow.a or nilai==0:
        if(nilai>=vlow.a and nilai<=vlow.b):
            result.append(1)
        else:
            hasil.append(vlow)
        jenis.append(0)
    if nilai >low.a and nilai <low.c:
        hasil.append(low)
        jenis.append(1)
    if nilai>norm.a and nilai <norm.c :
        hasil.append(norm)
        jenis.append(2)
    if nilai>high.a and nilai<high.c:
        hasil.append(high)
        jenis.append(3)
    if nilai>vhigh.a and nilai<vhigh.c:
        if(nilai>=vhigh.b and nilai<=vhigh.c):
            result.append(1)
        else:
            hasil.append(vhigh)
        jenis.append(4)
    if nilai==100:
        result.append(1)
        jenis.append(4)


    for index in range(len(hasil)):
        if nilai==100:
            temp=1;
        elif(nilai>hasil[index].a) and (nilai<=hasil[index].b):
            asdf=(nilai-hasil[index].a)
            dsa=(hasil[index].b-hasil[index].a)*1.0
            temp= asdf/dsa   
        elif (nilai>hasil[index].b and nilai<=hasil[index].c):
            asdf= (-(nilai-hasil[index].c))
            dsa=(hasil[index].c-hasil[index].b)
            temp= asdf/(dsa*1.0)
        else:
            temp=1
        result.append(temp)
    return result, jenis

def inference(rules, emosi, provokasi):
	hasil=[]
	hasil2=[]
	for indexe in range (len(emosi[0])):
		for indexp in range (len(provokasi[0])):
			esmosi= emosi[1][indexe]
			propokasi= provokasi[1][indexp]
			hasil.append(rules[esmosi][propokasi])
			hasil2.append(pickMin(emosi[0][indexe],provokasi[0][indexp]))
	return pickMax(hasil2, hasil), hasil


#-9999= true gada #cek ada true ato false ato keduanya
#-8888= false gada #array pertama == true #array dua=false

def mandaniMaBro(itung, bool):
	cekTrue=False
	cekFalse=False
	if(itung[0]!=-9999):
		cekTrue=True
	if (itung[1]!=-8888):
		cekFalse=True

	if(cekTrue and cekFalse):
		yyy=float((itung[0]*4.0)+(itung[1]*4.0))
		xxx=((60+70+80+90)*itung[0])+((10+20+30+40)*itung[1])
		return (xxx/yyy)
	elif (cekTrue and not cekFalse):
		yyy= float(itung[0]*4.0)
		return(((60+70+80+90)*itung[0])/yyy)
	elif (not cekTrue and cekFalse):
		yyy= float(itung[1]*4.0)
		return(((10+20+30+40)*itung[1])/yyy)			


def mandanitoStringMaBro(int):
	if int>=50.0:
		return "Ya"
	else:
		return "Tidak"

def pickMin(a,b):
	if a<b:
		return a
	elif a>b:
		return b
	else:
		return a

def pickMax(a, b):
	maxTrue=-9999
	maxFalse=-8888
	for index in range(len(a)):
		if(a[index]>maxTrue and b[index]==True):
			maxTrue=a[index]
		elif(a[index]>maxFalse and b[index]==False):
			maxFalse=a[index]
	return maxTrue, maxFalse


rules=[]
rules.append([False, False, False, False, True]) 
rules.append([False, False, False, False, True])
rules.append([False, False, False, True, True])
rules.append([False, False, False, True, True])
rules.append([False, False, True, True, True])

daftar_berita=[]
#10 pertama
daftar_berita.append(Berita(97,74))
daftar_berita.append(Berita(36,85))
daftar_berita.append(Berita(63,43))
daftar_berita.append(Berita(82,90))
daftar_berita.append(Berita(71,25))
daftar_berita.append(Berita(79,81))
daftar_berita.append(Berita(55,62))
daftar_berita.append(Berita(57,45))
daftar_berita.append(Berita(40,65))
daftar_berita.append(Berita(57,45))

#10 data tengah
daftar_berita.append(Berita(77,70))
daftar_berita.append(Berita(68,75))
daftar_berita.append(Berita(60,70))
daftar_berita.append(Berita(82,90))
daftar_berita.append(Berita(40,85))
daftar_berita.append(Berita(80,68))
daftar_berita.append(Berita(60,72))
daftar_berita.append(Berita(50,95))
daftar_berita.append(Berita(100,18))
daftar_berita.append(Berita(11,99))

#10 data terakhir
daftar_berita.append(Berita(58,63))
daftar_berita.append(Berita(68,70))
daftar_berita.append(Berita(64,66))
daftar_berita.append(Berita(57,77))
daftar_berita.append(Berita(77,55))
daftar_berita.append(Berita(98,64))
daftar_berita.append(Berita(91,59))
daftar_berita.append(Berita(50,95))
daftar_berita.append(Berita(95,55))
daftar_berita.append(Berita(27,79))

#main program
index=1
#
for news in daftar_berita:
    result= fuzzification(news.emosi, "emosi")
    result1= fuzzification(news.provokasi, "provokasi")
    hasil=inference(rules, result, result1)
    panteque= mandaniMaBro(hasil[0], hasil[1][0])
    z=mandanitoStringMaBro(math.ceil(panteque))
    print("Berita ", index, " : ", z) #,z
    # print(z)
    index+=1
