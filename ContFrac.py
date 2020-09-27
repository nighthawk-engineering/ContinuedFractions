##!/share/dev/tools/bin/python3

a= 431
b= 327

rat = float(a)/float(b)
rat = 3.14159265359
rat = 3.14159

prec = 1e5

print('Rational:',rat)

frac = True
count = 0

while (frac > 0 and count < 1000000):
  itgr = int(rat) 
  frac = rat - itgr
  #print('frac+1 %1.15f; frac-1 %1.15f'%(frac+1,frac-1))
  #print('   ',(frac+1)/(frac-1))
  if (abs((frac+1)/(frac-1))) > prec:
    itgr += 1
    frac = 0
  elif frac < 1/prec:
    frac = 0
  if frac != 0:
    print('%d, %f, %1.15f'%(itgr,frac,1/frac))
    rat = 1/frac
  else:
    print('%d'%itgr)

  #
  count += 1
