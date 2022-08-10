try:
    a = input("Enter the value a\n")
    b = input("Enter the value b\n")

    output = ((float(int(a[6:100])))*2 + int(b[6:100])*2*3.14**3)**0.314

    if output <= 0:
        f = round(output,2)
        print (f)
    else:
        f = round(output,2)
        print ("Program output is", f)

except Exception as e:
    e = "Try Again/Input Correct VALUE for a & b"
    print(e)