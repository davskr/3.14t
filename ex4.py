# to go or not to go
''' DICT

0 = rdeca
1 = rumena
2 = zelena
3 = 
4
5
6



'''

podatki = ['ndemanding', 3]
'''
0 = znacaj bossa
1 = semafor
'''


def boss(podatki):
        
    if podatki[0] == 'demanding':      
        if podatki[1] == 0:
            print('stoj pederu')
        elif podatki[1] == 1:
            print('get ready')
        elif podatki[1] == 2:
            print(1)
        elif podatki[1] == 3:
            print(2)
        else:
            print('spizdi')
        
    else:
        print('yes, boss')  
        

print(boss(podatki))    
