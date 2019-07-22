text = 'ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC'

targ = []

for i in list(text):
    if i == 'A':
        targ.append(4)
    elif i=='B':
        targ.append(3)
    elif i=='C':
        targ.append(2)
    else: 
        targ.append(1)
        
list(map(lambda x: x, targ))