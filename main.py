import datetime

def kunlar_soni():
    # Bugungi sana
    bugun = datetime.date.today()
    
    # Ikki kundan keyin sana
    ikki_kun_keyin = bugun + datetime.timedelta(days=2)
    
    # Ikki kundan oldin sana
    ikki_kun_oldin = bugun - datetime.timedelta(days=2)
    
    # Ikki sana orasidagi kunlar sonini hisoblash
    kunlar_soni = (ikki_kun_keyin - ikki_kun_oldin).days + 1
    
    return kunlar_soni

print(kunlar_soni())
