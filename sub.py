#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
#Maklum kalo berantakan ster
G0 = '\033[0;32m'
C0 = '\033[0;36m'
W0 = '\033[0;37m'
R0 = '\033[0;31m'
import json,os,requests,sys
try:
	os.system('clear')
	print '''%s
  _________    ___.        .___      
 /   _____/__ _\_ |__    __| _/____     %sCoded by D4RKSH4D0WS%s
 \_____  \|  |  \ __ \  / __ |/  _ \    %sIG @anonroz_team%s
 /        \  |  / \_\ \/ /_/ (  <_> )   %sFB gg.gg/AnonRoz-Team%s
/_______  /____/|___  /\____ |\____/    Subdomain finder
        \/          \/      \/       
'''%(C0,W0,C0,W0,C0,W0,C0)
	for site in open(sys.argv[1]).read().splitlines():
		if '://' in site:
			site=site.split('://')[1]
		print '%s[%s•%s] In process %s ...'%(W0,R0,W0,site)
		api=requests.get('https://crt.sh/?q='+site+'&output=json',headers={'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'}).json()
		c=0
		while True:
			try:c+=1;open('1','a+').write(api[c]['name_value']+'\n')
			except IndexError:break
		result=[]
		for x in open('1').read().split('\n'):
			if 'www' in x:continue
			elif '*' in x:continue
			else:open('2','a+').write(x+'\n')
		os.system('rm -rf 1')
		for sub in open('2').read().split('\n'):
			if sub in result:continue
			else:result.append(sub);open('sub-'+sys.argv[1]+'.txt','a+').write('http://'+sub+'\n')
		os.system('rm -rf 2')
		print '%s[%s✓%s] %s subdomains found for %s\n'%(W0,G0,W0,len(result),site)
	print '%s[%s✓%s] Done, saved in sub-%s.txt'%(W0,G0,W0,sys.argv[1])
except requests.exceptions.ConnectionError:exit('%s[%s!%s] Check internet'%(W0,R0,W0))
except IndexError:exit('%s[%s!%s] Use : python2 %s list.txt'%(W0,R0,W0,sys.argv[0]))
except IOError:exit('%s[%s×%s] File does not exist'%(W0,R0,W0))
except KeyboardInterrupt:exit('\n%s[%s!%s] Exit'%(W0,R0,W0))