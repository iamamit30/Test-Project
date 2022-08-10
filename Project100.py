# a = 'apache1.0'
# b = 'apache2.0'
try:
    a = input("Enter the value a\n")
    b = input("Enter the value b\n")

    version = ((float(int(a[6:100])))*2 + int(b[6:100])*2*3.14**3)**0.314

    if version <= 0:
        f = round(version,2)
        print (f)
    else:
        f = round(version,2)
        print ("Program version value is", f)

except Exception as e:
    e = "Try Again/Input Correct VALUE for a & b"
    print(e)
    