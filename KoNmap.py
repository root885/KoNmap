#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system("apt-get update")
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet KoNmap")
print("""
Turkish Nmap Scan Project 

1) IP PROTOCOL TARAMASI
2) UDP TARAMASI
3) FTP TARAMASI
4) ZOMBIE HOST BOSTA TARAMA
5) COOKIE ECHO TARAMALARI
6) XMAS TARAMALARI
7) HEDEF ISLETIM SISTEM BILGISI


""")

islemno = input("İşlem Numarasını Girin: ")


if(islemno=="1"):

 
	 hedefip = input("Hedef İp Girin: ")
	 os.system("nmap -v " + hedefip)
elif(islemno=="2"):

	  hedefip = input("Hedef İp Girin: ")
	  os.system("nmap -v -sU " + hedefip)
elif(islemno=="3"):
 
	 hedefip = input("Hedef İp Girin: ")
	 os.system("nmap -v -b " + hedefip)
elif(islemno=="4"):
 
	 hedefip = input("Hedef İp Girin: ")
	 os.system("nmap -v -sI " + hedefip)	
elif(islemno=="5"):
 
	 hedefip = input("Hedef İp Girin: ")
	 os.system("nmap -v -sZ " + hedefip)	
elif(islemno=="6"):
 
	 hedefip = input("Hedef İp Girin: ")
	 os.system("nmap -v -sX " + hedefip)
elif(islemno=="7"):

	 hedefip = input("Hedef İp Girin: ")
	 os.system("nmap -v -sV " + hedefip)		
else:
	print("Hatalı Seçim Yaptınız. Program Kapatılıyor.")
