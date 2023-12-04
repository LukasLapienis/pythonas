with open('10Failas/02data.txt', 'r+', encoding='utf-8') as f:
    txt = f.read()
    print(txt)
    f.seek(2) # sugrazinamas zymeklis i bylos pradzia
    t1 = int(f.readline())
    t2 = int(f.readline())
    t3 = int(f.readline())
    print((t3))
    s = t1 + t2 + t3
    f.write(f'\n{t1} + {t2} + {t3} = {s}\n')