#this program finds larger of the two given numbers
a=10
b=20
def maximum(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        print("Both numbers are equal")
