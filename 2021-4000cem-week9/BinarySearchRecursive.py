def binarySearch( sequence, value ):
    '''Function to find if a value is in a sorted sequence.
       Returns a Boolean indicating this.
       Should implement recursive binary search'''
    # COMPLETE THE FUNCTION
    z=0
    if value == sequence[z]:
        return True
    else:
        return False
        z=z+1
        binarySearch(sequence[z],value)
        