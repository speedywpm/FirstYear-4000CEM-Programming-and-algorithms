def selectionSort( sequence ):
    '''Input is a list, output a list with
    the same data sorted using Selection Sort.'''  
    # COMPLETE ME - Yellow task
    # See Codio Guide Section 4
    aa=0
    n=len(sequence)
    while aa<n:
        bb=0
        while bb<n-1:
            if sequence[bb]>sequence[bb+1]:
                v=sequence[bb]
                b=sequence[bb+1]
                sequence[bb]=b
                sequence[bb+1]=v
                bb=bb+1
            else:
                bb=bb+1
        aa=aa+1
    return sequence