def maiusculas(frase):
    import unicodedata as uncd
    print (re.findall('[A-Z]',uncd.normalize('NFKD',frase)) )
    
