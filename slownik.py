produkty = {'s1222': 'sukienka trojkat',
            'p1222': 'spodnie krata' ,
            'x212': 'konsola do gier'}

igla = 'X2X'

if igla in produkty:
    print("Znalazlem {0}".format(igla))
else:
    print('Brak w magazynie {0}'.format(igla))
