def check_function(value,min,max):
    if(min == None):
        return check_the_range1(value, max)
    elif(max == None): 
        return check_the_range2(value,min)
    return check_the_range(value, min,max)

def check_the_range1(value,max):
    if( value > max ):
        return False
    return True

def check_the_range2(value,min):
    if(value<min):
        return False
    return True

def check_the_range(value,min,max):
    if(value< min or value > max):
        return False
    return True


def print_console(string):
  print(string," is out of range")