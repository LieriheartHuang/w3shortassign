a=float(input('Enter CPU gigahertz:\n'))

b=int(input('Enter CPU core count:\n'))
     
      
if b>=20:
      print('That is a high-performance CPU.')
elif b>=8 and a>=3.2:
      print('That is a high-performance CPU.')
elif b>=6 and a>=2.5:
      print('That is a medium-performance CPU.')
elif b>=2 and a>=2.0:
      print('That is a low-performance CPU.')
else:
      print('That CPU could use an upgrade.')

