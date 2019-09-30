def taxcalc(landuse,value):
    if landuse=="SFR":
        rate=0.05
    elif landuse=="MFR":
        rate=0.04
    else:
        rate=0.02
    assesment=rate*value
    return assesment