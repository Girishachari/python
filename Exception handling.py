print("starting line ")
a=[11,22,33]

try:
    a=10/5
    print(a[1])
    print(y)
except ZeroDivisionError:
    print("exception  raised due to zero division error")
except IndexError:
    print("exception  raised due to index out of range")
except NameError:
    print("exception  raised due to underfined variable")
except:
    print("some exception raised")
else:
    print("NO exception raised,code is been exuected")
finally:
    print("this is final")
print("outside try block")