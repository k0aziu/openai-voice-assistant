t1 = ['1', '2', '3']
t2 = ['2', '54']
t3 = ['k', 's']


def chuj(*listte):
    qwer = []
    # print(listte)
    for i in listte:
        for q in i:
            qwer.append(q)
            
    print(qwer)
    
    
chuj(t1, t2, t3)