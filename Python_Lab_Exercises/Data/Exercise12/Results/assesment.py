import sys
landuse=sys.argv[1]
value=int(sys.argv[2])

if landuse=="SFR":
    rate=0.05
elif landuse=="MFR":
    rate=0.04
else:
    rate=0.02
assesment=value*rate
print assesment