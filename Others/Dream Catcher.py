print('''
o          `O        o                                                    o.OOOo.   `OooOOo.  o.OOoOoo    Oo    Oo      oO        .oOOOo.     Oo    oOoOOoOOo  .oOOOo.  o      O o.OOoOoo `OooOOo.
O           o       O                                                      O    `o   o     `o  O         o  O   O O    o o       .O     o    o  O       o     .O     o  O      o  O        o     `o
o           O       o                                     O                o      O  O      O  o        O    o  o  o  O  O       o          O    o      o     o         o      O  o        O      O
O           O       O                                    oOo               O      o  o     .O  ooOO    oOooOoOo O   Oo   O       o         oOooOoOo     O     o         OoOooOOo  ooOO     o     .O
o     o     o .oOo. o  .oOo  .oOo. `oOOoOO. .oOo.         o   .oOo.        o      O  OOooOO'   O       o      O O        o       o         o      O     o     o         o      O  O        OOooOO'
O     O     O OooO' O  O     O   o  O  o  o OooO'         O   O   o        O      o  o    o    o       O      o o        O       O         O      o     O     O         O      o  o        o    o
`o   O o   O' O     o  o     o   O  o  O  O O             o   o   O        o    .O'  O     O   O       o      O o        O       `o     .o o      O     O     `o     .o o      o  O        O     O
 `OoO' `OoO'  `OoO' Oo `OoO' `OoO'  O  o  o `OoO'         `oO `OoO'        OooOO'    O      o ooOooOoO O.     O O        o        `OoooO'  O.     O     o'     `OoooO'  o      O ooOooOoO  O      o

''')

my_dreams={}


def multiple_values():
    dream_catcher = True
    while dream_catcher:
        print("Here is everything you have logged before\n")
        for date, note in my_dreams.items():
            print(f"{date} → {note}")
        if not my_dreams:
            print("Nothing yet!")
        diary_date = input("Enter date in the format month/day, eg- Jan/01: ")
        diary_note = input("Enter your note for today: ")
        my_dreams[diary_date] = diary_note

        rerun=input("Do you want to rerun the program? Type y for yes and n for no.").lower()
        if rerun!="y":
            dream_catcher=False
            print("Have a nice day!!")
multiple_values()