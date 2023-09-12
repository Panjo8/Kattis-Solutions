import sys

do_dvajset = ['zero',
'one',
'two',
'three',
'four',
'five',
'six',
'seven',
'eight',
'nine',
'ten',
'eleven',
'twelve',
'thirteen',
'fourteen',
'fifteen',
'sixteen',
'seventeen',
'eighteen',
'nineteen',
]

desetice = {                
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}

def v_besede(stevilo):    
    '''Vrne število 'stevilo' zapisano z besedo.'''
    if stevilo < 20:                        # Število med 0 in 19
        return do_dvajset[stevilo]

    elif stevilo % 10 == 0:                 # Število je večkratnik od 10
        return desetice[stevilo / 10]  

    else:                                   # Katerokoli drugo število
        return "-".join([desetice[stevilo // 10],do_dvajset[stevilo % 10]]) # [desetice ...] ker join iz tabele naredi niz 
                                                                            # vsak niz pa loči s "-"
tabela = []                             
for vrstica in sys.stdin:               
    for beseda in vrstica.split():      
        if not beseda.isdigit():        # Vrne True ali False
            tabela.append(beseda)       # besede na začetku stavka so že zapisane z veliko začetnico
        else:                                       
            tabela.append(v_besede(int(beseda)))

koncno = " ".join(tabela)               # Naredi velik string z vsemi besedami ločene s presledki
print(koncno[0].upper() + koncno[1:])   # samo prvo črko poveča (ker je vse en string)

