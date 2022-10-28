def parrot(voltage, state='a stiff',action='voom',type='Norwegian Blue'):
    print('-- this parrot wouldnt', action, end=' ')
    print('if you put', voltage,)
    #..................................

parrot(1000) #1st argument
parrot(voltage=1000) #keyword argument
parrot('a mil', 'berefit of life') #positional argument
parrot('1k', state='pushing') #positional and keyword
parrot(actor="Someone") #unknown keyword arg
parrot(110 , voltage=220) #duplicate value for the same argument