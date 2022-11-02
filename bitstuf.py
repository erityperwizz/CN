choice=int(input('Choice:\t'))
string = input('Bit-String:\t')
if choice==1:
    print(string.replace('11111', '111110'))
elif choice==0:
    print(string.replace('111110', '11111'))
else:
    print('nope')