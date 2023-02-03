# Baseless.py
def alsoInfinite(n):
    if n==0:
        print("Finished")
    else:
        print(n)
        alsoInfinite(n+1)
alsoInfinite(4)