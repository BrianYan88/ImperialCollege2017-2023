def fatty_gen(x,y,z):
    fat_acid=''
    if y==0:
        fat_acid=fat_acid+x*'C'+'(=O)O'
    elif z=='E':
        fat_acid=fat_acid+(x-y-1)*'C'+'\C=C\\' + (y-1)*'C'+ '(=O)O'
    #return fat_acid
    elif z=='Z':
        fat_acid=fat_acid+(x-y-1)*'C'+'/C=C\\' + (y-1)*'C'+ '(=O)O'
    else:
        fat_acid=fat_acid+(x-y-1)*'C'+'C=C' + (y-1)*'C'+ '(=O)O'
    print(fat_acid)
x1=input("Chain length?")
x=int(x1)
y1=input("Double bond position?")
y=int(y1)
z=input("Orientation?")

fatty_gen(x,y,z)

input("Press return to close the window.")