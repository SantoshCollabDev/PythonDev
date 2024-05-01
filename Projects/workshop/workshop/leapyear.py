'''
This module has function to calculate leapyear
'''
def is_leap_year(year):
    ''' function to leap year
    '''
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    return False

def leap_years(start, end):
    ''' function to leap year
    '''
    result = [ year for year in range(start, end+1) if is_leap_year(year)]
    return result
