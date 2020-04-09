#!/usr/bin/env python
import os
import sys
import hashlib
import getpass
import re

def altera01():
    with open("/home/usuario/ZIMBRA/roles/zimbra/vars/main.yml",'r+') as f:
        x = f.read()
        print ("Estado atual do arquivo que sera alterado")
        print (x)

def altera02(dado1, dado2):
    with open("/home/usuario/ZIMBRA/roles/zimbra/vars/main.yml",'r+') as f:
        x = f.read()
        w = re.split("\s",x)
        resultado1 = w[3]
        resultado2 = w[7]
        final1 = x.replace(resultado1,dado1)
        final2 = final1.replace(resultado2,dado2)
        print (final2)
        f.seek(0)
	f.write(final2)
	f.truncate()
        os.system("ansible-playbook -i /home/usuario/ZIMBRA/hosts /home/usuario/ZIMBRA/site.yml -K -k")

def altera03():
        print ("Nenhuma alteracao foi realizada, Obrigado")
		
def main():
    p = raw_input("Entre com o email:  ")
    q = getpass.getpass()
    print ("sua senha e : "), q
    altera01()
    j = raw_input("Voce gostaria de realizar esta alteracao? Sim(s) ou Nao(n): ")
    if j == "s":
      altera02(p,q)
    else:
      altera03()


if __name__ == '__main__':
    main()
