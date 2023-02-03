def quickSort( sequence ):
    '''Input is a list, output a list with
    the same data sorted using Quick Sort.'''  
    # COMPLETE ME - Yellow task
    # See Codio Guide Section 6 
    # See also Week 9 Lecture Slides
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