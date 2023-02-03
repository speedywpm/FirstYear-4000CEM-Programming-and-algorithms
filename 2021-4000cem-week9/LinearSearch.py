
def linearSearch( sequence, value ):
        '''Function to iterate through a sequence in search of a value.  
           Returns a Boolean indicating if the value is in the sequence '''
        z=0
        for entry in sequence:
            if entry==value:
                return True
        return False

