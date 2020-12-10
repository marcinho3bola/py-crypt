# -*- coding: utf-8 -*-
# Este script foi escrito em inglês para o melhor entendimento do código, ja que esta é a lingua universal

import base64
import sys
import os
import time

r = "\033[1;31m"
a = "\033[1;36m"
y = "\033[1;33m"
g = "\033[1;32m"

def banner():
	os.system("clear")
	print(g+"[>                   ] 0%")
	time.sleep(0.25)
	os.system("clear")
	print(g+"[=====>              ] 25%")
	time.sleep(0.25)
	os.system("clear")
	print(g+"[==========>         ] 50%")
	time.sleep(0.25)
	os.system("clear")
	print(g+"[===============>    ] 75%")
	time.sleep(0.25)
	os.system("clear")
	print(g+"[====================] 100%")
	time.sleep(0.25)
	os.system("clear")
	print(g+"""
marcinho3bola

            o
            |
          ,'~'.
         /     \\
        |   ____|_
        |  '___,,_'         .----------------.
        |  ||(o |o)|       (     py-crypt!    )
        |   -------         ,----------------'
        |  _____|         -'
        \  '####,
         -------
       /________\\
     (  )        |)
     '_ ' ,------|\         _
    /_ /  |      |_\        ||
   /_ /|  |     o| _\      _||
  /_ / |  |      |\ _\____//' |
 (  (  |  |      | (_,_,_,____/
  \ _\ |   ------|
   \ _\|_________|
    \ _\ \__\\\\__\\
    |__| |__||__|
 ||/__/  |__||__|
         |__||__|
         |__||__|
         /__)/__)
        /__//__/
       /__//__/
      /__//__/.
    .'    '.   '.
   (_________)____)

------------------------------------------------
""")
	print (a + 'Coded by: marcinho3bola')
	print (a + 'GitHub: https://github.com/marcinho3bola\n')

try:
	banner()
	file = raw_input(y + 'Input file path >>> ')
except IndexError:
	print (r+'\n\n[!] Your file isn\'t working!\n')
	sys.exit()
except KeyboardInterrupt:
	print (r+'\n\n[!] Exiting...\n')
	sys.exit()
except EOFError:
	print (r+'\n\n[!] Exiting...\n')
	sys.exit()
else:
	try:
		fileopen = open(file).read()
	except IOError:
		print (r+'[!] This file doesn\'t exist!\n')
		sys.exit()
	try:
		a = base64.b64encode(fileopen)
	except TypeError:
		print (c+'[!]file already encrypted\n')
		sys.exit()

b = g + "#Encrypted by marcinho3bola\n#GitHub: https://Github.com/marcinho3bola\nimport base64\nexec(base64.b64decode('" + a + "'))"
c = file.replace('.py', '_enc.py')
d = open(c, 'w')
d.write(b)
d.close()
print ('\n' + b + '\033[1;36m\n\n[*] File encrypted!')
