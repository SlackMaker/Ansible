#!/usr/bin/env python

import sys
import os
import re

def recebe(a,b):
  with open('/home/usuario/ACL/playacl/vars/main.yml','r+') as f:
    x = f.read()
    print (x)
    w = re.split("\s",x)
    resultado1 = w[2]
    resultado2 = w[5]
    novo01 = x.replace(resultado1,a)
    novo02 = novo01.replace(resultado2,b)
    print (novo02)
    Resultado = raw_input(' Voce gostaria de efetuar as alteracoes acima ? (1) Sim - (2) Nao: ')
    if Resultado == '1':
      f.seek(0)
      f.write(novo02)
      f.truncate()
      print(novo02)
    else:
      print('Gravacao nao efetuada, estado do arquivo atual')
      print (x)


def main():
  print (' ACL Permissao usuario siga as informacoes abaixo ')
  p = raw_input("Digite o Caminho: ")
  j = raw_input("Digite o Nome: ")
  recebe(p,j)


if __name__=="__main__":
  try:
    main()
  except KeyboardInterrupt:
    print "nnVoce pressionou Ctrl+C ou Delete para interromper este programa!n"
