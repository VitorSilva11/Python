metro = float(input('Digite O Valor Em Metros: '))

km = metro / 1000
dam = metro / 10
hm = metro / 100
dm = metro * 10
cm = metro * 100
mm = metro * 1000

print('{} KM'.format(km))
print('{} HM'.format(hm))
print('{} DAM'.format(dam))
print('{:.0f} DM'.format(dm))
print('{:.0f} CM'.format(cm))
print('{:.0f} MM'.format(mm))
