'''
print list of leap years given the start and 
end years according to the gregorian calender
Additional:
----------
  2000: yes
  2100: No
Leap year:
----------
Every year that is exactly divisible by 4 is a 
leap year, except for years that are exactly
divisible by 100, but these centurial years are
leap years if they are exactly divisible by 400.
For example, the years 1700 and 1900 are not leap years,
but the years 1600 and 2000
'''
def is_leap(year):
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

### Approach 2 - Filters
print(list(filter(is_leap,range(1998,2010))))
print(list(filter(is_leap,range(2098,2110))))

### Approach 2 - List comprehension
print([year for year in range(1998,2010) if is_leap(year)])
print([year for year in range(2098,2110) if is_leap(year)])