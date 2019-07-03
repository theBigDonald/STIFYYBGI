from ONU import winninglist as comparisonlist

lstlst = []

with open ("scoretable.txt") as filehandle:
    for lists in range (0,5):
        comp = filehandle.readline()
        #print(i)
        if comp.endswith('\n'):
            #print(comp.strip())
            #if len(i.strip()) > 2:
            #    print ('%s is bigger than 2' %i.strip())
            comp = comp.strip()
            comp = comp.replace('10', '0')
            lstlst.append(comp)

for comparison in range(0,5):
    comp = ''.join(comparisonlist)
    comp = comp.replace('10', '0')
    if len(comp) > len(lstlst[comparison]):
        comparisonlist = lstlst[comparison]
        lstlst[comparison] = str(comp)

        with open ('scoretable.txt', 'w') as filehandle:
            for i in range(0,5):
                filehandle.write('%s\n' %lstlst[i])
    else:
        continue



        

