print ('###########################################')
print ('#                Kalkulator               #')
print ('#           Author : Ari Ardana           #')
print ('#    https://facebook.com/arie.ganz.96    #')
print ('#        https://github.com/Ryuzu23       #')
print ('###########################################\n')

def tambah(a, b):
	print ('Jawabannya adalah: ')
	print (a, '+',b, '=',a + b)
	return
def kurang(c, d):
	print ('Jawabannya adalah: ')
	print (c, '-',d, '=',c - d)
	return
def kali(e, f):
	print ('Jawabannya adalah: ')
	print (e, 'x',f, '=',e * f)
	return
def bagi(g, h):
	print ('Jawabannya adalah: ')
	print (g, ':',h, '=',g / h)
	return

def menu():
	pilihan = ['1', '2', '3', '4', '5']
	pilih = '0'
	quit = False
	while not quit:
		while not quit and pilih not in pilihan:
			print ('Pilih salah satu:')
			print ('1. Penjumlahan')
			print ('2. Pengurangan')
			print ('3. Perkalian')
			print ('4. Pembagian')
			print ('5. Keluar')
			pilih = input('Pilih angka 1, 2, 3, 4,atau 5 lalu tekan Enter: ')

			if pilih == '1':
				a = float(input('Angka: '))
				b = float(input('Ditambah dengan angka: '))
				tambah(a, b)
			elif pilih == '2':
				c = float(input('Angka: '))
				d = float(input('Dikurangi dengan angka: '))
				kurang(c, d)
			elif pilih == '3':
				e = float(input('Angka: '))
				f = float(input('Dikali dengan angka: '))
				kali(e, f)
			elif pilih == '4':
				g = float(input('Angka: '))
				h = float(input('Dibagi dengan angka: '))
				bagi(g, h)
			elif pilih == '5':
				quit = True
			pilih = '0'
	return
menu()
