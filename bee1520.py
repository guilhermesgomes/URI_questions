# -*- coding: utf-8 -*-
while True:
  try:
    caixas = input()
    
    if caixas != "":  
      parafusos = []
      
      for i in range(int(caixas)):
        lote = input().split()
        
        for j in range(int(lote[0]), int(lote[-1])+1):
          parafusos.append(j)

      parafusos = sorted(parafusos)
      
      num = int(input())
      
      i = 0
      f = len(parafusos)-1
      
      while i < len(parafusos) and parafusos[i] != num:
        i+=1
      
      if i == len(parafusos):
        print ("%d not found") % num
      else:
          while f >= 0 and parafusos[f] != num:
              f-=1 
          print ("%d found from %d to %d") %(num, i, f)
    
  except:
      break