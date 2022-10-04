def main(prvni, druhy):
    lower = 0 if len(prvni) - len(druhy) <=0 else 1
    l = [prvni,druhy]
    return (int(((len(l[lower-1])/len(l[lower]))+1))*l[lower])[:len(l[lower-1])]



prvni = "Antananss"
druhy = "Berlín"
print(main(prvni, druhy))

