user=input('enter your NI anumber')
user1=int(input('enter your salary:'))
if user1<=12570:
    print("no tax")
elif user1>=12571 and user1<=50270:
    taxrate1=(user1-12570)*.20
    print("20% of tax",'%.2f'%taxrate1)
elif user1>=50271 and user1<=150000:
    taxrate20=(50270-12570)*.2
    taxrate40=(user1-50270)*.4
    taxrate2=taxrate20+taxrate40
    print("40% of tax",'%.2f'%taxrate2)
elif user1>150000:
    taxratenew20=(50270-12570)*.2
    taxratenew40=(150000-50270)*.4
    taxratenew45=(user1-150000)*.45
    taxrate3=taxratenew20+taxratenew40+taxratenew45
    print("45% of tax",'%.2f'%taxrate3)
else:
    print("invalid")
print("****NI Calculation Rates***")
#calculate ni
salmon=user1/12
print('salary per month:','%.2f'%salmon)
if salmon>=520 and salmon<=797:
    print("No N.I")
elif salmon>797 and salmon<=4189:
    NIcontribution=(salmon-797)*.12
    NIcontributionnew=NIcontribution*12
    print("NIcontributionannumnew",'%.2f'%NIcontributionnew)
    takehome1=user1-taxrate1- NIcontributionnew
    print("takehome","%.2f"%takehome1)
elif salmon>4189:
    ni=(4189-797)*.12
    ninew=(salmon-4189)*.02
    ninew2=(ni+ninew)*12
    print("nicontriannumnew",'%.2f'%ninew2)
    takehome2=user1-taxrate2-ninew2
    print("takehome","%.2f"%takehome2)
"""elif user1>150000 and salmon>4189:
    ni=(4189-797)*.12
    ninew=(salmon-4189)*.02
    ninew2=(ni+ninew)*12
    print("nicontriannumnew",'%.2f'%ninew2)
    takehome3=user1-taxrate3-ninew2
    print("takehome","%.2f"%takehome3)"""
    
    


