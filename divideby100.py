n = input()
m = input()

dolzina_n = len(n)
dolzina_m = len(m)

razlika_dolzin = abs(dolzina_n - dolzina_m)

if dolzina_n < dolzina_m:
    # v sprem. decimalna_mesta spravimo število ponovitev števke 0 na mestih
    # decimalk. -1 dodamo ker se morata števili med seboj razlikovati za dve
    # ali več mest v dolžini za pojavitev ene ali več 0 v decimalnem zapisu
    decimalna_mesta = razlika_dolzin - 1
    print("0." + "0" * decimalna_mesta + n)
else:
    prvi_del_st = razlika_dolzin + 1
    prvi_del = n[:prvi_del_st]
    drugi_del = n[prvi_del_st:]
    # odstraniti moramo odvečne ničle na mestu decimalk
    for i in range(dolzina_m - 1):
        # če je drugi_del prazen ali pa smo naleteli na decimalno mesto,
        # ki je različno od 0 zaključimo odstranjevanje ničel
        if drugi_del[-1] != "0" or drugi_del == "":
            break
        drugi_del = drugi_del[:-1]
    if drugi_del == "":
        print(prvi_del)
    else:
        print(prvi_del + "." + drugi_del)
    

    
