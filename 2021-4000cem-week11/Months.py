def numToMonth(n):
    """Given an integer between 1 and 12 return a string with corresponding month"""
    monthNames = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    month = monthNames[n-1]
    return month

