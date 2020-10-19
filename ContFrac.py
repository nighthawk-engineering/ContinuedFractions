##!/share/dev/tools/bin/python3

#import mpmath as mp
from mpmath import *
import numpy as np

mp.dps = 100
print('digit precision:',mp.dps)

a= 431
b= 327

digs = 43

#rat = mpf(a/b)
#rat = mpf(np.pi) # doesn't return a good binary value for PI -- don't use this
piVal = '3.1415926535897932384626433832795028841971693993751'
rat = mpf(piVal[0:digs+2])
#rat = mpf('3.1415926')
print('Rat:',rat)

prec = mpf('1e15')
ndigits = len(str(rat))-2
print('number of digits',ndigits)
frac = True
count = 0
cfrac = []

while (frac > 0 and count < 1000000):
  itgr = int(rat) 
  #
  frac = rat - mpf(itgr); rat = rat
  #print('frac+1 %1.15f; frac-1 %1.15f'%(frac+1,frac-1))
  #print('   ',(frac+1)/(frac-1))
  if (abs((frac+1)/(frac-1))) > prec:
    itgr += 1
    frac = 0
  elif frac < 1/prec:
    frac = 0
  if frac != 0:
    #print('%d, %f,'%(itgr,frac),1/frac)
    #print(itgr,end=',')
    rat = mpf(1)/frac
  else:
    #print('%d'%itgr)
    pass
  cfrac.append(str(itgr))
  #
  count += 1

print('\nNotation: ',end='')
print('['+cfrac[0]+';'+','.join(cfrac[1:])+']')
print()
if count == 1000000:
  print('Exceeded max count')
else:
  fmt = 'Last rat %.'+str(ndigits)+'f'
  print(fmt%rat)

####################################################

a0 = cfrac.pop(0)
cfrac.reverse()
an = cfrac.pop(0)
val = 1/mpf(an)
for a in cfrac:
  val = 1/(mpf(a) + val)
val += mpf(a0)
print('Original',piVal[0:digs+2])
print('   Model',val)